# Define the function
def add_numbers(num1, num2):
    return num1 + num2

# Create the assistant
class Assistant:
    def process(self, message):
        # Split the message into words
        words = message.split()

        # Check if the message is a request to add numbers
        if words[0] == "add":
            # Parse the numbers to add
            num1 = int(words[1])
            num2 = int(words[2])

            # Use the add_numbers function to add the numbers
            result = add_numbers(num1, num2)

            # Return the result
            return f"The sum of {num1} and {num2} is {result}."

        else:
            return "I'm sorry, I didn't understand that. Please ask me to add two numbers."

# Test the assistant
assistant = Assistant()
print(assistant.process("add 5 7"))