import numpy as np
from PIL import Image, UnidentifiedImageError
import tifffile as tiff
import io
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
import os

def to_uint8(a: np.ndarray) -> np.ndarray:
    if a.dtype == np.uint8:
        return a
    a = a.astype(np.float32)
    if a.max() <= 1.0:
        a *= 255
    return np.clip(a, 0, 255).astype(np.uint8)

def read_tiff_quiet(path: str) -> np.ndarray:
    buf = io.StringIO()
    with redirect_stdout(buf), redirect_stderr(buf):
        try:
            return tiff.imread(path)
        except:
            with tiff.TiffFile(path) as tf:
                return tf.pages[0].asarray()

def safe_open(path: str) -> Image.Image:
    p = os.path.expanduser(path.strip())
    if not os.path.isfile(p):
        raise FileNotFoundError(f"No se encontró la imagen: {p}")

    try:
        im = Image.open(p)
        im.load()
        if im.mode != "RGB":
            im = im.convert("RGB")
        return im
    except UnidentifiedImageError as e:
        pil_error = e
    except Exception as e:
        pil_error = e

    if Path(p).suffix.lower() in (".tif", ".tiff"):
        try:
            arr = read_tiff_quiet(p)
            arr = to_uint8(arr)
            if arr.ndim == 2:
                im = Image.fromarray(arr, "L").convert("RGB")
            elif arr.ndim == 3:
                if arr.shape[-1] >= 3:
                    im = Image.fromarray(arr[..., :3]).convert("RGB")
                else:
                    im = Image.fromarray(np.repeat(arr, 3, axis=-1)).convert("RGB")
            else:
                raise ValueError("Formato TIFF no compatible (dimensiones extrañas).")
            return im
        except Exception as e:
            raise RuntimeError(f"Error al abrir TIFF: {p}") from e

    if isinstance(pil_error, UnidentifiedImageError):
        raise ValueError(f"El archivo no es una imagen válida: {p}") from pil_error
    raise RuntimeError(f"Error al abrir la imagen: {p}") from pil_error