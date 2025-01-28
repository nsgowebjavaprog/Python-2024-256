def chatbot():
    
    conversion = {
        "1":"111",
        "2":"222",
        "3":"333",
        "4":"444",
        "5":"555",
        "6":"666"
    }
    
    print("Hey I am Chatbot How can I help you today")
    while True:
        user_input = input("User : ").lower()
        
        if user_input in conversion:
            print("Chatbot : ", conversion[user_input])
        elif user_input == "good by":
            break
        else:
            print("Chatbot : Oh I am not Understand")    
    
chatbot()    