#! /bin/bash

# Below file takes filename as input, opens file, appends content to file.

echo -e "Provide file name: \c"   # \c To take input in same line, other wise in new line.
read -r file     # reads input as file. file is variable name here.
touch ./$file.sh      # creates .sh file in current dir. like abc.sh
echo "enter content" > ./$file.sh       # appends content
echo "enter more content" >> ./$file.sh # more content
echo "$(date)" >> ./$file.sh            # adds date time
echo "`date`" >> ./$file.sh             # adds date time
