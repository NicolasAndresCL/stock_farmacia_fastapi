# app/services/cleaners/despacho_modulo.py

import pandas as pd
from pathlib import Path


def consolidar_despacho_modulo(
    path_excel: Path,
    sheet_name: str = "COLECTIVA MODULOS 2026"
) -> pd.DataFrame:
    """
    Extrae despacho directo de módulos.
    Replica exactamente la lógica del VBA.
    """

    df = pd.read_excel(
        path_excel,
        sheet_name=sheet_name,
        usecols="A,B,F",
        skiprows=3,      # Empieza en fila 4
        nrows=20         # Hasta fila 23 inclusive
    )

    df.columns = ["FECHA", "MEDICAMENTO", "TOTAL_DESPACHADO"]

    # Limpieza básica
    df = df[df["MEDICAMENTO"].notna()]
    df["MEDICAMENTO"] = df["MEDICAMENTO"].astype(str).str.strip().str.upper()

    return df.reset_index(drop=True)
