class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort();
        prefix = strs[0];
        if (prefix == ""):
            return prefix;        
        for s in strs[1:len(strs)]:
            if (s == ""):
                return "";
            s = s[0:len(prefix)];
            for i, char in enumerate(s):                
                if prefix[i] == char:
                    continue;
                else:
                    prefix = s[0:i];
                    break;
        return prefix;