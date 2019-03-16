from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from project1.items import Project1Item
from project1.func.printitem import print_item
from project1.func.parse_svg import parse_food_type, parse_num, parse_location


class BlogSpider(CrawlSpider):
    name = 'spi1'
    # start_urls = ['http://www.dianping.com/search/category/1/10']
    start_urls = [
        'http://www.dianping.com/shenzhen/ch10/r29'
    ]
    
    location = {'r1949', 'r7475', 'r12322', 'r1560', 'r1556', 'r1559', 'r12321', 'r12225', 'r1951', 'r1573', 'r12226', 'r1557', 'r12324', 'r12323', 'r3138', 'r12320', 'r12319', 'r1950'}

    food_type = {'g112', 'g117', 'g103', 'g111', 'g113', 'g110', 'g116', 'g219', 'g251', 'g508', 'g114', 'g102', 'g34236', 'g1959', 'g34014', 'g2714', 'g33759', 'g34055', 'g104', 'g207', 'g106', 'g1338', 'g101', 'g26481', 'g34032', 'g115', 'g25474', 'g1783', 'g250', 'g311', 'g6743', 'g109', 'g3243', 'g107', 'g34059', 'g118'}

    def parse_start_url(self, response):
        # print('enter parse_start_url' + response.url)
        for lbs in self.location:
            for ft in self.food_type:
                url = 'http://www.dianping.com/shenzhen/ch10/%s%so3' % (lbs, ft)
                # print('Request ' + url)
                yield Request(url, callback=self.parse_list_first)

    def parse_list_first(self, response):
        # print('enter parse_list_first ' + response.url)
        selector = Selector(response)
        pg = 0
        pages = selector.xpath('//div[@class="page"]/a/@data-ga-page').extract()
        if len(pages) > 0:
            pg = pages[len(pages) - 2]
        pg = int(str(pg)) + 1
        url = str(response.url)
        for p in range(1, pg):
            ul = url + 'p' + str(p)
            # print('Request ' + ul)
            yield Request(ul, callback=self.parse_list)

    def parse_list(self, response):
        # print('enter parse_list ' + response.url)
        item = Project1Item()
        sel = Selector(response)
        div = sel.xpath('//div[@id="shop-all-list"]/ul/li')
        for dd in div:
            names = dd.xpath('div[2]/div[1]/a[1]/h4/text()').extract()
            item['name'] = names[0]

            urls = dd.xpath('div[2]/div[1]/a[1]/@href').extract()
            item['url'] = str(urls[0])

            levels = dd.xpath('div[2]/div[2]/span/@title').extract()
            item['level'] = levels[0]

            comment_nums = dd.xpath('div[2]/div[2]/a[1]/b').extract()
            if len(comment_nums) > 0:
                item['comment_num'] = parse_num(comment_nums[0])
            else:
                item['comment_num'] = '0'

            avg_costs = dd.xpath('div[2]/div[2]/a[2]/b').extract()
            if len(avg_costs) > 0:
                item['avg_cost'] = parse_num(avg_costs[0])
            else:
                item['avg_cost'] = '0'

            tastes = dd.xpath('div[2]/span/span[1]/b').extract()
            if len(tastes) > 0:
                item['taste'] = parse_num(tastes[0])
            else:
                item['taste'] = '0'

            environments = dd.xpath('div[2]/span/span[2]/b').extract()
            if len(environments) > 0:
                item['environment'] = parse_num(environments[0])
            else:
                item['environment'] = '0'

            services = dd.xpath('div[2]/span/span[3]/b').extract()
            if len(services) > 0:
                item['service'] = parse_num(services[0])
            else:
                item['service'] = '0'

            food_types = dd.xpath('div[2]/div[3]/a[1]/span').extract()
            item['food_type'] = parse_food_type(food_types[0])

            locations = dd.xpath('div[2]/div[3]/a[2]/span').extract()
            item['location'] = parse_location(locations[0])

            # print_item(item)
            yield item

    def parse_apage(self, response):
        print('parse_apage ' + response.url)
        sel = Selector(response)
        div = sel.xpath('//div[@id="shop-all-list"]/ul/li')
        locations = div.xpath('div[2]/div[3]/a[2]/span').extract()
        for loc in locations:
            print(parse_location(loc))
        food_types = div.xpath('div[2]/div[3]/a[1]/span').extract()
        for food_type in food_types:
            print(parse_food_type(food_type))
        tastes = div.xpath('div[2]/span/span[1]/b').extract()
        for taste in tastes:
            print(parse_num(taste))
        environments = div.xpath('div[2]/span/span[2]/b').extract()
        for environment in environments:
            print(parse_num(environment))
        services = div.xpath('div[2]/span/span[3]/b').extract()
        for service in services:
            print(parse_num(service))
        avg_costs = div.xpath('div[2]/div[2]/a[2]/b').extract()
        for cost in avg_costs:
            print(parse_num(cost))
        comment_nums = div.xpath('div[2]/div[2]/a[1]/b').extract()
        for num in comment_nums:
            print(parse_num(num))
        shop_levels = div.xpath('div[2]/div[2]/span/@title').extract()
        for level in shop_levels:
            print(parse_num(level))
        shop_names = div.xpath('div[2]/div[1]/a[1]/h4/text()').extract()
        for name in shop_names:
            print(name)
        urls = div.xpath('div[2]/div[1]/a[1]/@href').extract()
        for url in urls:
            print(url)

    def parse_0(self, response):
        item = Project1Item()
        sel = Selector(response)
        div = sel.xpath('//div[@id="shop-all-list"]/ul/li')
        for dd in div:
            names = dd.xpath('div[2]/div[1]/a[1]/h4/text()').extract()
            item['name'] = names[0]

            urls = dd.xpath('div[2]/div[1]/a[1]/@href').extract()
            item['url'] = str(urls[0])

            levels = dd.xpath('div[2]/div[2]/span/@title').extract()
            item['level'] = levels[0]

            comment_nums = dd.xpath('div[2]/div[2]/a[1]/b').extract()
            if len(comment_nums) > 0:
                item['comment_num'] = parse_num(comment_nums[0])
            else:
                item['comment_num'] = '0'

            avg_costs = dd.xpath('div[2]/div[2]/a[2]/b').extract()
            if len(avg_costs) > 0:
                item['avg_cost'] = parse_num(avg_costs[0])
            else:
                item['avg_cost'] = '0'

            tastes = dd.xpath('div[2]/span/span[1]/b').extract()
            if len(tastes) > 0:
                item['taste'] = parse_num(tastes[0])
            else:
                item['taste'] = '0'

            environments = dd.xpath('div[2]/span/span[2]/b').extract()
            if len(environments) > 0:
                item['environment'] = parse_num(environments[0])
            else:
                item['environment'] = '0'

            services = dd.xpath('div[2]/span/span[3]/b').extract()
            if len(services) > 0:
                item['service'] = parse_num(services[0])
            else:
                item['service'] = '0'

            food_types = dd.xpath('div[2]/div[3]/a[1]/span').extract()
            item['food_type'] = parse_food_type(food_types[0])

            locations = dd.xpath('div[2]/div[3]/a[2]/span').extract()
            item['location'] = parse_location(locations[0])

            print_item(item)

    def parse_base(self, response):
        food_type = []
        selector = Selector(response)
        links = selector.xpath('//div[@id="classfy"]/a/@href').extract()
        for l in links:
            l = str(l)
            l = l[l.find('10/') + 3:]
            food_type.append(l)
        print(food_type)
