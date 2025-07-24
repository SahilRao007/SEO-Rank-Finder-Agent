# by understanding the basics , ill try to create a chatbot
# after createing a basic structure ill make sure to add features 
'''
In this i basically created a simple chat bot.
'''
from google import genai
from google.genai import types
client=genai.Client(api_key='AIzaSyDZDERkK2zePpFmXiGOOuO8H3LwqJEiSNs')
print("Welcome to Demo chatbot")
print(" chat with the bot with anytopic")
print("if u want to exit write exit")


while True:

    prompt=input('user: ')
    if prompt.lower().strip()=='exit':
        print("thankyou for using")
        break
    instruction='make your response less than 50 words'
    response=client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=1.3,
            system_instruction='keep your answer short and not more than 30 words',
            
        )
    )
    print('-'*50)
    print('bot:',end=' ')
    print(response.text)