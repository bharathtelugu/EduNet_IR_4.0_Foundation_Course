# Function to reverse a string
reverse_string() {
    local str="$1"
    local reversed=""
    
    # Loop through the string from the end to the beginning
    for (( i=${#str}-1; i>=0; i-- )); do
        reversed="$reversed${str:i:1}"
    done
    
    echo "$reversed"
}

# Read input from the user
echo "Enter a string to reverse:"
read input_string

# Call the function and print the reversed string
reversed=$(reverse_string "$input_string")
echo "Reversed string: $reversed"

