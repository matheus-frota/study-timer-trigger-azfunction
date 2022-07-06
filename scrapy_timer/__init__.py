import datetime
import logging

import scrapy
from scrapy.crawler import CrawlerRunner
import azure.functions as func
import scrapydo

# Necessário a importação relativa para evitar
# erro ModuleNotFoundError
from .scrapy_timer.spiders.example import ExampleSpider

scrapydo.setup()

def myfunc(time):
    print(f'Time {time} - {ExampleSpider.name}')
    results = scrapydo.run_spider(ExampleSpider)
    print(results)
    # process = CrawlerRunner()
    # print(f'Process: {process}')
    # process.crawl(ExampleSpider)



def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    if mytimer.past_due:
        logging.info('The timer is past due!')

    myfunc(utc_timestamp)

    # logging.info('Python timer trigger function ran at %s', utc_timestamp)