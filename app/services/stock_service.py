import pandas as pd
from typing import List

from app.core.logger import logger


class StockService:
    """
    Servicio central de consolidación de stock.
    NO lee Excel.
    SOLO consolida movimientos.
    """

    REQUIRED_COLUMNS = {"medicamento", "cantidad", "tipo"}

    @staticmethod
    def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
        df.columns = (
            pd.Series(df.columns)
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )
        return df

    @staticmethod
    def validate_dataframe(df: pd.DataFrame, source: str = ""):
        missing = StockService.REQUIRED_COLUMNS - set(df.columns)
        if missing:
            msg = f"DataFrame inválido{f' ({source})' if source else ''}. Faltan columnas: {missing}"
            logger.error(msg)
            raise ValueError(msg)

    @staticmethod
    def consolidate_movements(dfs: List[pd.DataFrame]) -> pd.DataFrame:
        """
        Une múltiples DataFrames de movimientos
        """
        logger.info("Consolidando movimientos de stock")

        normalized = []

        for idx, df in enumerate(dfs):
            df = StockService.normalize_columns(df)
            StockService.validate_dataframe(df, source=f"df_{idx}")
            normalized.append(df)

        movements_df = pd.concat(normalized, ignore_index=True)
        logger.info(f"Movimientos totales: {len(movements_df)}")

        return movements_df

    @staticmethod
    def calculate_stock(movements_df: pd.DataFrame) -> pd.DataFrame:
        """
        Calcula el stock final por medicamento
        """
        logger.info("Calculando stock final")

        df = movements_df.copy()

        # Egresos restan
        df["cantidad_real"] = df.apply(
            lambda r: -r["cantidad"] if r["tipo"] == "egreso" else r["cantidad"],
            axis=1
        )

        stock_df = (
            df.groupby("medicamento", as_index=False)["cantidad_real"]
            .sum()
            .rename(columns={"cantidad_real": "stock"})
            .sort_values("medicamento")
        )

        return stock_df
