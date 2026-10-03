class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def timeTaken (pos,speed):
            tt = (target-pos)/speed
            return tt
        cars = []
        for i in range(len(position)):
            car = [position[i],timeTaken(position[i],speed[i])]
            cars.append(car)
        cars.sort()
        stack = []
        for car in cars:
            while stack and stack[-1][1] <= car[1]:
                stack.pop()
            stack.append(car)
        return len(stack)