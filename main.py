from ollama import chat
from ollama import ChatResponse

model = "deepseek-r1:14b"


response: ChatResponse = chat(model=model, messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)