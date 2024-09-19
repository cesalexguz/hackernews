import scrapy

"""
This class create a spider using scrapy. It extracts the data of the selected page,
capturing the number, title, points, and number of comments for each entry
"""
class HackerNewsSpider(scrapy.Spider):
    # Name of the spider. In this case the name of the site
    name = "hackernews"
    # URL from which we extract the data
    start_urls = ['https://news.ycombinator.com/']

    """
        Method that parses the response from the start URL and extracts the data
    """
    def parse(self, response):
        # We use CSS selectors from the response to get the requested fields. In this case each row of the list 
        for entry in response.css('tr.athing'):
            item = {
                # Get the number or set to "NA" if not found it
                'number': entry.css('span.rank::text').get() or "NA",
                # Get the title or set to "NA" if not found it. After that delete special characters from the title to avoid problems counting the words
                'title': (entry.css('span.titleline a::text').get() or "NA").replace("\u00e2\u20ac\u201c", ""),
                # Get the points or set to "0" if not found it
                'points': entry.xpath('following-sibling::tr[1]//span[@class="score"]/text()').re_first(r'(\d+)') or "0",
                # Get the comments or set to "0" if not found it
                'comments': entry.xpath('following-sibling::tr[1]//a[contains(text(),"comments")]/text()').re_first(r'(\d+)') or "0"
            }
            yield item