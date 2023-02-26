
# set without arguments displays list of shell options and current values.
# shell options determine behaviour of shell interpreter.

set # displays shell options.

#set -x  # prints the command before executing it. used for debugging

ls # ls is first printed then its output is printed.
set -e

set a b c
echo "first argument : $1" # a
echo "second argument : $2" # b
echo "third argument : $3" # c
echo "third argument : $0" # file name.

set `date`

echo "today : $1"
echo "month : $2"


echo "############"
# shift

set `date`
echo "$1 $2 $3 $4 $5"
shift
echo "$1 $2 $3 $4 $5"
shift 2
echo "$1 $2 $3 $4 $5"