'''
here i used ollama as a local llm and the model i used is llama3 

we could here fine tune the model here also but since it takes time to response so we will leave it
as it is 
'''
import json
import ollama

def analyze_with_llm(results, keyword):
    prompt = f"""You are a research assistant. Here are the top Bing search results for the keyword: "{keyword}":

{json.dumps(results, indent=2)} 

Your task:
- Tell me if webreinvent.com appears in the results
- At which position?
- Summarize the titles of the top 5 results.

Answer:
"""
    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']
