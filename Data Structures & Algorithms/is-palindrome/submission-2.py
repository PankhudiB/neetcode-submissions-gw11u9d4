class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s)-1
        while first < last:
            # print("F: " + s[first] + "L: " + s[last])
            while first < last and not s[first].isalnum():
                first += 1
            while last > first and not s[last].isalnum():
                last -= 1
            # print("F: " + s[first] + "L: " + s[last])
            if s[first].lower() == s[last].lower():
                first += 1
                last -= 1
            else:
                return False
        
        return True