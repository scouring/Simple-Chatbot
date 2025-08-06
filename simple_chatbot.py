import openai

# openai.api_key = 

def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

print(chat("Tell me a joke about engineers"))
