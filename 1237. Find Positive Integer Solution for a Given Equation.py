"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # ret = []
        # x, y = 1, z
        # while x <= z and y >= 1:
        #     temp = customfunction.f(x, y)
        #     if temp < z:
        #         x += 1
        #     elif temp > z:
        #         y -= 1
        #     else:
        #         ret.extend([[x, y]])
        #         x += 1
        #         y -= 1
        # return ret
        y,g = z,customfunction.f
        for x in range(1, z+1):
            while y:
                d = g(x,y) - z
                if d <= 0:
                    if not d:
                        yield [x,y]
                    break
                y -= 1
