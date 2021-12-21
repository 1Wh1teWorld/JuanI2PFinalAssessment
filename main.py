# Student Name: Steven Voronko
# Student Number: EC2057287
# Date: 21/12/2021
# Edinburgh College: Sighthill Campus

def display_menu():
    print("""
    ****************************************
    *
    Practical Assessment
    *
    ****************************************
    *
    1 - Display the users' information
    *
    *
    *
    *
    2 - Add a new user
    *
    *
    *
    *
    3 - Count the number of users
    *
    *
    *
    *
    4 - Exit
    *
    ****************************************
    """)

def display_user_info(user_list):

    if len(user_list) != 0:

        for i in range(0, len(user_list), 2):

            print(f"{user_list[i]}, {user_list[i+1]}")
    else:
        print("\nNo users currently in our records. Enter 2 to add a new user.")

def add_new_user(user_list):
    
    name = input("\nEnter your name below\n")
    phone_number = input("Enter your phone number below\n")

    if name in user_list and phone_number in user_list:
        print("Error: user already exists in our records.")
        return
    else:
        user_list.append(name)
        user_list.append(phone_number)

def count_users(user_list):
    
    print(f"Number of users: {len(user_list) // 2}")

def main():

    user_list = []

    display_menu()
    while True:
        user_choice = int(input("\nEnter your choice below\n"))

        if user_choice == 1:
            display_user_info(user_list)
        elif user_choice == 2:
            add_new_user(user_list)
        elif user_choice == 3:
            count_users(user_list)
        elif user_choice == 4:
            print("Terminating program")
            break
        else:
            print("Invalid choice! Please pick a number from the menu displayed above.")

main()