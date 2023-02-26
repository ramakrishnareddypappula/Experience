
a=10
b=2
echo "number 1 is $a"
echo "number 2 is $b"

echo "1. sum"
echo "2. subtraction"
echo "3. multiplication"
echo "4. division"
echo "enter a number: \c"
read -r ch

case $ch in
1) echo "sum of $a + $b = $(($a+$b))";;
2) echo "subtraction of $a - $b = $(($a-$b))";;
3) echo "product of $a * $b = $(($a*$b))";;
4) echo "division of $a / $b = $(($a/$b))";;
*) echo "invalid number";;
esac
