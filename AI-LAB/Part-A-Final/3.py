def chatbot():
    conversion = {
        "1":"1111",
        "2":"2222",
        "3":"3333",
        "4":"4444",
        "5":"5555",
        "6":"6666",
    }
    
    print("Hello How can i help you!!..")
    
    while True:
        user_input = input("User Side: ").lower()
        
        if user_input in conversion:
            print(conversion[user_input])
        elif user_input == "by":
            break
        else:
            print("Not Understand......!") 
chatbot()                   