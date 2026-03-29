#!/usr/bin/sh

sum=0
i=1

while [ $i -le 10 ]
do
    sum=$(( sum + i ))
    i=$(( i + 1 ))
done

echo "The sum of numbers from 1 to 10 is: $sum"

