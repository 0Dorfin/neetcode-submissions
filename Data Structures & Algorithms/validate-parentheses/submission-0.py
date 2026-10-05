class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dict_par = {')': '(', '}': '{', ']': '['}

        for par in s:
            if par not in dict_par:
                stack.append(par)
            else:
                if not stack:
                    return False
                else:
                    last_opened = stack.pop()
                    if last_opened != dict_par[par]:
                        return False

        if not stack:
            return True
        else:
            return False