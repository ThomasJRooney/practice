class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]

class Solution(object):
    def majorityElement(self, nums):
        counter_dic = {}
        for n in nums:
            if n in counter_dic:
                counter_dic[n] += 1
            else:
                counter_dic[n] = 1
        return max(counter_dic, key=counter_dic.get)
