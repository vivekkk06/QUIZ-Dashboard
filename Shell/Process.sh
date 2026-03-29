#!/bin/bash

input_file="input.txt"
output_file="output.txt"

> "$output_file"

awk '{
    if ($0 ~ /@/) {
        email = $0;
        print name "\t\t\t\t" email >> "'"$output_file"'"
    } else {
        name = $0
    }
}' "$input_file"

echo "Processing complete. Output written to $output_file."
