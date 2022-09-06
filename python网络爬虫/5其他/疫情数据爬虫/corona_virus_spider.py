import json
import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm


class CoronaVirusSpider(object):

    def __init__(self):
        # 数据主页网址
        self.home_url = "https://ncov.dxy.cn/ncovh5/view/pneumonia"

    def get_content_from_url(self, url):
        # 请求数据
        response = requests.get(url)
        # 获取主页数据
        home_page = response.content.decode()

        return home_page

    def parse_home_page(self, home_page, tag_id):
        # 解析主页数据
        soup = BeautifulSoup(home_page, "lxml")

        script = soup.find(id=tag_id)

        text = script.text

        # 利用正则表达式提取数据
        json_str = re.findall(r"\[.+\]",text)[0]
        data = json.loads(json_str)

        return data

    def save_data(self, path, data):

        with open(path, "w", encoding="utf8") as fp:
            json.dump(data, fp, ensure_ascii=False)

    def load(self, path):

        with open(path, encoding="utf8") as fp:
            data = json.load(fp)

        return data

    def parse_corona_virus(self, corona_virus_cata, desc):

        corona_virus = []

        for country in tqdm(corona_virus_cata, desc):

            statistics_data_url = country['statisticsData']

            statistics_data_json_str = self.get_content_from_url(statistics_data_url)

            statistics_data = json.loads(statistics_data_json_str)["data"]

            for one_day in statistics_data:
                one_day["provinceName"] = country["provinceName"]
                if country.get("countryShortCode"):
                    one_day["countryShortCode"] = country["countryShortCode"]

            corona_virus.extend(statistics_data)

        return corona_virus

    def crawl_last_day_corona_virus(self):

        home_page = self.get_content_from_url(self.home_url)

        last_day_corona_virus_data = self.parse_home_page(home_page,"getListByCountryTypeService2true")

        self.save_data("data/last_day_corona_virus.json", last_day_corona_virus_data)

    def crawl_last_day_corona_virus_china(self):
        home_page = self.get_content_from_url(self.home_url)

        last_day_corona_virus_data = self.parse_home_page(home_page, "getAreaStat")
        print(last_day_corona_virus_data)
        self.save_data("data/last_day_corona_virus_china.json", last_day_corona_virus_data)

    def crawl_corona_virus(self):

        last_day_corona_virus = self.load("data/last_day_corona_virus.json")

        corona_virus = self.parse_corona_virus(last_day_corona_virus, "1月23日以来各国疫情数据：")

        self.save_data("data/corona_virus.json", corona_virus)

    def crawl_corona_virus_china(self):

        last_day_corona_virus_china = self.load("data/last_day_corona_virus_china.json")

        corona_virus = self.parse_corona_virus(last_day_corona_virus_china, "1月22日以来各省疫情数据：")

        self.save_data("data/corona_virus_china.json", corona_virus)

    def run(self):

        # self.crawl_last_day_corona_virus()
        #
        # self.crawl_last_day_corona_virus_china()

        self.crawl_corona_virus()

        self.crawl_corona_virus_china()


if __name__ == '__main__':

    spider = CoronaVirusSpider()

    spider.run()


