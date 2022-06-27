
"""
usage ex:

from src.app.data.data.db import DataBase
from datetime import date, timedelta
start_date = date.today() - timedelta(days=300)
df = DataBase.get_data('sqqq',start_date, date.today())
"""

from enum import Enum
from typing import List
import os
from functools import lru_cache

import yfinance as yf
import pandas as pd

DIR_PATH = os.path.dirname(os.path.realpath(__file__))



class BaseEnum(Enum):
    

    @classmethod
    def keys(cls)-> List[str]:
        """_summary_

        Returns:
            List[str]: _description_
        """
        return [property.value for property in cls]

    
    

class Columns(BaseEnum):
    DATE = 'Date'
    OPEN = 'Open'
    HIGH = 'High'
    LOW = 'LOW'
    CLOSE = 'Low'
    ADJ_CLOSE = 'Adj Close'
    VOLUME = 'Volume'


class Tickers(BaseEnum):
    SQQQ = 'sqqq'
    TQQQ = 'tqqq'


class FileTypes(BaseEnum):
    CSV = 'csv'


class DataBase:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_data( ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        """_summary_

        Args:
            ticker (str): _description_
            start_date (str): _description_
            end_date (str): _description_

        Returns:
            pd.DataFrame: _description_
        """
        start_date_str = str(start_date)
        end_date_str = str(end_date)
        file_name = f"{ticker}_{start_date_str}_{end_date_str}.{FileTypes.CSV.value}"
        fully_qualified_file_name = os.path.join(DIR_PATH,file_name)
        if not os.path.exists(fully_qualified_file_name):
            print(f"Downloading data set for ticker: {ticker} from {start_date_str} to {end_date_str}.")
            data = yf.download(ticker, start=start_date_str,end=end_date_str)
            if data.size > 0:
                data.to_csv(fully_qualified_file_name)
        return DataBase.load_ticker(ticker=ticker, fully_qualified_file_name=fully_qualified_file_name)


    @staticmethod
    # @lru_cache
    def load_ticker(ticker: str, fully_qualified_file_name: str)->pd.DataFrame:
        """_summary_

        Args:
            ticker (str): _description_

        Returns:
            pd.DataFrame: _description_
        """
        df = pd.read_csv(filepath_or_buffer=fully_qualified_file_name,parse_dates=True,index_col=Columns.DATE.value)
        print(f"successfully loaded ticker: {ticker} into memory")
        return df 


