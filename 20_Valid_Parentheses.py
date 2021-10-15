class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        output = []
        if not s:
            return s
        for each in s:
            if each == '(' or each == '[' or each == '{':
                output.append(each)
            else:
                if each == ')':
                    if not output:
                        return False
                    current = output.pop()
                    if current != '(':
                        return False
                if each == ']':
                    if not output:
                        return False
                    current = output.pop()
                    if current != '[':
                        return False
                if each == '}':
                    if not output:
                        return False
                    current = output.pop()
                    if current != '{':
                        return False
        if output:
            return False
        return True
