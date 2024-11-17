import pandas as pd

def risk_ratio(df, categorical):
    for col in categorical:
        global_mean = df.churn.mean()
        df_group =df.groupby(col).churn.agg(['mean'])
        df_group['diff'] = df_group['mean'] - global_mean
        df_group['rate'] = df_group['mean'] / global_mean
        display(df_group)