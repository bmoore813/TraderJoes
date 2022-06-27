import sys

sys.path.append('/Users/bmoore/github.com/bmoore813/TraderJoes')

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from src.app.data.data.db import DataBase, Columns
from datetime import date, timedelta







def run()->None:
    """_summary_
    """
    num_days = 200
    start_date = date.today() - timedelta(num_days)
    df = DataBase.get_data('tqqq',start_date=start_date, end_date=date.today())

    log_return = 'LogReturn'
    df[log_return] = np.log(df[Columns.CLOSE.value]).diff().shift(-1)
    print(df.head())






if __name__ == '__main__':
    run()