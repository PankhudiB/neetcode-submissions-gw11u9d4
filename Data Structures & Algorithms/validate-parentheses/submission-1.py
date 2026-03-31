class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        stack.append(s[0])

        for bracket in s[1:]:
            print(stack)
            if len(stack) != 0 and self.areComplimentary(stack[-1], bracket):
                stack.pop()
                print(stack)                
            else:
                stack.append(bracket)
                print(stack)

        return len(stack) == 0

    def areComplimentary(self, str1, str2):
        if str1 == "{" and str2 == "}": return True
        if str1 == "[" and str2 == "]": return True
        if str1 == "(" and str2 == ")": return True
        return False