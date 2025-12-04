import pandas as pd
from utils import csv_file
from utils import Replacing_existing_columns
from utils import Replacing_existing_column
from utils import Replacing_existing_column_2
from utils import Create_new_column_1
from utils import Create_and_sort
from utils import Create_new_column_2
from utils import Delete_rows
from utils import create_with_lambda

if __name__ == '__main__':


    df = csv_file()
    df = Replacing_existing_columns(df)
    df = Replacing_existing_column_2(df)
    df = Replacing_existing_column(df)
    df = Create_new_column_1(df)
    df = Create_and_sort(df)
    df = Create_new_column_2(df)
    df = create_with_lambda(df)
    df = Delete_rows(df)
    print(df)
    df.to_csv('clean_orders_[ID_NUMBER].csv')


