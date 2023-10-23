import math

# check nan
def check_nan(df):
    return df.isna().any().any()
def cube(x):
    return math.sqrt(x)