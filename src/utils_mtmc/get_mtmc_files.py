from pathlib import Path
import pandas as pd


def get_etappen(year, selected_columns=None):
    if year == 2021:
        with open(Path('../data/input/mtmc/etappen_20221004.csv'), 'r', encoding='latin1') as etappen_file:
            df_etappen = pd.read_csv(etappen_file,
                                     sep=';',
                                     dtype={'HHNR': int,
                                            'W_AGGLO_GROESSE2012': int},
                                     usecols=selected_columns)
    else:
        raise Exception("Cannot get data for other years than 2010 and 2015! (etappen)")
    return df_etappen
