# ARITHMETIC OPERATORS.

echo "please enter a value: \c"
read -r a
echo "please enter b value: \c"
read -r b

echo "a + b is $(($a+$b))"
echo "a - b is $(($a-$b))"
echo "a * b is $(($a*$b))"
echo "a / b is $(($a/$b))"
echo "a % b is $(($a%$b))"

#OR

echo "a + b is `expr $a + $b`"
echo "a - b is `expr $a - $b`"
echo "a * b is `expr $a \* $b`"   # check this.
echo "a / b is `expr $a / $b`"
echo "a % b is `expr $a % $b`"

# RELATIONAL OPERATORS.

# -lt less than <
# -le less than or equal to <=
# -gt greater than >
# -ge greater than or equal to  >=
# -eq equal to =
# -ne not equal to !=

x=4
y=4

# if matches return 0 else returns 1.

test $x -lt $y; echo "$?"  # 1   # test is a keyword.
test $x -le $y; echo "$?"  # 0
test $x -gt $y; echo "$?"  # 1
test $x -ge $y; echo "$?"  # 0
test $x -eq $y; echo "$?"  # 0
test $x -ne $y; echo "$?"  # 1

# LOGICAL OPERATIORS.

# AND(-a)(&&)     OR(-o)(||)    NOT(-n)!

if test $x -ge $y -a $x -ne 0
then
echo  "x is greater than or equal to y AND x not equal 0"
fi

if test $x -ge $y -o $x -ne 0
then
echo  "x is greater than or equal to y OR x not equal 0"
fi

if [[ $x -ge 3 && $x -ne 0 ]]
then
echo  "x is greater than or equal to 3 AND x not equal 0"
fi

if [[ $x -ge 10 || $x -ne 0 ]]
then
echo  "x is greater than or equal to 10 OR x not equal 0"
fi


if [ $x -ge 3 ] && [ $x -ne 0 ]
then
echo  "x is greater than or equal to 3 AND x not equal 0"
fi