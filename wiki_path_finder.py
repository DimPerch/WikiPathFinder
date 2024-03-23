import requests
from bs4 import BeautifulSoup as bs
import re
from urllib.parse import unquote


class WikiPathFinder:
    def __init__(self, source, target) -> None:
        """
        The WikiPathFinder class is responsible for finding the WikiPath from a source and target URL
        :param source: urllike object of the source
        :param target: urllike object of the target
        """
        print("WikiPathFinder\n"
              "source: " + source + "\n"
              "target: " + target)
        self.source = source
        self.target = target
        self.visited = []
        self.is_run = True

    @staticmethod
    def _get_page(link) -> [str, None]:
        """
        Gets a page from wikipedia using requests library
        :param link:
        :return: str
        """
        response = requests.get(link)
        if response.status_code == 200:
            return response.text

    @staticmethod
    def _get_text_without_brackets(text: str) -> str:
        """
        Removes the brackets from a text and return the text without the brackets
        :param text: str
        :return: str
        """
        n = 1
        while n:
            text, n = re.subn(r'\([^()]*\)', '', text)
        return text

    @staticmethod
    def _get_links_from_page(soup) -> map:
        """
        Gets a list of links from wikipedia using requests library and returns a list of links
        :param soup: bs4 object
        :return: map object
        """
        data = soup.find_all("a", {"class": "",
                                   "accesskey": ""},
                             href=re.compile(r"^/wiki/[^:]+$"))
        data = filter(lambda tag: tag.parent.name == "p", data)
        data = map(lambda tag: "https://ru.wikipedia.org" + tag["href"], data)
        return data

    @staticmethod
    def _get_title_from_page(soup) -> [str, None]:
        """
        Gets a title from wikipedia page
        :param soup: bs4 object
        :return: str
        """
        title = soup.find_all("span", {"class": "mw-page-title-main"})
        if title:
            return title[0].text

    def _find(self, link) -> None:
        """
        Recursively finds the path from source to target page
        :param link: str
        :return: None
        """
        if unquote(link) == self.target:
            print("Target link found")
            self.is_run = False
        elif self.is_run:
            text = self._get_page(link)
            text = self._get_text_without_brackets(text)
            soup = bs(text, "html.parser")
            links = self._get_links_from_page(soup)
            print(self._get_title_from_page(soup))
            for index, next_link in enumerate(links):
                if next_link not in self.visited:
                    self.visited.append(next_link)
                    self._find(next_link)
                else:
                    continue

    def find(self) -> None:
        """
        Finds the path from source to target page
        :return: None
        """
        self._find(self.source)

