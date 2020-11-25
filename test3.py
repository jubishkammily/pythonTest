from coin import Coin

coin1 = Coin(rare = True)
coin2 = Coin()

print(coin1.color)

coin1.rust()

print(coin1.color)
print(coin2.color)