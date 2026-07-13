import ollama

def chat_with_sol(message):
    response = ollama.chat(
        model = "qwen2.5:3b",
        messages = [
            {
                "role": "system",
                "content":"You are Sol, a friendly personal AI assistant."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response["message"]["content"]

while True:

    user_input = input("You: ")

    if user_input.lower() in ["quit","exit","bye"]:
        print("Sol: Goodbye!")
        break

    answer = chat_with_sol(user_input)
    print("Sol: ", answer)