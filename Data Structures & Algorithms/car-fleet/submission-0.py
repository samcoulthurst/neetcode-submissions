class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        car_sorted = sorted(zip(position, speed), key=lambda pair: pair[0], reverse=True)

        for pos, speed in car_sorted:
            time = (target - pos )/ speed
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

