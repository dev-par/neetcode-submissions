class Solution:
    def isValid(self, s: str) -> bool:
        # every open bracket is closed by the same type of close bracket
        # open brackets are closed in correct order
        # close bracket has a cooresponding open bracket of the same type

        # [{[()]}]
        # iterate through it
        #when we see an opening bracket, add the cooresponding closing bracket to the stack
        # when we see a closing bracket, pop from the stack and compare, if incorrect false

        pairs = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            if char == "[":
                stack.append("]")
            elif char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            
            else:
                if stack:
                    close = stack.pop()
                    if close != char:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        return False

