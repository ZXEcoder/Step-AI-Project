# Scrapy settings for mycrawler project
BOT_NAME = "mycrawler"

SPIDER_MODULES = ["mycrawler.spiders"]
NEWSPIDER_MODULE = "mycrawler.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
ITEM_PIPELINES = {
   'scrapy.pipelines.files.FilesPipeline': 1,
}

# Output settings
FEED_FORMAT = "json"
FEED_URI = "data/scraped_data.json"

# Limit depth to 5
DEPTH_LIMIT = 5
