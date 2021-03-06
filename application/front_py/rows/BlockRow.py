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


class BlockRow(e._BlockElement):
    """
    Simple row
    """

    def __init__(self, *content):
        super().__init__()
        self._add_class("row")
        self.add_content(*content)






import unittest


class Test(unittest.TestCase):

    def test_BlocRow(self):
        self.assertEqual("""<div class="row " style=""></div>""", BlockRow().__str__())