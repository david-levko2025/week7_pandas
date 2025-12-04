import pandas as pd
import numpy as np
import re


print("THE CSV FILE")
def csv_file():
    df_read = pd.read_json('orders_simple.json')
    return df_read

print("=" * 60)
print("=" * 25,"STEP 1","=" * 20)
print(" "* 15,"Replacing existing columns")
print("=" * 60)

def Replacing_existing_columns(df):
    df['total_amount'] = df['total_amount'].str.replace("$","0").astype(float)
    df['shipping_days'] = df['shipping_days'].astype(int)
    df['customer_age'] = df['customer_age'].astype(int)
    df['rating'] = df['rating'].astype(float)
    df['order_date'] = pd.to_datetime(df['order_date'])
    return df


print("=" * 60)
print("=" * 25,"STEP 2","=" * 20)
print(" "* 15,"Replacing existing column")
print("=" * 60)

def Replacing_existing_column(df):
    df["items_html"] = df["items_html"].str.replace(r'<[^<>]*>','',regex= True)
    return df

print("=" * 60)
print("=" * 25,"STEP 3","=" * 20)
print(" "* 15,"Replacing existing columns")
print("=" * 60)

def Replacing_existing_column_2(df):
    df['coupon_used'] = df['coupon_used'].replace("","no cupon")
    return df

print("=" * 60)
print("=" * 25,"STEP 4","=" * 20)
print(" "* 8,"Create a new columns in the end of a table")
print("=" * 60)

def Create_new_column_1(df):                                                                               
    df["order_month"] = df["order_date"].dt.month
    return df

print("=" * 60)
print("=" * 25,"STEP 5","=" * 20)
print(" "* 10,"Create a new columns and sort")
print("=" * 60)

def Create_and_sort(df):
    filtur = df["total_amount"].mean()
    df['high_value_order'] = df["total_amount"] > filtur
    return df


print("=" * 60)
print("=" * 25,"STEP 6","=" * 20)
print(" "* 15,"Create a new columns")
print("=" * 60)

def Create_new_column_2(df): 
    df.assign(rating_by_country = df.groupby("country")["rating"].transform("mean"))
    return df

print("=" * 60)
print("=" * 25,"STEP 7","=" * 20)
print(" "* 15,"Delete rows wuth filter")
print("=" * 60)

def Delete_rows(df):
    df = df[(df['rating'] > 4.5 ) & (df['total_amount'] > 1000)]
    return df

print("=" * 60)
print("=" * 25,"STEP 8","=" * 20)
print(" "* 15,"Create a new columns")
print("=" * 60)

def create_with_lambda(df):
    df['delivery_status'] = df['shipping_days'].apply(lambda x :"delayed" if x > 7 else "on time")
    return df