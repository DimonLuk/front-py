"""
Copyright (C) 2018  Dima Lukashov github.com/DimonLuk

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from core import elements as e
from rows import SectionRow
from Article import Article


class RowArticles(SectionRow):
    """
    Parameters
    ----------

    section_title: string
        how your block of articles will be called
    position: special string
        center, left or right
    horizontal_distance: special string for example 30px
        distance between each article
    horizontal_line: bool
        if it is necessary to underscore all articles
    headers_level: int
        how big header of each article has to be
    save_format: bool
        indicates if the formatting from source string has to be saved
    is_code: bool
        indicates if it's code
    lang: string
        language for codding for example python, javascript and etc.
    articles_background: json_object with css properties
        json object with css properties
    """

    def __init__(
            self, section_title="", position="center", horizontal_distance="",
            horizontal_line=False, headers_level=2, save_format=False,
            is_code=False, lang="", articles_background={},
            *articles):
        super().__init__()
        self.save_format = save_format
        self.is_code = is_code
        self.articles_background = articles_background
        self.articles = []  # Array with all articles
        if section_title:
            self.section_title = section_title
            header = e._HeaderElement()
            if position == "center":
                header._add_class("mx-auto")
            h = e._HeaderTextElement(1, self.section_title)
            header.add_content(h)
            self.add_content(header)
        self.horizontal_line = horizontal_line
        self.horizontal_distance = horizontal_distance
        self.headers_level = headers_level
        if articles:
            for i in articles:
                self.articles.append(i)

    def add_article(self, header_text="", text="", footer="",
                    save_format=False, is_code=False, lang="", background={}):
        """
        Parameters
        ----------

        header_text: string
            header of single article
        text: string
            text of article
        footer: string
            footer of article
        save_format: bool
            save source string formatting
        is_code: bool
            if it's some program code
        lang: string
            programming language
        background: json object with css properties
        """
        article = Article(
            header_text=header_text,
            paragraph=text,
            footer=footer,
            headers_level=self.headers_level,
            column_num=12,
            save_format=save_format,
            is_code=is_code,
            lang=lang,
            background=background)
        if self.horizontal_line:
            article.add_content(e._HorizontalLineElement())

        if self.horizontal_distance:
            article._add_style({"margin-top": self.horizontal_distance})

        self.articles.append(article)

    def _render(self):
        self.add_content(*self.articles)
        super()._render()

    def __call__(self, header_text="", text="", footer=""):
        """
        Create new article and wrap it into existing context and modify this contextual object

        Returns
        ----------
        new article wraped into existing object
        """
        self.add_article(
            header_text=header_text,
            text=text,
            footer=footer,
            save_format=self.save_format,
            is_code=self.is_code,
            background=self.articles_background)
        return self

    def __iter__(self):
        for i in self.articles:
            yield i










import unittest


class Test(unittest.TestCase):

    def test_RowArticles(self):
        self.assertEqual("""<section class="container " style=""><div class="row " style=""></div></section>""", RowArticles().__str__())

    def test_RowArticles_add_article(self):
        a = RowArticles()
        a.add_article("Test")
        self.assertEqual("""<section class="container " style=""><div class="row " style=""><article class="col-lg-12 col-12 " style=""><header class="" style=""><h2 class="" style="">Test</h2></header></article></div></section>""", a.__str__())

    def test_RowArticles__call__(self):
        a = RowArticles()
        self.assertEqual("""<section class="container " style=""><div class="row " style=""><article class="col-lg-12 col-12 " style=""><header class="" style=""><h2 class="" style="">Test</h2></header><p class="" style=""><section class="container " style=""><div class="row " style=""></div></section></p></article></div></section>""", a("Test", a).__str__())

    def test_RowArticle__iter__(self):
        a = RowArticles()
        a.add_article("a")
        a.add_article("b")
        results = ("""<article class="col-lg-12 col-12 " style=""><header class="" style=""><h2 class="" style="">a</h2></header></article>""",
                   """<article class="col-lg-12 col-12 " style=""><header class="" style=""><h2 class="" style="">b</h2></header></article>""")
        k = 0
        for i in a:
            self.assertEqual(results[k], i.__str__())
            k += 1
