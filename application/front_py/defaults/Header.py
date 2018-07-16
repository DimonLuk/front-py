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


class HeaderText(e._HeaderTextElement):
    """
    This is exactly <h1>, <h2> and etc. tag

    Parameters
    ----------

    level: int
        <h1>, <h2> an etc.
    text: string
        Text to be displayed as header
    """
    def __init__(self, level=1, text=""):
        super().__init__(level=level, text=text)


class Header(e._HeaderElement):
    """
    This is <header><h1></h1>, <h2></h2> and etc.</header>

    Parameters
    ----------

    level: int
        <h1>, <h2> and etc
    text: string
        text to be placed int header
    """
    def __init__(self, level=1, text=""):
        super().__init__()
        self.h = HeaderText(level, text)

    def _render(self):
        self.add_content(self.h)
        super()._render()





import unittest


class Test(unittest.TestCase):

    def test_HeaderText(self):
        self.assertEqual("""<h1 class="" style=""></h1>""", HeaderText().__str__())

    def test_Header(self):
        self.assertEqual("""<header class="" style=""><h1 class="" style=""></h1></header>""", Header().__str__())
