
while getopts :a:b: options
do
case $options in
a) opt_a=$OPTARG;;
b) opt_b=$OPTARG;;
?) echo "I dont know what $OPTARG is"
esac
done
echo "option A = $opt_a and option B = $opt_b"

# sh 13_get_options.sh -a 10 -b 20 -c 20
# I dont know what c is
# option A = 10 and option B = 20
