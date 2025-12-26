import yfinance as yf

ticker = yf.Ticker("AAPL")
df = ticker.history(period="5d")

columns = ['Open', 'High', 'Low', 'Close', 'Volume']
df = df[columns]
print(df.head())