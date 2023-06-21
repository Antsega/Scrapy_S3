# Quotes Scraper

The Quotes Scraper is a Python script that efficiently scrapes quotes tagged with humor from [quotes.toscrape.com](https://quotes.toscrape.com) and stores them in JSON Lines format both locally and in an Amazon S3 bucket. This script utilizes the Scrapy library for web scraping and boto3 for interacting with Amazon Web Services (AWS).

## Features

- Scrapes quotes and authors from the web.
- Stores data in JSON Lines format.
- Saves the scraped data locally.
- Uploads the scraped data to an Amazon S3 bucket with unique timestamps for filenames to avoid overwriting.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- An AWS account with S3 access.
- AWS Access Key ID and Secret Access Key.

## Dependencies

This script requires the following Python libraries:

- scrapy
- boto3
- python-dotenv

You can install them using pip:

```sh
pip install scrapy boto3 python-dotenv
```

## Set Up

To run the script, navigate to the directory containing the script and execute the following command:

```sh
scrapy runspider quotes_spider.py -o quotes.jsonl
```

This command runs the scraper and outputs the scraped data in JSON Lines format to a file named quotes.jsonl. The data will also be uploaded to the specified AWS S3 bucket.

## Note
This script is intended for educational purposes and should be used responsibly by adhering to the terms and conditions of the websites you are scraping as well as the laws and regulations regarding web scraping.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.






