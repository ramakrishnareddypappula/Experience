x=4
y=3

if [ $x -gt $y ]
then
echo "$x is greater than $y"
elif [ $x -lt $y ]
then
echo "$x is less than $y"
else
echo "$x is equal to $y"
fi

touch ./test{1..100}.txt   # this will create test1.txt, test2.txt .... test100.txt


