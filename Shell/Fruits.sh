# Explicit declaration 
fruits=("apple" "banana" "cherry") 
# Adding an element explicitly 
fruits[3]="date" 
# Implicit declaration 
numbers=() 
numbers[0]=10 
numbers[1]=20 
numbers[2]=30 
echo "Fruits: ${fruits[@]}" 
echo "Numbers: ${numbers[@]}"
