
def birthdayCakeCandles(candles):
    maxi=candles[0]
    for i in range(1,len(candles)):
        if candles[i]>maxi: 
            maxi = candles[i]
    return candles.count(maxi)

### my other solution
def birthdayCakeCandles(candles):
    return candles.count(max(candles))