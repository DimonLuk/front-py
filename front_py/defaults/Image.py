"""
This is core module of application. It contains all exceptions types, Core_meta and Core_element which is the main feature of the framework
which makes it possible to build html tags in python objects.


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

class Image(e._Link_element):
    """
    Simple responsive image
    """
    def __init__(self,href,alt="picture",columns=6):
        super().__init__(href)
        self.image = e._Image_element(src=href,alt=alt)
        self.image._add_style({"width":"100%"})
        self._add_class("col-%s"%str(columns))
        self.add_content(self.image)
