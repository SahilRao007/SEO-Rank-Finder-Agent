import streamlit as st
import json
import pandas as pd
from datetime import datetime

from scrappernew import search_bing
from llm import analyze_with_llm

st.set_page_config(page_title="WebReinvent Rank Agent", layout="wide")
st.title("🔍 WebReinvent Rank Checker (Local AI Agent)")
st.markdown("Enter multiple keywords (one per line):")

keywords_input = st.text_area("Keywords", height=200)

if st.button("Run Agent"):
    if not keywords_input.strip():
        st.warning("Please enter at least one keyword seperated by comma's")
    else:
        keywords = [k.strip() for k in keywords_input.split("\n") if k.strip()]
        results_data = []
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for keyword in keywords:
            st.write(f"### 🔎 Searching: **{keyword}**")
            results = search_bing(keyword)
            analysis = analyze_with_llm(results, keyword)
            results_data.append({
                "timestamp": timestamp,
                "keyword": keyword,
                "analysis": analysis,
                "top_results": results
            })

            st.markdown(f"**🧠 LLM Summary for '{keyword}':**")
            st.code(analysis, language="markdown")

        st.success("✅ All keywords processed!")

        flat_rows = []
        for entry in results_data:
            for result in entry["top_results"]:
                flat_rows.append({
                    "timestamp": entry["timestamp"],
                    "keyword": entry["keyword"],
                    "rank": result.get("rank"),
                    "title": result.get("title"),
                    "url": result.get("url"),
                    "analysis": entry["analysis"]
                })

        df = pd.DataFrame(flat_rows)

        if st.checkbox("📥 Download results as CSV?"):
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download CSV File",
                data=csv,
                file_name="webreinvent_rank_results.csv",
                mime="text/csv"
            )
