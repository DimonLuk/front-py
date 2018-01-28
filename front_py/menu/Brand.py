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

class Brand_text(e._Link_element):
    """
    Company name or other brand short and nice info

    The first argument is text
    The second is color
    """
    def __init__(self,text="",color="#ffffff"):
        super().__init__(href="")
        self.color = color
        self.text = text
        self._add_class("navbar-brand")
        self._add_style({"color":self.color})
        self._add_attr_value("href","#")
        self.add_content(self.text)

class Brand_image(Brand_text):
    """
    Company logo
    The firts arg is name of the picture which is inside the media folder of the project
    The second is text to be displayed if picture can't be loaded
    """
    def __init__(self,imageName,alt):
        super().__init__()
        self.img = e._Image_element(imageName,alt)
        self.add_content(self.img)