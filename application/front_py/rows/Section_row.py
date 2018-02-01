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
from containers import Section_container
from Block_row import Block_row


class Section_row(Section_container):
    """
    Creates a row inside Section_container
    """

    def __init__(self):
        super().__init__()
        self.row = Block_row()

    def add_content(self, *content):
        self.row.add_content(*content)

    def _render(self):
        super().add_content(self.row)
        super()._render()
