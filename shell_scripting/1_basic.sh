#! /bin/bash    # execute using /bin/bash

cat /etc/shells   # displays all shells present the system. /bin/bash is mostly used.

which bash  # /bin/bash

#  /bin/sh   # OR /bin/bash to enter into sh or bash.
#  exit  # to exit out.

echo "hello world"

# This is a comment

echo "Welcome USER"
echo "Welcome $USER"   # Here USER is a variable. we access USER variable using $USER. This actually prints the username.

echo "The directory is pwd"
echo "The directory is `pwd`"
# OR
echo "The directory is $(pwd)"  # `` or $() are used for command substitution.

echo "Today date is `date`"
echo "Today date is $(date)"

a=4    # no spaces around =. else error will be shown.
echo $a # 4



# script can be executed using

#>. 1_basic.sh
#>source 1_basic.sh
#>./1_basic.sh
#>sh 1_basic.sh




