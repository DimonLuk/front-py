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


class Invalid_insertion(Exception):
    def __init__(self, message):
        super().__init__(message)


class Empty_web_page(Exception):
    def __init__(self):
        super().__init__("You can't leave page empty, try to add some content with add_element method")


class Unlinked_elements_error(Exception):
    def __init__(self, message):
        super().__init__(message)


class Missing_parameter_error(Exception):
    def __init__(self, message):
        super().__init__(message)


class Unsupported_feature(Exception):
    def __init__(self, message):
        super().__init__(message)
