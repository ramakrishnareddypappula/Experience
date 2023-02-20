

# If you have $10000. You delegate to 10 person to count giving each $1000. Then inturn 10 giving each $100.
# If $10 or less then you return.

def delegate(n):
    if n <= 10:
        return n
    else:
        return 10 * delegate(n/10)

print(delegate(100000))