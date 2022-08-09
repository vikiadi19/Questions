class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TC - O(len(strs)*len(string)*26)
        # SC - O(nm)
#         ans = defaultdict(list)
#         for i in strs:
#             count = [0]*26
#             for c in i:
#                 count[ord(c)-ord("a")] += 1
                
#             ans[tuple(count)].append(i)
            
#         return ans.values()
                
        
        
        
    #sol1 - we create a list 26 characters long(len of alphabets)
    #       and a default dict of list as ans
    #       we loop each word and inside each word we loop the character and based on its 
    #       ord value - ord value of a we assign the value at particular index in list
    #       we use this list as key for dictionary and append any word that has the same key
    #       we cannot have list as key in dictionary therefore we convert it into tuple first
    #       we return the values.
    #   TC-0(n*k), SC-0(n*k)
    
    #sol2 - use sort to use sorted word as key for dictionary
    #       
        # for i in range(len(strs)):
        d = {}
        
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-ord('a')] += 1
            if tuple(count) not in d:
                d[tuple(count)] = [i]
            else:
                d[tuple(count)].append(i)
                
        # print(d)
        return d.values()

    
                
        