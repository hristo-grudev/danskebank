BOT_NAME = 'danskeci'

SPIDER_MODULES = ['danskeci.spiders']
NEWSPIDER_MODULE = 'danskeci.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'danskeci.pipelines.DanskeciPipeline': 100,

}