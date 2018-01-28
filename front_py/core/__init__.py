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
import sys
from __custom_import__ import prepare_import
prepare_import("front_end","back_end")
from back_end import *
from front_end import *
from exceptions import *
