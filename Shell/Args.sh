echo Number of arguments passed is $#
echo Name of the script is $0
echo "Process ID: $$"

for arg in $*
do 
	echo $arg
done
