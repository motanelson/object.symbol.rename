printf "give me the file object to change ? \n"
read a 
printf "give me the symbol object from ? \n"
read b
printf "give me the new symbol object to rename ? \n"
read c
objcopy --redefine-sym $b=$c $a /tmp/$a
cp  /tmp/$a $a
