class Market:
    def __init__(self,a,b,c,d):
        self.a = a      # Demand intercept
        self.b = b      # Demand slope
        self.c = c      # Supply intercept
        self.d = d      # Supply slope

    def demand(self, price):
        return self.a - self.b * price
    
    def supply(self, price):
        return self.c + self.d * price
    
    def validation(self):
        errors = []

        if self.a <= 0:
            errors.append("a must be greater than 0")

        if self.b <= 0:
            errors.append("b must be greater than 0")   

        if self.d <= 0:
            errors.append("d must be greater than 0")

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }    
    
    def demand_domain(self):
        p_max = self.a / self.b
        p_min = 0
        return(p_min ,p_max)

    def supply_domain(self):
        p_min = max(0, -self.c / self.d)
        p_max = float("inf")
        return (p_min, p_max)

    def market_domain(self):
        demand_min, demand_max = self.demand_domain()
        supply_min, supply_max = self.supply_domain()

        market_min = max(demand_min, supply_min)
        market_max = min(demand_max, supply_max)

        if market_min > market_max:
            return None

        return(market_min, market_max)

    def equilibrium_price(self):
        domain = self.market_domain()

        if domain is None:
            return None

        eq_price = (self.a - self.c) / (self.b + self.d)

        if domain[0] <= eq_price <= domain[1]:
            return eq_price

        return None

    def equilibrium_quantity(self, price):
        if price is None:
            return None

        return self.demand(price)

    def analyze(self):
        validation = self.validation()

        if not validation["valid"]:
            return self.failure(validation["errors"])

        domain = self.market_domain()

        if domain is None:
           return self.failure(
               ["No valid economic price range exists."]
           )
        
        price = self.equilibrium_price()

        if price is None:
            return self.failure(
                ["No valid economic equilibrium exists."]
            )

        quantity = self.equilibrium_quantity(price)

        return self.success({
            "price": price,
            "quantity": quantity,
            "domain": domain
        })

    def analyze_price(self, price):
        validation = self.validation()

        if not validation["valid"]:
            return self.failure(validation["errors"])

        
        domain = self.market_domain()

        if domain is None:
           return self.failure(
               ["No valid economic price range exists"]
           )

        if not domain[0] <= price <= domain[1]:
            return self.failure(
                ["Price is outside the valid economic domain."]
            )

        demand = self.demand(price)
        supply = self.supply(price)

        equilibrium_price = self.equilibrium_price()
        price_difference = price - equilibrium_price

        if demand > supply :
            condition = "shortage"
            difference = demand - supply

        elif demand == supply :
            condition = "equilibrium"
            difference = 0

        else:
            condition = "surplus"
            difference = supply - demand


        return self.success({
            "price": price,
            "equilibrium_price": equilibrium_price,
            "price_difference": price_difference,
            "demand": demand,
            "supply": supply,
            "condition": condition,
            "difference": difference
        })

    def success(self, data):
        return {
            "status": "valid",
            "errors": [],
            "data": data
        }

    def failure(self, errors):
        return {
            "status": "invalid",
            "errors": errors ,
            "data": None
        }

