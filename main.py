from market import Market
from visualization import plot_market

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")    

a = get_number("Enter demand intercept (a):")
b = get_number("Enter demand slope (b):")
c = get_number("Enter supply intercept (c):")
d = get_number("Enter supply slope (d)")


market = Market(a, b, c, d)

plot_market(market)