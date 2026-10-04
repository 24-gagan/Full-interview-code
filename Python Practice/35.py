def apply_discount(prices,thershold=50,discount=10):
    discounted_prices=[]
    for price in prices:
        if price>=thershold:
            price-=price*(discount/100)
        discounted_prices.append(price)
    return discounted_prices
print(apply_discount([60,30,80]))
print(apply_discount([60,30,80],thershold=40,discount=20))