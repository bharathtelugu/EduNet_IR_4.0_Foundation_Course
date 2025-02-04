# path to the file
filepath="./reverseOfString.sh"

# storing file size in a variable.
size=$(wc --bytes < $filepath)

# displaying file size
echo "The size of file is $size Bytes"

