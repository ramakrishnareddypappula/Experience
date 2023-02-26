
opt=y
while [ $opt = y -o $opt = Y ]
do
echo "enter a number: \c"
read -r num
echo "square of number is = $(($num*$num))"
echo "Do you wish to continue [y/n]: \c"
read -r wish
if [ $wish = y -o $wish = Y ]
then
continue
else
echo "program is exiting..."
exit
fi
done