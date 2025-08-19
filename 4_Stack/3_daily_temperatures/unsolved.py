# Given a list of daily temperatures, return a list that tells for each day how many days until a warmer temperature.
class DailyTemperatures:
    def __init__(self, nums) -> None:
        self.nums = nums
    
    def daily_temperatures(self):
        count = 0
        days = []

        while self.nums:
            top = self.nums.pop()
            while len(self.nums) > 1 and top > self.nums[-1]:
                count += 1
                self.nums.pop()
            days.append(count)
            count = 0
        return days


if __name__ == "__main__":
    print(DailyTemperatures([73,74,75,71,69,72,76,73]).daily_temperatures())# [1,1,4,2,1,1,0,0]
    print(DailyTemperatures([30,40,50,60]).daily_temperatures())# [1,1,1,0]
    print(DailyTemperatures([30,60,90]).daily_temperatures()) # [1,1,0]         
