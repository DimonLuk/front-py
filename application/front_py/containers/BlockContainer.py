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


class BlockContainer(e._BlockElement):
    """
    Is used to build complex structures, sometimes can be useful for user, so no '_' in the begining of name
    """

    def __init__(self):
        super().__init__()
        self._add_class("container")






import unittest


class Test(unittest.TestCase):

    def test_BlockContainer(self):
        self.assertEqual("""<div class="container " style=""></div>""", BlockContainer().__str__())
