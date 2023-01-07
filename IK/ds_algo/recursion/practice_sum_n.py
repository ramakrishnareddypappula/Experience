


def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)

print(sum_n(10)) # 10 + 9 +8+ 7 +6+ 5 +4+ 3+ 2 + 1


def multiply(n):
    if n == 1:
        return 1
    else:
        return n * multiply(n - 1)

print(multiply(4))

print("-------")
def string_a(n, str1, result):
    if len(str1) == n:
        result.append(str1)
        return

    else:
        x =  string_a(n, str1 + "a", result)
        y = string_a(n, str1 + "b", result)
        z = string_a(n, str1 + "c", result)
    return result

print(string_a(2, "", []))



def helper(s, i, result):
    if len(s) == i:
        result.append("".join(s[:]))
        return
    else:
        for j in range(i, len(s)):
            s[i], s[j] = s[j], s[i]
            helper(s, i + 1, result)
            s[i], s[j] = s[j], s[i]
    return result

def string_b(s):
    return helper(s, 0, [])

print(string_b(["a", "b", "c"]))
print(string_b(["a", "b"]))


