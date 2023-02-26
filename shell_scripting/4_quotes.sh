
var='abc'

# "" double quotes
# variables inside "" are expanded to values.
echo "my name is $var"  # my name is abc

echo "date is `date`"      # expanded
echo "date is $(date)"     # both outputs are same.




# '' single codes
# variables inside '' are NOT expanded to values.
echo 'my name is $var'  # my name is $var

echo 'date is `date`'    # date is `date`
echo 'date is $(date)'   # date is `date`

# ` ` backticks or reverse quotes
# This is used when output of 1 command is used for another command
echo `pwd`  # the output of pwd is given to echo(print).


a=cal
echo $a     # cal is output

a=`cal`
echo $a    # calender month is outputted.