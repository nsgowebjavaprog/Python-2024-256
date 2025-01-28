def chatbot():
    conversion = {
        "hi": "Hello",
        "hello": "Hi",
        "how are you": "I am fine, thank you",
        "what is your name": "I am a chatbot",
        "bye": "Goodbye"
    }
    print("Chatbot: Hi, I am a chatbot")
    
    while True:
        user_input = input("User: ").lower()
        
        if user_input in conversion:
            print("Chatbot: ", conversion[user_input])
        elif user_input == "good bye":
            break
        else:
            print("Chatbot: I am sorry, I did not understand")    
            
chatbot()            