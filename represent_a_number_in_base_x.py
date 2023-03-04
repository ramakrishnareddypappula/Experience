


def base_x(n, x):
    map = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    # if base 32, map should contain 32 keys etc.
    # OR we can have string = "0123456789ABCDEF" -> each index will give you that value.
    currval = n
    output = ""
    while currval >= x: # 23
        quotient = currval // x
        remainder = currval % x
        # map remainder to digit in base x and append it to growing list of digits.
        output =  map[remainder] + output
        currval = quotient

    output = map[currval] + output
    return output

print(base_x(22, 16))
print(base_x(32, 16))
print(base_x(29, 16))