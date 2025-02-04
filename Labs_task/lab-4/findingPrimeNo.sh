# Function to check if a number is prime
is_prime() {
    local num=$1
    if [ $num -le 1 ]; then
        return 1  # Not a prime number
    fi
    for (( i=2; i*i<=num; i++ )); do
        if [ $(( num % i )) -eq 0 ]; then
            return 1  # Not a prime number
        fi
    done
    return 0  # Prime number
}

# Read the range from the user
echo "Enter the range (start and end):"
read start end

echo "Prime numbers between $start and $end are:"

# Loop through the range and check for prime numbers
for (( num=$start; num<=$end; num++ )); do
    if is_prime $num; then
        echo $num
    fi
done

