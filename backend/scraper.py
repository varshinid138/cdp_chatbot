import requests
from bs4 import BeautifulSoup

CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com"
}

def scrape_docs(cdp):
    url = CDP_DOCS.get(cdp.lower())
    if not url:
        return "Invalid CDP name"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
    except requests.exceptions.RequestException as e:
        return f"Error fetching {url}: {str(e)}"

    soup = BeautifulSoup(response.text, "html.parser")
    text = " ".join([p.text for p in soup.find_all("p")])  # Extract all paragraphs
    return text if text.strip() else " "
