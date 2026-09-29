"""Descarga y caché local de precios de activos.

Por defecto se apoya en `yfinance`, pero la idea es que `source` permita
enchufar otros proveedores de datos en el futuro.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import yfinance as yf

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
    # Garantiza que sea una lista
    tickers = [tickers] if isinstance(tickers, str) else list(tickers)

    # Comprobamos si lo tenemos en la cache y sino descargamos
    key = f"{'_'.join(sorted(tickers))}_{start}_{end}_{interval}"

    if use_cache:
        cached = load_from_cache(key, cache_dir)
    if cached is not None:
        return cached          # ya estaba guardado: no descarga
        
    # Descargamos los activos    
    data = yf.download(
        tickers,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=True,
        progress=False,
    )["Close"]
    # Garantiza que sea un DataFrame
    if isinstance(data, pd.Series):      # por si viniera un solo ticker como Series
        data = data.to_frame(tickers[0])
    return data


def load_from_cache(key, cache_dir=DEFAULT_CACHE_DIR):
    """Carga datos cacheados en disco si existen, o None si no hay caché."""
    path = Path(cache_dir) / f"{key}.csv"
    if not path.exists():
        return None
    return pd.read_csv(path, index_col=0, parse_dates=True)


def save_to_cache(data, key, cache_dir=DEFAULT_CACHE_DIR):
    """Guarda un DataFrame en la caché local."""
    Path(cache_dir).mkdir(parents=True, exist_ok=True)
    data.to_csv(Path(cache_dir) / f"{key}.csv")