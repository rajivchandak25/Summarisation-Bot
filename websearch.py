from ddgs import DDGS
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# -------------------------------
# Web Search + Summarizer
# -------------------------------
class WebSearch:
    def __init__(self):
        # Hugging Face summarizer model
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def get_top_links(self, query, num_results=5):
        """
        Uses DuckDuckGo search to fetch top links.
        """
        links = []
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=num_results)
            for res in results:
                if "href" in res:
                    links.append(res["href"])
        return links

    def fetch_and_summarize(self, url):
        """
        Scrape webpage text and summarize it.
        """
        try:
            response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = " ".join([p.get_text() for p in soup.find_all("p")])

            if len(paragraphs) > 500:
                summary = self.summarizer(
                    paragraphs[:1000],
                    max_length=2000,
                    min_length=100,
                    do_sample=False
                )
                return summary[0]["summary_text"]
            return paragraphs[:500]
        except Exception:
            return None
