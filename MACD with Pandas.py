import pandas as pd

def macd_12_26_9 (file_path):
    df = pd.read_csv (file_path)
    exp1 = df.ewm (span= 26, adjust=False) ['Close'].mean ()
    exp2 = df.ewm (span= 12, adjust=False) ['Close'].mean ()
    macd = exp2 - exp1
    df ['MACD'] = macd
    signal = df.ewm (span= 9 , adjust=False) ['MACD'].mean ()
    df ['Signal'] = signal
    histogram = macd - signal
    df ['Histogram'] = histogram
    return df

file_Path = 'E:/TSE Data/LatinSymbol/SBZZ1-a.csv'
df = macd_12_26_9 (file_Path)
df.to_csv ('sabzevarMACDpandas.csv', index=False)