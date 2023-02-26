
# variables start with alphabets and not numbers.
# spaces, special characters, - are not allowed.


A=10
HOSTNAME=$(hostname)
DATE=`date`
#1var=1     # error
#false@f=false # error
#hpen-a=20   # error

echo $A
echo $HOSTNAME
echo $DATE

#Datatypes

name="john" # strings
age=30 # integers
f=3.2   # float
fruits=("apple" "banana")   # arrays
echo ${fruits[1]}     # banana
echo ${fruits[@]}     # apple banana

declare -a colors    # associative arrays
colors["red"]="AAA"
colors["blue"]="BBB"
colors["green"]="CCC"
echo ${colors["green"]}       # CCC



# special variables $*, $#, $1, $2, $0, "$@", $?, $$, $!

# $* = stores complete positional arguments into 1 string.
# $# = number of arguments count.
# $1 = first argument
# $2 = second argument
# $0 = name of executed command
# "$@" = each quoted string is treated as separate argument.
# $? = exit status of last command.
# $$ = PID of current shell
# $! = PID of last background job.

echo "output of "'$* '"is $*"
echo "output of "'$# '"is $#"
echo "output of "'$1 '"is $1"
echo "output of "'$2 '"is $2"
echo "output of "'$0 '"is $0"
echo "output of "'$@ '"is $@"       # $* vs $@ difference below.
echo "output of "'$? '"is $?"       # example below
echo "output of "'$$ '"is $$"       # PID of shell
sleep 4 &
echo "output of "'$! '"is $!"       # PID of last background job.

#===================================
echo "Using \$@:"
for arg in "$@"; do
  echo "$arg"
done
# $1
# $2

echo "Using \$*:"
for arg in "$*"; do
  echo "$arg"
done

# $1 $2

#====================================
# $?
# exit status is a numeric value between 0 and 255 that indicates whether the command completed successfully
# (exit status 0) or encountered an error (non-zero exit status).


ls /non
echo "$?" # 1
ls
echo "$?" # 0
