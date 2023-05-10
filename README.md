# Monte Carlo Simulation for Options Pricing

## Background - What is a Monte Carlo Simulation?
They are a way of solving probabilistic problems through simulating many scenarios 
of the given problem. Helpful for finding expected value, variance, and other numerical
summaries for complex problems. Learn more here: https://en.wikipedia.org/wiki/Monte_Carlo_method

For this project, we are simulating Financial Derivatives. Why? Options
are complex and hard to simulate using analytical formulas. This is usually done with risk-neutral
pricing (since it's easier to calculate)

### Market Value vs Theoretical Value for `MSFT`
![image](https://github.com/TimothyW553/Monte-Carlo-Options-Pricing/assets/31230953/09d944d3-6bc4-40d0-8f72-4287e391fd60)

### Market Value vs Theoretical Value for `AAPL`
![image](https://github.com/TimothyW553/Monte-Carlo-Options-Pricing/assets/31230953/e5a89849-6693-4916-851f-18a2ce25da44)

### Ways to improve accuracy
 1. Variance reduction methods:
    - Antithetic variates
    - Control variates
 2. Quasi-random variates compared to pseudo random numbers
