import numpy as np
import datetime
import matplotlib.pyplot as plt
from scipy.stats import norm
import yfinance as yf

# Create a ticker object for the stock you want to retrieve data for
ticker = yf.Ticker("MSFT")

# Retrieve historical price data
data = ticker.history(period="1mo")
options = ticker.options

info = ticker.info
S = current_price = data['Close'][0]  # stock price
yield_value = info.get('trailingAnnualDividendYield')

expiration_dates = ticker.options
expiration_date = expiration_dates[0]
options_chain = ticker.option_chain(expiration_date)
call_options = options_chain.calls

K = call_options.iloc[0]['strike']               # strike price
vol = call_options.iloc[0]['impliedVolatility']  # volatility (in %)
r = risk_free_rate = yield_value / 100           # risk-free rate (in %)
N = 10                                           # number of steps
M = 1000                                         # number of simulations

market_value = market_price = call_options.iloc[0]['lastPrice']           # market price of option
T = ((datetime.date(2023, 6, 9) - datetime.date.today()).days + 1) / 365  # time in years
print(T)

#precompute constants
dt = T/N
nudt = (r - 0.5*vol**2)*dt
volsdt = vol*np.sqrt(dt)
lnS = np.log(S)

# Monte Carlo Method
Z = np.random.normal(size=(N, M))
delta_lnSt = nudt + volsdt*Z
lnSt = lnS + np.cumsum(delta_lnSt, axis=0)
lnSt = np.concatenate((np.full(shape=(1, M), fill_value=lnS), lnSt))

# Compute Expectation and SE
ST = np.exp(lnSt)
CT = np.maximum(0, ST - K)
C0 = np.exp(-r*T)*np.sum(CT[-1])/M
sigma = np.sqrt(np.sum((CT[-1] - C0)**2) / (M-1))
SE = sigma/np.sqrt(M)
print("Call value is ${0} with SE +/- {1}".format(np.round(C0, 2), np.round(SE,2)))

# Define the confidence interval as a multiple of the standard error
confidence_interval = 1.96

# Generate the x-values for the probability distribution
x_min = C0 - confidence_interval * SE
x_max = C0 + confidence_interval * SE
x = np.linspace(x_min, x_max, 100)

# Compute the probability density function for the normal distribution
pdf = norm.pdf(x, C0, SE)

# Create the probability distribution plot
plt.plot(x, pdf, color='tab:blue', label='Probability Distribution')
plt.axvline(x=C0, color='k', linestyle='--', label='Theoretical Value')
plt.axvline(x=market_value, color='r', linestyle='--', label='Market Value')
plt.fill_between(x, pdf, where=(x > C0 + SE), color='tab:blue', alpha=0.2)
plt.fill_between(x, pdf, where=(x < C0 - SE), color='tab:blue', alpha=0.2)
plt.fill_between(x, pdf, where=((x >= C0 - SE) & (x <= C0 + SE)), color='cornflowerblue', alpha=0.5)
plt.ylabel("Probability Density")
plt.xlabel("Option Price")
plt.legend()
plt.show()

