'''this bascially is the ui part of the project 
which will give and show the user what to search domain and the results 
and i have made sure that the csv files gets automatically downloaded 
'''
import streamlit as st # used streamlit to create a simple and easy ui interface
import pandas as pd # used pandas to download the files to csv 
from datetime import datetime # used this to mark or help in tracking the search result in future

from scrappernew import search_bing #importing search function from scrappernew 
from llm import analyze_with_llm #importing agent from llm file

st.set_page_config(page_title="WebReinvent Rank Agent", layout="wide")
st.title(" WebReinvent Rank Checker (Local AI Agent)")
st.markdown("Enter multiple keywords (one per line): seperated by newline")

keywords_input = st.text_area("Keywords", height=200)

if st.button("Run Agent"):
    if not keywords_input.strip():
        st.warning("Please enter at least one keyword (one per line).") # used newline instead of comma because using comma was messy
    else:
        keywords = [k.strip() for k in keywords_input.split("\n") if k.strip()]
        results_data = []
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # gets the datetime of current moment 

        for keyword in keywords:
            st.write(f"### Searching: **{keyword}**")
            results = search_bing(keyword)
            analysis = analyze_with_llm(results, keyword)
            results_data.append({
                "timestamp": timestamp,
                "keyword": keyword,
                "analysis": analysis,
                "top_results": results
            })  # data is stored in list-dict format which is used in padnas dict get converted into heading and columns

            st.markdown(f"** LLM Summary for '{keyword}':**")
            st.code(analysis, language="markdown")

        st.success(" All keywords processed!")

        # Flatten data for CSV
        flat_rows = []
        for entry in results_data:
            for result in entry["top_results"]:
                flat_rows.append({
                    "timestamp": entry["timestamp"],
                    "keyword": entry["keyword"],
                    "rank": result.get("rank"),
                    "title": result.get("title"),
                    "url": result.get("url"),
                    #"analysis": entry["analysis"] # this part is not giving correct answer its better to do manually
                })

        # df = pd.DataFrame(flat_rows)

        # # Auto-save CSV locally
        # output_path = "webreinvent_rank_results_final2.csv"
        # df.to_csv(output_path, index=False)
        # st.success(f" Results saved automatically to `{output_path}`")

