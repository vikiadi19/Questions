class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        one = 1
        for i in range(32):
            # one = one<<i
            x = (n>>i) & 1
            # x = n&one
            x = x<<(31-i)
            ans = ans|x
            
        return ans