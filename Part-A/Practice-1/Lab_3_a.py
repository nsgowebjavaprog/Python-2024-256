def chatbot():
    con = {
        "1": "11111",
        "2": "2222",
        "3": "3333",
        "4": "44444",
        "5": "5555"
    }
    print("I am Chat-Bot")
    
    while True:
        user_input = input("You - Side: ").lower()
        
        if user_input in con:
            print("Chatbot: ", con[user_input])
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Invalid input. Please try again.")

chatbot()
