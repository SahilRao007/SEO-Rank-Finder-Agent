from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
# i included this header for changing the bing unusual link to the general link 
import urllib.parse as urlparse
from urllib.parse import parse_qs, unquote
import base64

#decoding bing or a1-style redirect -> basically the links starting with a1 or ck/a ones will be corrected here
def decode_bing_redirect(link):
    if not link:
        return link

    # Case 1: 
    if link.startswith("a1"):
        b64 = link[2:]
        b64 += "=" * (-len(b64) % 4)
        try:
            decoded = base64.urlsafe_b64decode(b64).decode("utf-8")
            if urlparse.urlparse(decoded).scheme in ("http", "https"):
                return decoded
        except Exception:
            pass

    # Case 2: 
    if "bing.com/ck/a?" in link:
        parsed = urlparse.urlparse(link)
        qs = parse_qs(parsed.query)

        if "u" in qs:
            raw_u = qs["u"][0]
            if raw_u.startswith("a1"):
                b64 = raw_u[2:]
                b64 += "=" * (-len(b64) % 4)
                try:
                    decoded = base64.urlsafe_b64decode(b64).decode("utf-8")
                    if urlparse.urlparse(decoded).scheme in ("http", "https"):
                        return decoded
                except Exception:
                    pass
            else:
                return unquote(raw_u)

        if "r" in qs:
            r = qs["r"][0]
            r += "=" * (-len(r) % 4)
            try:
                return base64.urlsafe_b64decode(r).decode("utf-8")
            except Exception:
                return link

    return link

#  Main Project scrapper search logic 
def search_bing(keyword, max_results=10):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu") # run without gpu ( totally optional but was making problem running with ollama )
    options.add_argument("--window-size=1920,1080") #this was necessary cause without it browser was opening in mobile view
    options.add_argument("--user-agent=Mozilla/5.0") # to prevent selenium from bing bots 

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        query = keyword.replace(" ", "+")
        url = f"https://www.bing.com/search?q={query}"
        driver.get(url)
        time.sleep(2)

        results = driver.find_elements(By.CSS_SELECTOR, "li.b_algo")
        data = []

        count = 0
        for result in results:
            if count >= max_results:
                break
            try:
                title_elem = result.find_element(By.TAG_NAME, "h2")
                link_elem = title_elem.find_element(By.TAG_NAME, "a")
                title = title_elem.text
                raw_link = link_elem.get_attribute("href")
                decoded_link = decode_bing_redirect(raw_link) # the proper link is genereated here 

                if title and decoded_link:
                    count += 1
                    data.append({
                        "rank": count,
                        "title": title.strip(),
                        "url": decoded_link.strip()
                    })

                    if "webreinvent.com" in decoded_link:
                        break
            except:
                continue
        return data
    finally:
        driver.quit() # closes the driver which is running in the background for webscrapping 
