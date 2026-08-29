import matplotlib.pyplot as plt

def plot_market(market):

    domain = market.market_domain()

    if domain is None:
        print("Cannot plot an invalid market.")
        return
    
    
    price_min, price_max = domain


    prices = []
    demand_quantities = []
    supply_quantities = []


    for price in range(int(price_min), int(price_max) + 1):
        prices.append(price)
        demand_quantities.append(market.demand(price))
        supply_quantities.append(market.supply(price))

    eq_price = market.equilibrium_price()
    eq_quantity = market.equilibrium_quantity(eq_price)

    

    plt.plot(demand_quantities, prices, label="demand")
    plt.plot(supply_quantities, prices, label="supply")

    plt.scatter(eq_quantity, eq_price)   

    plt.axhline(eq_price)
    plt.axvline(eq_quantity)

    plt.xlabel("Quantity")
    plt.ylabel("Price")

    label = f"Equilibrium\nP = {eq_price}\nQ = {eq_quantity}"
    plt.annotate(label, (eq_quantity, eq_price))

    plt.title("Supply and Demand")

    plt.legend()
    plt.grid()

    plt.show()
