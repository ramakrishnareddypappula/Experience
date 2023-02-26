
function my_function() {    # () and function are optional here. without these as well, fun works fine.
    echo "parameter 1 is $1"
    echo "parameter 2 is $2"
    echo "parameter 3 is $3"
    echo "parameter 4 is $4"

}

my_function "Hello" "World" "Hi"



function my_func {
   if [ -f $1 ]      # if param 1 is file.
   then
   tail -n 5 $1
   fi
}

my_func 10_case.sh