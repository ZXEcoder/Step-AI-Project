import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.html import remove_tags

class NvidiaSpider(CrawlSpider):
    name = "nvidia"
    allowed_domains = ["nvidia.com"]
    start_urls = ["https://docs.nvidia.com/cuda/"]
    custom_settings = {
        "DEPTH_LIMIT": 5,
        "FEED_FORMAT": "json",
        "FEED_URI": "data/scraped_data.json",
    }

    rules = (
        Rule(LinkExtractor(allow="docs.nvidia.com/cuda"), callback="parse_page", follow=True),
    )

    def parse_page(self, response):
        body_content = response.css('body').get()
        headings = response.css('h1::text, h2::text, h3::text, h4::text, h5::text, h6::text').getall()
        clean_body = " ".join(response.css('body *::text').getall()).strip()
        clean_body = remove_tags(clean_body)  # Remove any remaining HTML tags
        clean_body = clean_body.replace("\n", "").replace("\r", "")  # Remove newline and carriage return characters

        headings = [heading.replace("\n", "").replace("\r", "") for heading in headings if heading.strip()]
        
        yield {
            'url': response.url,
            'content': clean_body,
            'headings': headings if headings else None
        }
