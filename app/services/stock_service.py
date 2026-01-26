import pandas as pd
from typing import List
from pathlib import Path

from app.core.logger import logger


class StockService:
    """
    Service responsible for reading, cleaning and consolidating
    stock data from Excel files.
    """

    REQUIRED_COLUMNS = {
        "medicamento",
        "cantidad"
    }

    @staticmethod
    def read_excel_files(files: List[Path]) -> pd.DataFrame:
        """
        Read multiple Excel files and concatenate them
        """
        dataframes = []

        for file_path in files:
            logger.info(f"Reading file: {file_path}")

            df = pd.read_excel(file_path)
            df.columns = StockService.normalize_columns(df.columns)

            StockService.validate_columns(df, file_path)

            dataframes.append(df)

        combined_df = pd.concat(dataframes, ignore_index=True)
        logger.info(f"Combined dataframe shape: {combined_df.shape}")

        return combined_df

    @staticmethod
    def normalize_columns(columns):
        """
        Normalize column names: lowercase, strip spaces
        """
        return (
            pd.Series(columns)
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

    @staticmethod
    def validate_columns(df: pd.DataFrame, file_path: Path):
        """
        Ensure required columns exist
        """
        missing = StockService.REQUIRED_COLUMNS - set(df.columns)

        if missing:
            error_msg = f"{file_path.name} missing columns: {missing}"
            logger.error(error_msg)
            raise ValueError(error_msg)

    @staticmethod
    def calculate_stock(df: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate real stock per medication
        """
        logger.info("Calculating stock")

        stock_df = (
            df.groupby("medicamento", as_index=False)["cantidad"]
            .sum()
            .sort_values("medicamento")
        )

        return stock_df
