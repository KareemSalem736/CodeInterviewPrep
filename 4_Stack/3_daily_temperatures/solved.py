# Given a list of daily temperatures, return a list that tells for each day how many days until a warmer temperature.

class DailyTemperatures:
    def __init__(self, arr) -> None:
        self.arr = arr

    def daily_temperatures(self) -> list[int]:
        n = len(self.arr)
        result = [0] * n
        stack = []  # holds indices of days

        for i, temp in enumerate(self.arr):
            # If current day is warmer than the day on top of stack
            while stack and temp > self.arr[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append(i)

        return result

if __name__ == "__main__":
    print(DailyTemperatures([73,74,75,71,69,72,76,73]).daily_temperatures())# [1,1,4,2,1,1,0,0]
    print(DailyTemperatures([30,40,50,60]).daily_temperatures())# [1,1,1,0]
    print(DailyTemperatures([30,60,90]).daily_temperatures()) # [1,1,0]         
