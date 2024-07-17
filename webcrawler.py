import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

class WebCrawler:
    def __init__(self, base_url, max_depth=5):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited = set()
        self.data = []

    def crawl(self):
        self._crawl(self.base_url, 0)
        return self.data

    def _crawl(self, url, depth):
        if depth > self.max_depth:
            return
        if url in self.visited:
            return
        self.visited.add(url)

        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return
        
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        self.data.append({'url': url, 'text': text})

        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
        for link in links:
            if urlparse(link).netloc == urlparse(self.base_url).netloc:
                self._crawl(link, depth + 1)
            time.sleep(1)  # Politeness delay

if __name__ == "__main__":
    base_url = 'https://docs.nvidia.com/cuda/'
    crawler = WebCrawler(base_url)
    scraped_data = crawler.crawl()
    print(f"Scraped {len(scraped_data)} pages.")
