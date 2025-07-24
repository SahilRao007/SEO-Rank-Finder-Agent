# this is to learn image caption generation 
# after working i need to learn streamlit ui 

# multimodal inputs 
'''
In this i basically learned to deal with images 
i used PIL lib to import images and then basically it tells whats in the image using 
google gemini api
'''
from PIL import Image
from google import genai
import os 
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv('API_KEY')
model=os.getenv('Model_name')
client=genai.Client(api_key=api_key)
# make it accept various types of images 
# make it take from web search ? 
img_path='tiger.jpg'
image=Image.open(img_path)

response=client.models.generate_content(
    model=model,
    contents=[image,'give me the short description of the photo']
)

print(response.text)