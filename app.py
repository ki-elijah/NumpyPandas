import yfinance as yf
import matplotlib.pyplot as plt
import seaborn



data = yf.Ticker("MSFT")

print(data.info)

hist = data.history(period="5d")
hist['Close'].plot(figsize=(16, 9))
data_df = yf.download("AAPL", start="2021-01-01", end="2021-08-01")
data_df.to_csv('aapl.csv')
