# Monte Carlo Simulation for Options Pricing

## Background - What is a Monte Carlo Simulation?
They are a way of solving probabilistic problems through simulating many scenarios 
of the given problem. Helpful for finding expected value, variance, and other numerical
summaries for complex problems. Learn more here: https://en.wikipedia.org/wiki/Monte_Carlo_method

For this project, we are simulating Financial Derivatives. Why? Options
are complex and hard to simulate using analytical formulas. This is usually done with risk-neutral
pricing (since it's easier to calculate)

Compared to a deterministic model (such as the Black-Scholes options pricing model for European 
call options), the Monte Carlo is inefficient. We can improve its accuracy by using:
 1. Variance reduction methods:
    - Antithetic variates
    - Control variates
 2. Quasi-random variates compared to pseudo random numbers