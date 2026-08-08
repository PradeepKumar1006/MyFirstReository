class Solution:
    def isValid(self, p: str) -> bool:
        s = []
        for ch in p:
            if ch in ['(','{','[']:
                s.append(ch)
            else:
                if len(s) == 0:
                    return False
                top = s.pop()
                if top == '(' and ch != ')':
                    return False
                if top == '[' and ch != ']':
                    return False
                if top == '{' and ch != '}':
                    return False
        return len(s)==0