# Given a list of daily temperatures, return a list that tells for each day how many days until a warmer temperature.


if __name__ == "__main__":
    print(DailyTemperatures([73,74,75,71,69,72,76,73]).daily_temperatures())# [1,1,4,2,1,1,0,0]
    print(DailyTemperatures([30,40,50,60]).daily_temperatures())# [1,1,1,0]
    print(DailyTemperatures([30,60,90]).daily_temperatures()) # [1,1,0]         
