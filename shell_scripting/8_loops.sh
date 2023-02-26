
# WHILE LOOP


echo "Enter a number: \c"
read -r c
i=1
while [ $i -le 10 ]
do
#b=`expr $c \* $i`
b=$(($c*$i))  # both work fine.
echo "$c * $i = $b"
i=`expr $i + 1`
done

echo "##############"

max=10
for (( i=1; i <= $max; i++ ))
do
b=$(($c*$i))  # both work fine.
echo "$c * $i = $b"
done

echo "##############"


max=10
for i in `seq 1 $max`
do
b=$(($c*$i))  # both work fine.
echo "$c * $i = $b"
done


echo "##############"

list=(1 2 3 4 5)
for i in "${list[@]}"
do
echo "$i"
done


echo "##############"

names=("127.0.0.1" "8.8.8.8" "256.2.1.2" "255.255.255.255")
for i in "${names[@]}"
do
ping -c 1 $i > /dev/null 2>&1
valid=`echo $?`
if [ $valid -eq 0 ]
then
echo "$i host is up"
else
echo "$i host unreachable"
fi
done

echo "##############"
# UNTIL LOOP

echo "Enter an ip: \c"
read -r ip
until ping -c 3 $ip
do
echo "Host $ip is still down"
sleep 1
done

echo "host $ip is up"