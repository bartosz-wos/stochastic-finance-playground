import yfinance as yf
import numpy as np
import pandas as pd

def con_kelly(ticker='BTC-USD', risk_free=0.05, trading_days=365):
    data = yf.download(ticker, period="5y", progress=False)
    
    if data.empty:
        return

    close_prices = data['Close'][ticker]

    log_returns = np.log(close_prices / close_prices.shift(1)).dropna()
    
    daily_var = float((log_returns ** 2).mean())
    annual_var = daily_var * trading_days
    annual_volatility = np.sqrt(annual_var)
    
    daily_log_mean = float(log_returns.mean())
    annual_log_mean = daily_log_mean * trading_days
    annual_mu = annual_log_mean + (annual_var / 2)
    
    kelly_fraction = (annual_mu - risk_free) / annual_var
    half_kelly = kelly_fraction / 2
    
    print(ticker)
    print(f"expected return {annual_mu*100}%")
    print(annual_volatility)
    print()
    print(kelly_fraction)
    print(half_kelly)

con_kelly()
