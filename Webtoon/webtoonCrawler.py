# -*- coding: utf-8 -*-

import os
import urllib
import urllib2
import cStringIO
from urlparse import urlparse, parse_qs
from bs4 import BeautifulSoup
from PIL import Image

WEBTOON_ID = 20853
miss_count = 0


def run():
    for i in xrange(1, 10000):
        crawl(WEBTOON_ID, i)


def crawl(webtoon_id, no):
    url = get_url(webtoon_id, no)
    markup = get_markup(url)
    global miss_count
    if markup:
        webtoon = ParsedMarkup(markup)
        webtoon_images = get_webtoon_images(webtoon.get_image_url_list())
        webtoon_name = webtoon.get_webtoon_name()
        webtoon_title = webtoon.get_webtoon_title()

        make_directory_if_not_exist(webtoon_name)
        default_path = os.path.join(webtoon_name, str(no).zfill(5) + "." + webtoon_title)

        if len(webtoon_images) == 1:
            path = default_path + ".jpg"
            webtoon_images[0].save(path)
            print path
        else:
            for i in xrange(len(webtoon_images)):
                path = default_path + "[" + str(i) + "]" + ".jpg"
                webtoon_images[i].save(path)
                print path

        miss_count = 0
    else:
        miss_count += 1
        print "해당 회차의 웹툰이 존재하지 않습니다."
        if miss_count >= 3:
            exit(0)


class ParsedMarkup:
    def __init__(self, markup):
        self.soup = BeautifulSoup(markup, "lxml")
        self.image_html_list = self.soup.select('.wt_viewer img')
        self.name_markup = str(
            self.soup.select_one("#content > div.section_cont.wide > div.comicinfo > div.detail > h2"))
        self.title_markup = self.soup.select_one("#content > div.section_cont.wide > div.tit_area > div.view > h3")

    def get_image_url_list(self):
        image_url_list = []
        for image_html in self.image_html_list:
            image_url_list.append(image_html["src"])
        return image_url_list

    def get_webtoon_name(self):
        return BeautifulSoup("".join(self.name_markup), "lxml").h2.contents[0].strip()

    def get_webtoon_title(self):
        return BeautifulSoup("".join(self.title_markup), "lxml").p.text.strip()


def get_url(title_id, no):
    domain = "http://comic.naver.com/webtoon/detail.nhn?"
    param = {"titleId": title_id, "no": no}
    return domain + urllib.urlencode(param)


def get_markup(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    response_url = response.geturl()
    if is_exist_webtoon(url, response_url):
        return response.read()
    else:
        return None


def is_exist_webtoon(origin_url, response_url):
    parsed_origin_url = urlparse(origin_url)
    parsed_response_url = urlparse(response_url)
    return parse_qs(parsed_response_url.query)["no"] == parse_qs(parsed_origin_url.query)["no"]


def get_image_from_url(url):
    request = urllib2.Request(url)
    request.add_header("Referer", "http://comic.naver.com")
    response = urllib2.urlopen(request)
    image_file = cStringIO.StringIO(response.read())
    return Image.open(image_file)


def get_merge_vertical_images(image_list, limit_height):
    start_image_idx = 0
    images = []

    x = image_list[0].size[0]
    y = 0

    for image in image_list:
        y += image.size[1]
        if y > limit_height:
            end_image_index = image_list.index(image)
            images.append(create_image(image_list[start_image_idx: end_image_index], (x, y - image.size[1])))
            y = image.size[1]
            start_image_idx = end_image_index

    images.append(create_image(image_list[start_image_idx:], (x, y)))
    return images


def create_image(image_list, image_size):
    new_image = Image.new("RGB", image_size, (256, 256, 256))
    position_y = 0
    for image in image_list:
        new_image.paste(image, (0, position_y))
        position_y += image.size[1]
    return new_image


def get_image_size_vertical(image_list):
    x = image_list[0].size[0]
    y = 0
    for image in image_list:
        y += image.size[1]
    return x, y


# 65500 보다 큰 이미지 생성 불가.
def get_webtoon_images(url_list, limit_height=60000):
    image_list = []
    for url in url_list:
        image_list.append(get_image_from_url(url))

    return get_merge_vertical_images(image_list, limit_height)


def make_directory_if_not_exist(path):
    if not os.path.isdir(path) and not os.path.exists(path):
        os.makedirs(path)


run()
