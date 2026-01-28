import pandas as pd
from collections import defaultdict
from datetime import date, timedelta
import math


def consolidar_cronicos_anual_2026(path_excel: str) -> pd.DataFrame:
    """
    Limpia y consolida despacho semanal de crónicos
    desde 'CRONICOS 2026'.
    """

    df = pd.read_excel(
        path_excel,
        sheet_name="CRONICOS 2026",
        usecols="C,G,H",
        skiprows=1,
        names=["medicamento", "dias", "dosis_total"]
    )

    df["medicamento"] = (
        df["medicamento"]
        .astype(str)
        .str.upper()
        .str.strip()
    )

    inicio_virtual = date(2026, 1, 1)
    acumulado = defaultdict(float)

    for _, row in df.iterrows():
        nombre = row["medicamento"]
        dias = row["dias"]
        dosis = row["dosis_total"]

        if not nombre or dosis <= 0:
            continue

        es_inhalador = "INHALA" in nombre or "AERO" in nombre

        if es_inhalador:
            semana = inicio_virtual.isocalendar().week
            key = (semana, nombre)
            acumulado[key] += 1

        else:
            if 28 <= dias <= 31:
                dosis_semanal = dosis / 4
                for j in range(4):
                    fecha = inicio_virtual + timedelta(days=j * 7)
                    semana = fecha.isocalendar().week
                    key = (semana, nombre)
                    acumulado[key] += dosis_semanal

            elif dias > 31:
                semana = inicio_virtual.isocalendar().week
                key = (semana, nombre)
                acumulado[key] += dosis

    # Convertir a DataFrame
    data = [
        {
            "semana_id": f"Semana {semana:02d}",
            "medicamento": med,
            "cantidad_consolidada": math.ceil(cantidad)
        }
        for (semana, med), cantidad in acumulado.items()
    ]

    resultado = pd.DataFrame(data).sort_values(
        by=["semana_id", "medicamento"]
    )

    return resultado.reset_index(drop=True)
