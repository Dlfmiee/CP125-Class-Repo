def compare_prices(store_a, store_b):
    only_a = []
    a_cheaper = []
    b_cheaper = []

    if not store_a:
        return {"only_a": [], "a_cheaper": [], "b_cheaper": []}

    for item, price_a in store_a.items():
        if item not in store_b:
            only_a.append(item)
            
        else:
            price_b = store_b[item]
            if price_a < price_b:
                a_cheaper.append(item)
                
            elif price_a > price_b:
                b_cheaper.append(item)

    return {
        "only_a": sorted(only_a),
        "a_cheaper": sorted(a_cheaper),
        "b_cheaper": sorted(b_cheaper),
    }



store_a = {"milk": 3.50, "bread": 2.00, "eggs": 5.00, "butter": 4.50}
store_b = {"milk": 3.00, "bread": 2.50, "eggs": 5.00, "coffee": 8.00}
result = compare_prices(store_a, store_b)
print(result["only_a"])
print(result["a_cheaper"])
print(result["b_cheaper"])
