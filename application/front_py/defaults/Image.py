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


class Image(e._LinkElement):
    """
    Parameters
    ----------

    href: string
        it's name of image that is placed within static/ folder
    alt: string
        alternative text for people who can't see the picture itself
    columns: int
        how many of 12 columns the picture will take
    """

    def __init__(self, href, alt="picture", columns=6):
        super().__init__(href)
        self.image = e._ImageElement(src=href, alt=alt)
        self.image._add_style({"width": "100%"})
        self._add_class("col-%s" % str(columns))
        self.add_content(self.image)





import unittest


class Test(unittest.TestCase):

    def test_Image(self):
        self.assertEqual("""<a class="col-6 " style="" href=""><img class="" style="width:100%; " src="" alt="picture" /></a>""", Image("").__str__())
