import operator, functools
class Solution:
    def parseBoolExpr(self, expression: str, op=None) -> bool:
        groups = []
        level = 0
        
        pre = op
        for i, c in enumerate(expression):
            if c == '(':
                if level == 0:
                    start = i + 1
                level += 1
            elif c == ')':
                level -= 1
                if level == 0:
                    groups.append(self.parseBoolExpr(expression[start:i], op))
                    op = pre
            elif c == ',':
                continue
            elif level == 0:
                if c == '&':
                    op = operator.__and__
                elif c == '|':
                    op = operator.__or__
                elif c == '!':
                    op = operator.__not__
                elif c == 't':
                    groups.append(True)
                else:
                    groups.append(False)
        
        if op == None and groups:
            return groups[0]
        if op == operator.__not__:
            return not groups[0]
        return functools.reduce(op, groups)

val=Solution()
s1=input()
print(val.parseBoolExpr(s1))
