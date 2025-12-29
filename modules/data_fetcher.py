import yfinance as yf
import pandas as pd
import config

def fetch_stock_data(ticker: str, period: str = "3mo", interval: str = "1d") -> pd.DataFrame:
  try:
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)

    if df.empty:
      print(f"No data was found for {ticker}.")
      return pd.DataFrame()
    
    columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    df = df[columns]

    df = df.dropna()

    return df
  
  except Exception as e:
    print(f"Error fetching data for {ticker}: {e}")
    return pd.DataFrame()
  
def latest_price(ticker: str) -> float:
  df = fetch_stock_data(ticker, period="1d", interval="1d")

  if df.empty:
    return None
  
  return round(df['Close'].iloc[-1], 2)

if __name__ == "__main__":

  print("Testing Module")

  testing_ticker = "AAPL"

  df = fetch_stock_data(testing_ticker, period="1mo", interval="1d")
  print(df.head())
  if not df.empty:
    price = latest_price(testing_ticker)
    print(f"Current price of {testing_ticker} is ${price}.")
  