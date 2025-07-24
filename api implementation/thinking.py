'''
In this i basically wanted to see how the gemini thinks before answering the question 
'''

from google import genai
from google.genai import types
import os 
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv('API_KEY')
model=os.getenv('Model_name')

client = genai.Client(api_key=api_key)
prompt = "What is the sum of the first 50 prime numbers?"
response = client.models.generate_content(
  model=model,
  contents=prompt,
  config=types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(
      include_thoughts=True
    )
  )
)

for part in response.candidates[0].content.parts:
  if not part.text:
    continue
  if part.thought:
    print("Thought summary:")
    print(part.text)
    print()
  else:
    print("Answer:")
    print(part.text)
    print()