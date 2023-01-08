import numpy as np

# Calculate the option price using the Black-Scholes model
def black_scholes(S, K, T, r, sigma, option_type):
    from scipy.stats import norm
    T = T / 12  # Convert time to expiration to months
    d1 = (np.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == "call":
        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

# Prompt the user to enter the values for the Black-Scholes model
S = float(input("Enter the spot price of the underlying asset: "))
K = float(input("Enter the strike price of the option: "))
T = float(input("Enter the time to expiration of the option (in months): "))
r = float(input("Enter the risk-free interest rate: "))
sigma = float(input("Enter the volatility of the underlying asset: "))
option_type = input("Enter the option type (call or put): ")

# Calculate the option price
option_price = black_scholes(S, K, T, r, sigma, option_type)

# Print the option price
print("Option price:", option_price)
