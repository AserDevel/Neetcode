class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        unique_numbers = []
        unique_numbers_counter = []
        for i in nums:
            flag = True
            for j in range(len(unique_numbers)):
                if i == unique_numbers[j]: 
                    flag = False
                    unique_numbers_counter[j] += 1
            if flag: 
                unique_numbers.append(i)
                unique_numbers_counter.append(1)
        
        K_Frequent_Numbers = []
        for i in range(k):
            index_of_most_frequent = 0
            for j in range(len(unique_numbers_counter)):
                if unique_numbers_counter[j] > unique_numbers_counter[index_of_most_frequent]:
                    index_of_most_frequent = j

            K_Frequent_Numbers.append(unique_numbers[index_of_most_frequent])
            unique_numbers.remove(unique_numbers[index_of_most_frequent])
            unique_numbers_counter.remove(unique_numbers_counter[index_of_most_frequent])
        
        print(K_Frequent_Numbers)
        return K_Frequent_Numbers 
    
#test
nums = [3,1,2,2,3,3,3]
k = 2
Solution.topKFrequent(0, nums, k)