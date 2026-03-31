class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for asteroid in asteroids:
            while stack and (stack[-1] > 0 and asteroid < 0):
                top = stack[-1]
                if self.areOppositeMoving(top, asteroid):                    
                    if abs(top) == abs(asteroid):
                        stack.pop()
                        asteroid = 0
                    if abs(top) > abs(asteroid):
                        asteroid = 0
                    elif abs(top) < abs(asteroid):
                        stack.pop()
                else:
                    stack.append(asteroid)
            if asteroid != 0:
                stack.append(asteroid)
        
        return list(stack)

    def areOppositeMoving(self, a1, a2):
        if a1 > 0 and a2 < 0: return True
        return False