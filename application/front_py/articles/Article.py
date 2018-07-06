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
    """
    Dervied from e._Article_element. Used for displaying text, image and video
    information as a single article.
    Constructor arguments: header_text, headers_level, paragraph, footer,
    column_num, responsive, save_format, is_code, lang, background.

    header_text: string or framework object, default: ""
        - text that acts as a header of an article
    headers_level: int, default: 1
        - display how deep this header is used to bring
        some semantic to the webpage
    parapgraph: string or framework object, default:""
        - text of paragraph (can include images and videos) to be displayed
    column_num: int, default: 4
        - shows how many of 12 columns this paragraph has to take
    responsive: boolean, default: True
        -shows if this paragraph has to be responsive
    save_format: boolean, default: False
        - shows if the text has to be displayed in default html format
        or use exact formating that is hardcoded
    is_code: boolean, defualt: False
        - shows if the text is a source code of some programming language
    lang: string, default: ""
            - determines which programming language this text is
    """
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
            self.paragraph._add_class("j"+str(hex(hash(self.paragraph))))
            self.paragraph.add_content("<script>$('.%s').each(function(i, block) {hljs.highlightBlock(block);});</script>" % ("j"+str(hex(hash(self.paragraph)))))
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
        """
        Adds content to the article's paragraph
        Arguments: *content.
        *content: any number of strings or frameworks objects(can be mixed)
            - content to be added and to be displayed
        """
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
