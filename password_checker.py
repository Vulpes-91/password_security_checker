


while True:  # Запускать цикл до тех пор, пока не будет введен подходящий пароль
    print("Create a strong password. It MUST contain at least 1 lowercase letter, 1 uppercase letter, at least 1 special symbol (from !@#$%^&*()-+)  and must be at least 12 symbols long")
    user_pass = input("Please enter your password: ")
    user_pass_length = len(user_pass)
    user_pass_length_difference = 12 - user_pass_length
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_chars = "!@#$%^&*()-+"
    numbers = "1234567890"



    if user_pass_length < 12:
        print("The password is too short. Add at least " + str(user_pass_length_difference) + " characters")
    elif not any(letter in user_pass for letter in numbers):
        print("The password does not contain any numbers. Please add at least 1. ")
    elif not any(letter in user_pass for letter in lowercase_letters):
        print("The password does not contain any lowercase letters. Add at least 1.")
    elif not any(letter in user_pass for letter in uppercase_letters):
        print("The password does not contain any uppercase letters. Add at least 1.")
    elif not any(letter in user_pass for letter in special_chars):
        print("The password does not contain any valid special symbols. Add at least 1.")


    else:
        print("Password accepted.")
        break  # Выход из цикла, если пароль подходит