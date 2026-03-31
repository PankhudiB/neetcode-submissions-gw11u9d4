from collections import deque;

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for item in operations:
            print(item)
            match item:
                case "C":
                    top = stack.pop()
                    sum -= int(top)
                    print(stack)
                case "D":
                    top = stack[-1]
                    stack.append(2 * top)
                    sum += (2 * top)
                    print(stack)
                case "+":
                    first = stack[-1]
                    second = stack[-2]
                    res = first + second
                    stack.append(res)
                    sum += res
                    print(stack)
                case _:
                    stack.append(int(item))
                    sum += int(item)
                    print(stack)
        return sum
            

        