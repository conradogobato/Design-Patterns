class BuyOperation:
    def buy():
        print('Item bought')


class Market:
    def __init__(self, products:list[str]):
        self.products = products

    def getProduct(self, index):
        print(f'{self.products[index]}')

class ShoppingFacade:
    def __init__(self, market: Market, buy_op: BuyOperation):
        self.buy = buy_op
        self.market = market

    def buy_item(self, index):
        self.market.getProduct(index)
        self.buy.buy()
