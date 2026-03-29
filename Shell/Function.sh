#!/bin/bash

# Function to add two numbers
add_numbers() {
    sum=$(( $1 + $2 ))
    echo "The sum is: $sum"
}

# Calling the function with two numbers
add_numbers 24 78

