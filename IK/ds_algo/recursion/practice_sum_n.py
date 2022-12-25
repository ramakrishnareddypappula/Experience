


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
def string_a(n, str1):
    if len(str1) == n:
        print(str1)
    else:
        x =  string_a(n, str1 + "a")
       # print("x:", x)
        y = string_a(n, str1 + "b")
       # print("y:", y)
        z = string_a(n, str1 + "c")
       # print("z:", z)

string_a(2, "")