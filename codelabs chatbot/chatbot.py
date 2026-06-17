from datetime import datetime

print("🤖 AI Chatbot Started")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am doing great!")

    elif user_input == "your name":
        print("Bot: My name is RuleBot.")

    elif user_input == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user_input == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user_input == "thank you":
        print("Bot: You're welcome!")

    elif user_input == "time":
        print("Bot:", datetime.now().strftime("%H:%M:%S"))
        
    elif user_input == "date":
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif user_input in ["bye", "exit"]:
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")