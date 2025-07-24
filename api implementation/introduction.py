## this is where i will see how to use api in python 
'''
In this basically i learned how to use the api keys and use the prompt to show me the resonse 
pretty basic project
'''
from google import genai
from google.genai import types 

client=genai.Client(api_key='')

print(' '*5,'enter')
prompt=input('User: ')

print()
response=client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        
        thinking_config=types.ThinkingConfig(thinking_budget=0),
        system_instruction='dont make your answer longer than 50 words'
    )
)

print(response.text)
