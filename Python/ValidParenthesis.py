class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        # iterate over the string
        for c in s:
            # if it is not a closure append and go to next character
            if c not in Map:
                stack.append(c)
                continue
            # if the stack is not empty and the last item is not the sibling 
            if not stack or stack[-1] != Map[c]:
                return False
            # then the pair is valid
            stack.pop()

        return not stack