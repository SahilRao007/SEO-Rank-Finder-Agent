from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def search_bing(keyword, max_results=10):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--user-agent=Mozilla/5.0")

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
                link = link_elem.get_attribute("href")

                if title and link:
                    count += 1
                    data.append({
                        "rank": count,
                        "title": title.strip(),
                        "url": link.strip()
                    })

                    if "webreinvent.com" in link:
                        break
            except:
                continue
        return data
    finally:
        driver.quit()
