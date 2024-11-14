def calculate_due_amount(total_bill, payment):
    due_amount = total_bill - payment
    if due_amount > 0:
        return due_amount
    elif due_amount == 0:
        return "Bill fully paid"
    else:
        return f"Overpayment. Change to be returned: ${abs(due_amount):.2f}"

def get_valid_input(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            if user_input < 0:
                print("Please enter a non-negative amount.")
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

while True:
    total_bill = get_valid_input("Enter the total bill amount: $")
    payment = get_valid_input("Enter the payment amount: $")
    due_amount = calculate_due_amount(total_bill, payment)
    
    if isinstance(due_amount, float):
        print(f"Due amount: ${due_amount:.2f}")
    else:
        print(due_amount)
    
    continue_prompt = input("Would you like to calculate another bill? (yes/no): ").strip().lower()
    if continue_prompt != "yes":
        print("Exiting the program. Goodbye!")
        break
