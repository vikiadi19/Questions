class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a, b = 0, len(numbers)-1
        while b>a:
            summ = numbers[a]+numbers[b]
            if summ > target:
                b-=1
            elif summ < target:
                a+=1
            else:
                return [a+1,b+1]