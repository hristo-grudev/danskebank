import scrapy

from scrapy.loader import ItemLoader
from ..items import DanskeciItem
from itemloaders.processors import TakeFirst


class DanskeciSpider(scrapy.Spider):
	name = 'danskeci'
	start_urls = ['https://danskeci.com/ie/news']

	def parse(self, response):
		post_links = response.xpath('//div[@class="columns medium-10 medium-offset-1"]/ul/li/a/@href')
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1//text()').get()
		description = response.xpath('//div[@class="row article-body"]//text()|//div[@class="row article-header text-left"]//p//text()|//div[@class="article"]//text()|//p[@class="article-subheadline"]/text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//div[@class="meta"]/span/text()').get()

		item = ItemLoader(item=DanskeciItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
