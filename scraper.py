from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Setup driver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

product_pages = [
    ("Handmade Crochet Flower", "https://www.daraz.pk/tag/hand-made-crochet-flower/"),
    ("Crocheted Accessories", "https://www.daraz.pk/tag/crocheted-accessories/"),
]

all_data = []

for category, url in product_pages:
    print(f"Scraping {category}...")
    driver.get(url)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-qa-locator='product-item']")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    products = driver.find_elements(By.CSS_SELECTOR, "div[data-qa-locator='product-item']")
    for product in products:
        try:
            try:
                name = product.find_element(By.CSS_SELECTOR, "div.RfADt a").text.strip()
                if not name:
                    name = product.find_element(By.CSS_SELECTOR, "a[title]").text.strip()
            except:
                name = "N/A"
            if name == "N/A": continue 
            try:
                price = product.find_element(By.CSS_SELECTOR, "span.ooOxS").text.strip()
            except: price = ""
            try:
                rating = product.find_element(By.CSS_SELECTOR, "span.qzqFw").text.strip()
            except: rating = ""
            try:
                link = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            except: link = url
            all_data.append([category, name, price, rating, link])
        except: continue
    time.sleep(3)

driver.quit()
# Logic added. CSV Export will be added in final commit.