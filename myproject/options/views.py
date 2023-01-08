import numpy as np
from django.shortcuts import render

def options_view(request):
    if request.method == 'POST':
        sigma = float(request.POST['sigma'])
        S = float(request.POST['S'])
        K = float(request.POST['K'])
        T = float(request.POST['T'])
        r = float(request.POST['r'])
        option_type = request.POST['option_type']
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
        # Render the pricing template and pass the option price to the template
        return render(request, 'pricing.html', {'option_price': black_scholes(S, K, T, r, sigma, option_type)})
    else:
        return render(request, 'pricing.html', {})


def pricing():
    return None