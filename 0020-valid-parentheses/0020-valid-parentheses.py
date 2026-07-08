class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ['(','{','[']:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top == '(' and ch != ')':
                    return False
                if top == '[' and ch != ']':
                    return False
                if top == '{' and ch != '}':
                    return False
        return len(stack) == 0