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
from containers import SectionContainer
from rows import BlockRow
from defaults import Header


class ColumnArticles(SectionContainer):
    def __init__(
            self, header="", footer="", headers_level=1, position="",
            vertical_distance="30px", horizontal_line=False, *articles):
        """
        Parameters
        ----------
        header: string or framework object
            text or object which represents header of article
        footer: string or framework object
            text or object which represents footer of article
        headers_level: int
            can be int from 1 to 7 like in html
        position: special string
            string which is center, left or right
        vertical_distance: string which looks like int + px, for example 30px
            I do not remember certainly what is it, need to experiment )))
        horizontal_line: bool
            line which will underscore all articles
        articles: several of Article
            I suppose it is simple
        """
        super().__init__()
        self.header = header
        self.headers_level = headers_level
        self.line = horizontal_line
        self.footer = footer
        self.row_header = BlockRow()

        self.head = Header(self.headers_level, header)
        if position == "center":
            self.head._add_class("mx-auto")
        self.row_header.add_content(self.head)
        if vertical_distance:
            self.row_header._add_style({"margin-bottom": vertical_distance})
        super().add_content(self.row_header)

        self.rowArticles = BlockRow()
        if articles:
            self.rowArticles.add_content(*articles)

    def add_content(self, *content):
        self.rowArticles.add_content(*content)

    def _render(self):
        super().add_content(self.rowArticles)
        if self.footer:
            super().add_content(self.footer)
        if self.line:
            super().add_content(e._HorizontalLineElement())
        super()._render()

    def __call__(self, *articles):
        for i in articles:
            self.add_content(i)










import unittest


class Test(unittest.TestCase):
    def test_ColumnArticles(self):
        self.assertEqual("""<section class="container " style=""><div class="row " style="margin-bottom:30px; "><header class="" style=""><h1 class="" style=""></h1></header></div><div class="row " style=""></div></section>""", ColumnArticles().__str__())

    def test_ColumnArticles_add_content(self):
        a = ColumnArticles()
        a.add_content("Test", a)
        self.maxDiff = None
        self.assertEqual("""<section class="container " style=""><div class="row " style="margin-bottom:30px; "><header class="" style=""><h1 class="" style=""></h1></header></div><div class="row " style="">Test<section class="container " style=""><div class="row " style="margin-bottom:30px; "><header class="" style=""><h1 class="" style=""></h1></header></div><div class="row " style="">Test</div></section></div></section>""", a.__str__())
