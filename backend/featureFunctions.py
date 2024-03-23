
import matplotlib.pyplot as plt
class FeatureFunctions:
  def __init__(self, prices):
      self.prices = prices
    
    
  def calculate_rsi(self,period=14):
    delta = self.prices.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.ewm(com=period - 1, min_periods=period).mean()
    avg_loss = loss.ewm(com=period - 1, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


  def calculateSMA(self, period=20):
    return self.prices.rolling(window=period).mean()

  def calculateEMA(self, period):
    return self.prices.ewm(span=period, adjust=False).mean()

  def calculateMACD(self, period1=12, period2=26):
    ema1 = self.calculateEMA( period1)
    ema2 = self.calculateEMA( period2)
    return ema1 - ema2

  def calculateBollingerBands(self, period=20):
    upperband = self.calculateSMA(period) + 2 * self.prices.rolling(window=period).std()
    lowerband = self.calculateSMA(period) - 2 * self.prices.rolling(window=period).std()  
   # middleband = self.calculateSMA( period)

    #return upperband, middleband, lowerband
    return upperband-lowerband

  def plotFeatures(self, bollingerBandsls=[],MACD=[],SMA=[],rsi=[]):
    fig,ax = plt.subplots()
    ax.plot(self.prices.index, self.prices, label='Price')
    if len(bollingerBandsls) > 0:
        ax.plot(self.prices.index, bollingerBandsls[0], label='Upper Band')
        ax.plot(self.prices.index, bollingerBandsls[1], label='Middle Band')
        ax.plot(self.prices.index, bollingerBandsls[2], label='Lower Band')
    if len(MACD) > 0:
        ax.plot(self.prices.index, MACD, label='MACD')
    if len(SMA) > 0:
        ax.plot(self.prices.index, SMA, label='SMA')
    if len(rsi) > 0:
        ax.plot(self.prices.index, rsi, label='RSI')
    ax.set_title('Bollinger Bands, MACD, SMA, RSI')
    ax.legend()
    plt.show()
    