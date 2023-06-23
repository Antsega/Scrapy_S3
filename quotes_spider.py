import scrapy
import json
import os
import boto3
from dotenv import load_dotenv
from datetime import datetime

# load environment variables from .env.local
load_dotenv('.env.local')

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def __init__(self, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.s3 = boto3.client('s3',
                                aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                                aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
        self.bucket_name = os.getenv("S3_BUCKET_NAME")

        # Unique file name with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.local_filename = f'quotes_{timestamp}.jsonl'
        self.s3_key = f'quotes_{timestamp}.json'
    

    def parse(self, response):
        quotes = []
        for quote in response.css('div.quote'):
            quotes.append({
                'author': quote.xpath('span/small/text()').get(),
                'text': quote.css('span.text::text').get(),
            })
        
        #Save to local file
        with open(self.local_filename, 'a') as file:
            for quote in quotes:
                file.write(json.dumps(quote) + '\n')

        # Upload to S3
        self.s3.put_object(Body=json.dumps(quotes),
                           Bucket=self.bucket_name,
                           Key=self.s3_key)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
