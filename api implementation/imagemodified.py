#implimenting streamlit ui here 
# creating a basic image summarizer here
# need to add spinner cause user will not know what is happening
'''
In this i basically used streamlit ui to make an ui in which user can 
upload the image and it will show the description of the image 
and it will also show spinner here
'''
from PIL import Image
from google import genai
from google.genai import types
import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv('API_KEY')
model=os.getenv('Model_name')
client=genai.Client(api_key=api_key)
st.title('Image Uplaod and show ')

upload=st.file_uploader("select an image",type=None)

if upload:
    st.image(upload,caption='image',use_column_width=True)
    image=Image.open(upload)

    with st.spinner('generating caption'):

        response=client.models.generate_content(
            model=model,
            contents=[image,'give me the caption of this photo'],
            config=types.GenerateContentConfig(
                system_instruction='make answer short and precise',
                temperature=0.4,
                
            )

        )
        caption=response.text
        st.success('caption generated:')
        st.write(caption)
