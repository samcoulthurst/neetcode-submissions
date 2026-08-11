class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator

        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

        stack = []
        for i in tokens:
            if i not in ops:
                stack.append(int(i))

            if i == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))

            elif i in ops.keys():
                num2 = stack.pop()
                num1 = stack.pop()
                func = ops[i]
                value = func(num1,num2)
                stack.append(value)
        return int(stack[-1])