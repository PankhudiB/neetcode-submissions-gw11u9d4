class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs.sort();
        # prefix = strs[0];
        # if (prefix == ""):
        #     return prefix;        
        # for s in strs[1:len(strs)]:
        #     if (s == ""):
        #         return "";
        #     s = s[0:len(prefix)];
        #     for i, char in enumerate(s):                
        #         if prefix[i] != char:
        #             prefix = s[0:i];
        #             break;
        # return prefix;
        prefix = strs[0];
        for curr in strs[1:len(strs)]:
            min_length = min(len(curr), len(prefix));
            i = 0;
            while(i < min_length):
                if prefix[i] == curr[i]:
                    i += 1;
                else:
                    break;
            prefix = prefix[0:i];
        return prefix;

                
