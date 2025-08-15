# Given a list of daily temperatures, return a list such that for each day tells you how many days you would have to wait until a warmer temperature.
# If there is no future day for which this is possible, put 0 instead.

def daily_temperatures(temps):
    return

if __name__ == '__main__':
    print(daily_temperatures([73,74,75,71,69,72,76,73]))  
    # [1,1,4,2,1,1,0,0]
    print(daily_temperatures([30,40,50,60]))              
    # [1,1,1,0]
    print(daily_temperatures([30,60,90]))                 
    # [1,1,0]