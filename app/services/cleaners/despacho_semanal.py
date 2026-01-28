# app/services/cleaners/despacho_semanal.py

import pandas as pd
from datetime import date, timedelta
import math


def consolidar_despacho_semanal(
    path_excel: str,
    sheet_name: str,
    anio: int = 2026
) -> pd.DataFrame:
    """
    Consolida despacho semanal desde libros CRONICOS o PSICOTROPICOS.
    Replica la lógica de macros VBA.
    """

    df = pd.read_excel(
        path_excel,
        sheet_name=sheet_name,
        usecols="C,G,H",
        skiprows=0
    )

    df.columns = ["medicamento", "dias", "dosis_total"]

    df["medicamento"] = (
        df["medicamento"]
        .astype(str)
        .str.strip()
        .str.upper()
    )

    df = df[df["dosis_total"] > 0]

    inicio_virtual = date(anio, 1, 1)
    registros = []

    for _, row in df.iterrows():
        med = row["medicamento"]
        dias = row["dias"]
        dosis = row["dosis_total"]

        if not med:
            continue

        es_inhalador = ("INHALA" in med) or ("AERO" in med)

        if es_inhalador:
            semana = inicio_virtual.isocalendar().week
            registros.append({
                "Semana_ID": f"Semana {semana:02d}",
                "Medicamento": med,
                "Cantidad_Consolidada": 1
            })

        else:
            if 28 <= dias <= 31:
                dosis_semana = dosis / 4
                for j in range(4):
                    fecha = inicio_virtual + timedelta(days=j * 7)
                    semana = fecha.isocalendar().week
                    registros.append({
                        "Semana_ID": f"Semana {semana:02d}",
                        "Medicamento": med,
                        "Cantidad_Consolidada": dosis_semana
                    })

            elif dias > 31:
                semana = inicio_virtual.isocalendar().week
                registros.append({
                    "Semana_ID": f"Semana {semana:02d}",
                    "Medicamento": med,
                    "Cantidad_Consolidada": dosis
                })

    resultado = (
        pd.DataFrame(registros)
        .groupby(["Semana_ID", "Medicamento"], as_index=False)
        .agg({"Cantidad_Consolidada": "sum"})
    )

    resultado["Cantidad_Consolidada"] = (
        resultado["Cantidad_Consolidada"]
        .apply(lambda x: math.ceil(x))
    )

    resultado = resultado.sort_values("Semana_ID")

    return resultado
