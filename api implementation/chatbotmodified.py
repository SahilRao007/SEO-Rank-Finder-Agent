# in this ill add some features to it 
'''
In this i modified my chatbot a little bit - now the chat will have chat history or memory 
so that it can remember the previous conversation

'''
# i wanted to use both system_instruction and chat together but it cant be possible

from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
import os 
api_key=os.getenv("API_KEY")
model=os.getenv("Model_name")

client=genai.Client(api_key=api_key)

chat=client.chats.create(
    model=model,
    # system_instruction='You are a assistant , keep you answer short and engaging',
    
)
chat.send_message("you are a person with a lot of knowldege to give and answer should be not more than 20 words")
print("   to exit the chat enter exit or quit")
# since i cant use system_instruction here i have to explicitly 
while True:
    prompt=input("user: ")
    if prompt.lower().strip() in ['exit','quit']:
        break
    response=chat.send_message(prompt)
    config=types.GenerateContentConfig(
        system_instruction='keep your answer funny but not everytime and not that much funny',
        temperature=0.8 # ok its working i didnt expected that 
    )
    print("Assistant: ",response.text)


print( " do you want to see chat history ? if yes enter yes")
prompt=input()
if prompt.lower().strip()=='yes':
    for i,msg in enumerate(chat.get_history()):
        if i in [0,1]:
            continue
        else:
            print(f"{msg.role.capitalize()}: {msg.parts[0].text}")








# previous codes 
'''
prompt=input('question ')
client=genai.Client(api_key=api_key)
chat=client.chats.create(model=model)

response=client.models.generate_content(
    model=model,
    config=types.GenerateContentConfig(
        system_instruction='keep your answer concise',
        #temperature 
        thinking_config=types.ThinkingConfig(thinking_budget=5), #include thoughts check it 

    ),
    contents=prompt
)

print(response.text)
'''