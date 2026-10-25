class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for char in s:
            if char in "[({":
                stack.append(char)
            elif char == "]":
                if len(stack)==0:
                    return False
                if stack[-1] =="[" :
                    stack.pop()
                else:
                    stack.append(char)
            elif char == ")":
                if len(stack)==0:
                    return False
                if stack[-1] =="(":
                    stack.pop()
                else:
                    stack.append(char)
            elif char == "}":
                if len(stack)==0:
                    return False
                if stack[-1] =="{":
                    stack.pop()
                else:
                    stack.append(char)
        print(stack)
        return len(stack)==0