import datetime

run = True
file = open('userdata.txt','')
def options_menu():
    global run
    print("\n 1) Type your message \n 2) Show all saved messages and dates \n 3) Delete the name and date \n 4) Exit")
    user_choice = input("Enter your option: ")
    
    if user_choice == '1':
        save_message()
    elif user_choice == '2':
        show_details()
    elif user_choice == '3':
        deleate_mesage()
    elif user_choice == '4':
        run = False
        print("📂 Exiting the program. All messages saved successfully!")
    else:
        print("⚠️ Invalid option, please choose again!")

def save_message():
    user_message = input("Enter your message: ")
    
    if not user_message.strip():  # Prevent empty messages
        print("⚠️ Please enter a valid message!")
        return  # Stop function if input is empty

    user_date = input("Enter the future reminder date (dd/mm/yyyy): ")
    
    try:
        formatted_date = datetime.datetime.strptime(user_date, "%d/%m/%Y")
        today_date = datetime.datetime.now()
        
        if formatted_date <= today_date:
            print("⚠️ Enter a future date, not a past date!")
            return  # Stop function if the date is in the past
        
        # Save to file
        with open("userdata.txt", "a") as file:
            file.write(f"message: {user_message} | reminder Date: {user_date}\n")
        
        print("✅ Message and date saved successfully!")
    
    except ValueError:
        print("⚠️ Enter the correct date format (dd/mm/yyyy)")

def show_details():
    try:
        with open("userdata.txt", "r") as file:
            messages = file.readlines()
            
            if messages:
                print("\n📜 Saved Messages and Dates:")
                for i, msg in enumerate(messages):
                    print(f"{i+1}) {msg.strip()}")
            else:
                print("📂 No messages found.")
    
    except FileNotFoundError:
        print("📂 No messages saved yet.")

def deleate_mesage():
    pass

# Main loop
while run:
    options_menu()
