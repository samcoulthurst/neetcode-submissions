class Solution:
    def isValid(self, s: str) -> bool:

        close_to_open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        stack = []
        for brack in s:
            #print(brack)
            if brack in close_to_open.keys():
                # closing bracket
                if not stack:
                    return False
                top = stack.pop()
                if close_to_open[brack] != top:
                    return False
            else:
                # open bracket
                stack.append(brack)


        if stack:
            return False

        return True     