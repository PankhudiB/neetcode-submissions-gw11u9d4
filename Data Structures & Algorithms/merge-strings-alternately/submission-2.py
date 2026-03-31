class Solution:
    # def mergeAlternately(self, word1: str, word2: str) -> str:                
    #     i = 0
    #     j = 0
    #     merged = []
    #     while i < len(word1) and j < len(word2):
    #         merged.append(word1[i])
    #         merged.append(word2[j])
    #         i += 1
    #         j += 1

    #     merged.append(word1[i:])
    #     merged.append(word2[j:])
    #     return "".join(merged)
    def mergeAlternately(self, word1: str, word2: str) -> str:                
        i = 0
        j = 0
        merged = []
        n1 = len(word1)
        n2 = len(word2)        
        while i < n1 or j < n2:
            if i < n1:
                merged.append(word1[i])
                i += 1
            if j < n2:
                merged.append(word2[j])
                j += 1

        return "".join(merged)
        