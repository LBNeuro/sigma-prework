
int_list = []


def num_input_validation(user_input):
    while user_input.isnumeric() == False or user_input == "":
        user_input = input("Error, this input is invalid, Please try again: ")
    print("Thank you, your input has been validated.")

    return int(user_input)


print("Welcome to the min, max integer machine." \
" You will be asked for 5 integers and the minimum and Maximum integers in the list will be displayed")

for i in range(5):
    new_int = input("Please input a new integer to add the the list: ")
    new_int = num_input_validation(new_int)
    int_list.append(new_int)

print(f"{max(int_list)} is the Maximum integer in the list. \n" \
      f"{min(int_list)} is the Minimum integer in the list.")


