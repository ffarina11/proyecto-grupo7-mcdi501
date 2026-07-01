"""
functions.py — Grupo 7 MCDI501
Funciones reutilizables del proyecto.
"""

import pandas as pd
import numpy as np
from IPython.display import display


def cargar_dataset(ruta: str, sep: str = ";") -> pd.DataFrame:
    """
    Carga un archivo CSV y retorna un DataFrame.
    Maneja los errores más comunes de lectura.
    """
    try:
        df = pd.read_csv(ruta, sep=sep)
        print(f"✓ Dataset cargado correctamente desde: {ruta}")
        print(f"  {df.shape[0]:,} filas × {df.shape[1]} columnas")
        return df
    except FileNotFoundError:
        print(f"✗ Archivo no encontrado: {ruta}")
        print("  Verifica que data_predict.csv esté en data/raw/")
        raise
    except Exception as e:
        print(f"✗ Error al cargar el archivo: {e}")
        raise


def mostrar_primeras_filas(df: pd.DataFrame, n: int = 5) -> None:
    """Muestra las primeras n filas del DataFrame."""
    print(f"\nPrimeras {n} filas:")
    display(df.head(n))


def resumen_dataset(df: pd.DataFrame, nombre: str = "Dataset") -> None:
    """
    Muestra un resumen estructural del DataFrame:
    filas, columnas, duplicados, NaN y tipos de datos.
    """
    print(f"\n{'='*55}")
    print(f"  RESUMEN — {nombre}")
    print(f"{'='*55}")
    print(f"  Filas             : {df.shape[0]:,}")
    print(f"  Columnas          : {df.shape[1]}")
    print(f"  Duplicados        : {df.duplicated().sum():,}")
    print(f"  Valores NaN total : {df.isnull().sum().sum():,}")
    print(f"\n  Tipos de datos:")
    for dtype, count in df.dtypes.astype(str).value_counts().items():
        print(f"    {dtype:15s} : {count} columnas")
    print(f"{'='*55}")
