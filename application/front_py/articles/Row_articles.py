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
from rows import Section_row
from Article import Article


class Row_articles(Section_row):
    """Creates a lot of articles. Each article in one single row

    The first argument is title of all articles| not required
    The second is position, now only center or nothing allowed| not required

    Use 'config' method to set your preferences for all articles
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
            header = e._Header_element()
            if position == "center":
                header._add_class("mx-auto")
            h = e._Header_text_element(1, self.section_title)
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
        Adds single artile with header, text, and footer. All arguments are not required and can be objects
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
            article.add_content(e._Horizontal_line_element())

        if self.horizontal_distance:
            article._add_style({"margin-top": self.horizontal_distance})

        self.articles.append(article)

    def _render(self):
        self.add_content(*self.articles)
        super()._render()

    def __call__(self, header_text="", text="", footer=""):
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
