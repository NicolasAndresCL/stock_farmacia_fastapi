# app/services/cleaners/recetas_blancas.py

import pandas as pd
import math
from pathlib import Path


def consolidar_recetas_blancas(
    path_excel: Path,
    sheet_name: str = "ENE 26"
) -> pd.DataFrame:
    """
    Consolida recetas blancas por semana y medicamento.
    Replica exactamente la lógica del módulo VBA.
    """

    df = pd.read_excel(
        path_excel,
        sheet_name=sheet_name,
        usecols="E,J,K,N"
    )

    df.columns = ["MEDICAMENTO", "DIAS", "FECHA", "TOTAL"]

    # Limpieza base
    df["MEDICAMENTO"] = df["MEDICAMENTO"].astype(str).str.strip().str.upper()
    df = df[
        (df["MEDICAMENTO"] != "") &
        (df["TOTAL"] > 0) &
        (pd.notna(df["FECHA"]))
    ]

    registros = []

    for _, row in df.iterrows():
        medicamento = row["MEDICAMENTO"]
        dias = row["DIAS"]
        total = row["TOTAL"]
        fecha_base = pd.to_datetime(row["FECHA"])

        # Caso A: 30 días → 4 semanas
        if dias == 30:
            dosis_semana = total / 4

            for j in range(4):
                fecha_virtual = fecha_base + pd.Timedelta(days=j * 7)
                semana = fecha_virtual.week

                registros.append({
                    "Semana_ID": f"Semana {semana:02d}",
                    "Medicamento": medicamento,
                    "Cantidad": dosis_semana
                })

        # Caso B: otro número de días
        else:
            semana = fecha_base.week

            registros.append({
                "Semana_ID": f"Semana {semana:02d}",
                "Medicamento": medicamento,
                "Cantidad": total
            })

    resultado = (
        pd.DataFrame(registros)
        .groupby(["Semana_ID", "Medicamento"], as_index=False)
        .agg({"Cantidad": "sum"})
    )

    resultado["Cantidad"] = resultado["Cantidad"].apply(lambda x: math.ceil(x))

    return resultado.sort_values(["Semana_ID", "Medicamento"]).reset_index(drop=True)
