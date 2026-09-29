"""Descarga y caché local de precios de activos.

Por defecto se apoya en `yfinance`, pero la idea es que `source` permita
enchufar otros proveedores de datos en el futuro.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DEFAULT_CACHE_DIR = Path(__file__).resolve().parents[2] / "data" / "cache"


def download_prices(
    tickers: str | list[str],
    start: str | None = None,
    end: str | None = None,
    interval: str = "1d",
    source: str = "yfinance",
    use_cache: bool = True,
    cache_dir: str | Path = DEFAULT_CACHE_DIR,
) -> pd.DataFrame:
    """Descarga precios (ajustados) para uno o varios tickers.

    Parameters
    ----------
    tickers : str | list[str]
        Ticker o lista de tickers a descargar.
    start, end : str | None
        Fechas límite en formato "YYYY-MM-DD".
    interval : str
        Frecuencia de los datos (por defecto diaria).
    source : str
        Proveedor de datos a usar ("yfinance" por defecto).
    use_cache : bool
        Si True, intenta leer/escribir en `cache_dir` antes de descargar.
    cache_dir : str | Path
        Carpeta donde se guarda la caché local (incluida en .gitignore).

    Returns
    -------
    pd.DataFrame
        Precios indexados por fecha, una columna por ticker.
    """
    raise NotImplementedError


def load_from_cache(key: str, cache_dir: str | Path = DEFAULT_CACHE_DIR) -> pd.DataFrame | None:
    """Carga datos cacheados en disco si existen, o None si no hay caché."""
    raise NotImplementedError


def save_to_cache(data: pd.DataFrame, key: str, cache_dir: str | Path = DEFAULT_CACHE_DIR) -> None:
    """Guarda un DataFrame en la caché local."""
    raise NotImplementedError
