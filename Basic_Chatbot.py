#simple rule-based chatbot

name=input("enter your name:")

print(f"===HI, {name} WELCOME TO THE CHATBOT WORLD===\n")

def chatbot():

    while True:

        user=input("you:").lower()
        if "hello" in user:
            print("chatbot:Hi!\n")

        elif "how are you" in user:
            print("chatbot:I'm fine,thanks!\n")

        elif "bye" in user:
            print("chatbot:Goodbye\n")
            break
chatbot()