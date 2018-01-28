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

class Header_text(e._Header_text_element):
    def __init__(self,level=1,text=""):
        super().__init__(level=level,text=text)

class Header(e._Header_element):
    def __init__(self,level=1,text=""):
        super().__init__()
        self.h = Header_text(level,text)
    def _render(self):
        self.add_content(self.h)
        super()._render()
