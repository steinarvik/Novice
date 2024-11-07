import datetime

# Define some responses for keywords
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What’s on your mind?",
    "weather": "I'm not sure about the weather, but it’s always a good day to code!",
    "time": f"The current time is {datetime.datetime.now().strftime('%H:%M')}.",
    "day": f"Today is {datetime.datetime.now().strftime('%A')}.",
    "python": "Python is a versatile programming language, great for web development, data science, and more.",
    "bye": "Bye! Have a great day!",
}

# Default response if no keywords are found
default_response = "I'm not sure I understand, could you tell me something else?"


# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! I'm here to chat. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        print(user_input)

        # Check for keywords in user input
        response_found = False
        for keyword, response in responses.items():
            if keyword in user_input:
                print("Chatbot:", response)
                response_found = True
                if keyword == "bye":
                    return
                break

        # If no keywords matched, give the default response
        if not response_found:
            print("Chatbot:", default_response)


# Start the chatbot
chatbot()