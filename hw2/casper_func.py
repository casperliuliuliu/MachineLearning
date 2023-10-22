

# check nan
def check_nan(df):
    return df.isna().any().any()