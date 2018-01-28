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
from __custom_import__ import prepare_import
prepare_import()
from constants import *
from Core_element import Core_element


class Page(Core_element):
    def __init__(self,title,encoding,background={}):
        self._mimetype = "text/html"
        self.title = title
        self.encoding = encoding
        super().__init__("div",True,True,["class","style"])
        self._add_class("global")
        if background:
            self._add_style(background)
        self._tmp = """
<!DOCTYPE html>
<!--
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
-->
<html>
        <head>             
        <title>%s</title>
        <meta charset="%s">
        <base href="/">
        <link rel="icon" href="favicon.ico" type="image/x-icon"/>
        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon"/>
        <link rel="stylesheet" type="text/css" href="%s">
    </head>            
    <body style="margin-top:-16px;">
            %s
        <script src="%s"></script>
        <script src="%s"></script>
        <script src="%s"></script>
        <script>hljs.initHighlightingOnLoad();</script>
    </body>
</html>
        """
    def add_element(self,*content):
        for i in content:
            self.add_content(i)
    def set_titile(self,title):
        self.title = title
    def set_background(self,background):
        self._add_style(background)
    def _render(self):
        self._template = self._tmp % (self.title,self.encoding,BOOTSTRAP_CSS,self._template,JQUERY_3_2_1_MIN_JS,BOOTSTRAP_MIN_JS,SCRIPT_JS)
        super()._render()
