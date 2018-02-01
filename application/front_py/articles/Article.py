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


class Article(e._Article_element):
    def __init__(self, header_text="", headers_level=1, paragraph="",
                 footer="", column_num=4, responsive=True, save_format=False,
                 is_code=False, lang="", background={}):
        super().__init__()
        self.checker = False
        self.save_format = save_format
        self.is_code = is_code
        if self.save_format and self.is_code:
            self.paragraph = e._Code_element()
            self.paragraph._add_class(lang)
        else:
            self.paragraph = e._Paragraph_element()
        if background:
            self.paragraph._add_style(background)
        self.text = paragraph
        self.header_text = header_text
        self.footer = footer
        self.column_num = column_num
        self.responsive = responsive
        self.headers_level = headers_level
        self._add_class("col-lg-%s" % str(column_num))
        if self.responsive:
            self._add_class("col-12")
        if self.header_text:
            self.header = e._Header_element()

            self.h = e._Header_text_element(headers_level)
            self.h.add_content(header_text)

            self.header.add_content(self.h)
        if self.text:
            self.paragraph.add_content(self.text)

    def add_content(self, *content):
        self.checker = True
        self.paragraph.add_content(*content)

    def _render(self):
        if self.save_format and self.is_code:
            tmp = e._Formated_text_element()
            tmp.add_content(self.paragraph)
            self.paragraph = tmp
        if self.header_text:
            super().add_content(self.header)
        if self.text or self.checker:
            super().add_content(self.paragraph)
        if self.footer:
            super().add_content(self.footer)
        super()._render()

    def __call__(self, header_text="", text="", footer=""):
        obj = Article(
            header_text=header_text,
            headers_level=self.headers_level,
            paragraph=text,
            footer=footer,
            column_num=self.column_num,
            responsive=self.responsive)
        return obj
