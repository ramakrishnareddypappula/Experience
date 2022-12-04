
def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    """
    cur = ""
    stack = []
    for each in path + "/": # if "/abc/.." is given, inorder to check .., we need to add "/" in the end so that it goes into if condition.
        if each == "/":
            if cur == "..":
                if stack: stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
            cur = ""
        else:
            cur = cur + each
    return "/" + "/".join(stack)

print(simplifyPath("/a//b////c/d//././/.."))