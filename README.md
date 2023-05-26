# Monte Carlo Simulation for Options Pricing

## Background - What is a Monte Carlo Simulation?
They are a way of solving probabilistic problems through simulating many scenarios 
of the given problem. Helpful for finding expected value, variance, and other numerical
summaries for complex problems. Learn more here: https://en.wikipedia.org/wiki/Monte_Carlo_method

For this project, we are simulating Financial Derivatives. Why? Options
are complex and hard to simulate using analytical formulas. This is usually done with risk-neutral
pricing (since it's easier to calculate)

### Market Value vs Theoretical Value for `MSFT`
![image](https://github.com/TimothyW553/Monte-Carlo-Options-Pricing/assets/31230953/0d95da53-bbad-46d6-92c0-da8a60124232)

### Market Value vs Theoretical Value for `AAPL`
![image](https://github.com/TimothyW553/Monte-Carlo-Options-Pricing/assets/31230953/2974c362-7853-4b50-b42c-aa166436125c) 

### Ways to improve accuracy
 1. Variance reduction methods:
    - Antithetic variates
    - Control variates
 2. Quasi-random variates compared to pseudo random numbers
