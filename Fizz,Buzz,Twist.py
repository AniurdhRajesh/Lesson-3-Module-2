def check_numbers_in_range(start, end):
    for num in range(start, end + 1):
        if num % 20 == 0:
            print("twist")
        elif num % 15 == 0:
            pass
        elif num % 5 == 0:
            print("fizz")
        elif num % 3 == 0:
            print("buzz")
        else:
            print(num)

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

check_numbers_in_range(start, end)
