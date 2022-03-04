from numba.experimental import jitclass

@jitclass
class Trader:
  def __init__(
    self,
    funds: float = 100,
    buyFee: float = 0.001,
    sellFee: float = 0.001,
  ):
    self.initFunds = funds
    self.buyFee = buyFee
    self.sellFee = sellFee
    self.reset()
  
  initFunds: float
  funds: float
  fundsDebt: float
  assets: float
  assetsDebt: float
  buyFee: float
  sellFee: float
  
  def reset(self):
    self.funds = self.initFunds
    self.fundsDebt = 0
    self.assets = 0
    self.assetsDebt = 0

