def reverse_string(input_string: str) -> str:
    l = len(input_string)
    return (input_string[l-1:0:-1] + input_string[0])

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
