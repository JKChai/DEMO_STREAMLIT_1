import os
import pandas as pd

from config import SetupFactory

def get_data():
    config_obj = SetupFactory()
    rootpath = config_obj.rootpath
    df_sql = pd.read_sql_query(config_obj.query, config_obj.cnxn)
    return df_sql, rootpath

def main():
    df_sql, rootpath = get_data()
    df = pd.DataFrame(df_sql)

    fpath = os.path.join(
            rootpath
            ,".."
            ,"assets"
            ,"ContosoRetailDW_FactSales.csv")
    df.to_csv(fpath, index=False)

if __name__ == "__main__":
    main()