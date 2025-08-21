
#   Rank Checker (Local AI Agent)

This project is a **Local AI Agent** that checks whether [webreinvent.com](https://webreinvent.com) [ 'This can be for any website '] appears in **Bing search results** for given keywords.  
It combines **web scraping (Selenium)**, a **local LLM (Ollama + LLaMA 3)**, and a **Streamlit UI** to provide both raw search data and an AI-generated analysis.

---

## 🚀 Features
- ✅ Enter multiple keywords at once  
- ✅ Scrapes **top Bing search results** (titles, URLs, rank)  
- ✅ Cleans Bing redirect links for accuracy  
- ✅ Uses **Ollama (LLaMA 3)** for AI-powered analysis:
  - Detects if `webreinvent.com` appears in results  
  - Identifies the **rank/position**  
  - Summarizes the **top 5 results**  
- ✅ Streamlit-based interactive UI  
- ✅ Download results as **CSV** for further analysis  

---

## 🛠️ Tech Stack
- [Python 3](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – UI  
- [Selenium](https://www.selenium.dev/) – Web scraping  
- [Ollama](https://ollama.com/) – Local LLM runtime  
- [LLaMA 3](https://ai.meta.com/llama/) – Language model  

---


---

## ⚡ How It Works
1. User enters keywords in the Streamlit app.  
2. For each keyword:  
   - **Scraper (Selenium)** fetches top Bing search results.  
   - **AI Agent (Ollama + LLaMA 3)** analyzes results:
     - Checks if `webreinvent.com` appears.  
     - Summarizes top 5 results.  
3. Results are shown on the UI and can be downloaded as a CSV.  

---

## 📸 Demo (Workflow)
1. Run the Streamlit app:
   ```bash
   streamlit run interface2.py
