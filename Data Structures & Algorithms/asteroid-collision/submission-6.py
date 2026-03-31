class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        stack.append(asteroids[0])

        for asteroid in asteroids[1:]:
            # print(stack)
            while stack and (stack[-1] > 0 and asteroid < 0):
                top = stack[-1]
                # print("top: ", top, "A:", asteroid)
                if self.areOppositeMoving(top, asteroid):                    
                    if abs(top) == abs(asteroid):
                        stack.pop()
                        asteroid = 0
                        # print(stack)
                    if abs(top) > abs(asteroid):
                        asteroid = 0
                    elif abs(top) < abs(asteroid):
                        stack.pop()
                        # stack.append(asteroid)
                        # print(stack)
                else:
                    stack.append(asteroid)
            if asteroid != 0:
                stack.append(asteroid)
        
        return list(stack)

    def areOppositeMoving(self, a1, a2):
        if a1 > 0 and a2 < 0: return True
        return False