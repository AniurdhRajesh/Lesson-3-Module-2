def check_alphabet_in_string(input_string):
    for char in input_string:
        if char == 'A' or char == 'a': 
            print("The alphabet 'A' is present.")
            break 
    else:
        print("The alphabet 'A' is not present.")
input_string = input("Enter a string: ")
check_alphabet_in_string(input_string)
