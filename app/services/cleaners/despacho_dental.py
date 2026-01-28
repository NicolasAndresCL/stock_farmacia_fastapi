# app/services/cleaners/despacho_dental.py

import pandas as pd
from pathlib import Path


def consolidar_despacho_dental(
    path_excel: Path,
    sheet_name: str = "COLECTIVA DENTAL 2026"
) -> pd.DataFrame:
    """
    Extrae despacho dental desde libro COLECTIVA MODULOS.
    Replica exactamente la lógica de la macro VBA.
    """

    df = pd.read_excel(
        path_excel,
        sheet_name=sheet_name,
        usecols="A:C",
        skiprows=2,      # Empieza en fila 3
        nrows=3          # Filas 3 a 5
    )

    df.columns = ["FECHA", "MEDICAMENTO", "TOTAL_DESPACHADO"]

    df = df[df["MEDICAMENTO"].notna()]

    return df.reset_index(drop=True)
