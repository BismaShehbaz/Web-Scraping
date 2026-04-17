# Project Name: Daraz Crochet Scraper

### 1. Project Overview
* **Target Website:** 
  - https://www.daraz.pk/tag/hand-made-crochet-flower/
  - https://www.daraz.pk/tag/crocheted-accessories/
* **Data Fields Extracted:** Category, Name, Price, Rating, Source URL
* **Tools Used:** Python, Selenium, WebDriver Manager

### 2. Setup Instructions
1. Clone this repo: `git clone [Your Link]`
2. Install dependencies: `pip install -r requirements.txt`
3. Run script: `python scraper.py`

### 3. Challenges & Solutions
* **Technical Hurdle:** Handled dynamic content loading on Daraz.pk by implementing Selenium's `WebDriverWait` to ensure product elements are fully rendered before extraction and used JavaScript scrolling to trigger lazy-loading of items.
