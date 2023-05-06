import openai
import speech_recognition as sr

openai.api_key = "YOUR API KEY HERE"

def generate_response(prompt, conversation_history):
    prompt_with_history = f"{conversation_history}User: {prompt}\nAI:"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt_with_history,
        temperature=0.5,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text.strip()

def main():
    conversation_history = "System: You are a sentient AI assistant designed to engage in context-aware, human-like conversations.\n"
    
    print("Hello! Welcome to SentiGPT.")
    print("What can I do for you?")
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        
        response = generate_response(user_input, conversation_history)
        print("AI:", response)
        
        conversation_history += f"User: {user_input}\nAI: {response}\n"

if __name__ == "__main__":
    main()
