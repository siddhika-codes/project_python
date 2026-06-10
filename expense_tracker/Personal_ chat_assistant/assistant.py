# PERSONA CHAT ASSISTANT
response = {
    "hello" : "Hey! How are you?",
    "how are you"  : "I'm great, thanks for asking!",
    "what is your name"  : "I am your personal assistant!",
    "bye" :  "Goodbye! Take care!",
}

def get_response(user_input):
     user_input = user_input.lower()
     if user_input in response:
        return response[user_input]
     else:
        return "Sorry, I don't understand that"

while True:
    userAsk = input("Your queries : ")
    if userAsk == "bye":
        print("Goodbye!")
        break
    print(get_response(userAsk))

