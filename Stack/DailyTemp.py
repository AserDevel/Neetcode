class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = []
        for i in range(len(temperatures)):
            daycount = 0
            result.append(daycount)
            for j in range(i, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    result[i] = daycount
                    break
                daycount += 1
        
        return result