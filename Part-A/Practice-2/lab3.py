# Chat-Bot Application Using Simple Tuple Data Structure

def chatbot():
    content = {
        "1":"111",
        "2":"222",
        "3":"333",
        "4":"444",
        "5":"555",
        "6":"666"
    }
    
    print("Hey Here I am Chat-Bot How Can i Help you Today")
    
    while True:
        user_input = input("you:").lower()
        
        if user_input in content:
            print("Chatbot: ", content[user_input])
        elif user_input  == "good by":
            break
        else:
            print("Chatbot: Oh I am not Understand")   
chatbot()            