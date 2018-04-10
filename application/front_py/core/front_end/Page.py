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
from constants import *
from Core_element import Core_element


class Page(Core_element):
    """!
    @brief Derived from Core_element but it's special element,
    which has additional html code.
    @param title: string
    - title of the page will be displayed at the tab of browser,
    for example if you pass into this argument "Your title" it will
    result as <title>Your title</title> in html inside <head></head>.
    @param encoding: string, default: "utf-8"
    - sets the encoding of the page, default it's utf-8.
    @parambackground: object
    - JSON object with css3 rules to define background
    of all page, for example
    @code{"background-color":"#abcdef"}@endcode
    """

    def __init__(self, title, url="/",encoding="utf-8", background={}):
        # Mimetype of page
        self._mimetype = "text/html"
        self.url = url

        # _title is the value inside
        # @code<title></title>@endcode tag
        self._title = title

        # encoding is the encdoing of the page
        # default: utf-8
        self.encoding = encoding

        super().__init__("div", True, True, ["class", "style"])
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
        <script src="%s"></script>
    </head>
    <body style="margin-top:-16px;">
            %s
        <script src="%s"></script>
        <script src="%s"></script>
        <script>hljs.initHighlightingOnLoad();</script>
    </body>
</html>"""

    def add_element(self, *content):
        """!
        @brief Adds element to page, elements can be both objects derived from Core_element and strings.
        @param *content: objects from the framework
        - content to be placed to the page.
        """
        for i in content:
            self.add_content(i)

    def set_title(self, title):
        """!
        @brief Changes previous title of the page.
        @param title: string
        - title of the page will be displayed at the tab of browser,
        for example if you pass into this argument "Your title" it will
        result as <title>Your title</title> in html inside <head></head>.
        """
        self._title = title

    def set_background(self, background):
        """!
        @brief Changes previous background of the page.
        @param background: object
        - JSON object with css3 rules to define background of all page,
        for example
        @code{"background-color":"#abcdef"}@endcode
        """
        self._add_style(background)

    def _render(self):
        """!
        @brief inherited from Core_element#_render
        """

        # Inherited from Core_element#_template
        self._template = self._tmp % (
            self._title, self.encoding, BOOTSTRAP_CSS, JQUERY_3_2_1_MIN_JS,
            self._template, BOOTSTRAP_MIN_JS, SCRIPT_JS)
        super()._render()

    def __setattr__(self, name, value):
        """!
        @details You can change title and background in this way:
        @code
        page.title = "Another title"
        page.background = {"background-image":"url(image_name.image_format)"}.
        @endcode
        To add image just place it into media folder of your project
        that by default has this path:
        (suppose you're in the folder where app.py is placed)
        @code application/static/media @endcode
        """
        if name == "background":
            self.set_background(value)
        elif name == "title":
            self.set_title(value)
        else:
            self.__dict__[name] = value


import unittest


class Test(unittest.TestCase):
    def __init__(self, a):
        super().__init__(a)
        self.test1 = Page("%s", "%s")

    def test_constructor(self):
        self.maxDiff = None
        self.assertEqual("""
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
        <link rel="stylesheet" type="text/css" href="e3202aea761d3d587dfcfc43c6982565">
    </head>
    <body style="margin-top:-16px;">
            <div class="global " style=""></div>
        <script src="234c8514654bb7ed8a60ea905b6f98f0"></script>
        <script src="13b2a30e265e18a6fd0792cc3fd7a09c"></script>
        <script src="9a9569e9d73f33740eada95275da7f30"></script>
        <script>hljs.initHighlightingOnLoad();</script>
    </body>
</html>""", self.test1.__str__())

    def test_add_element(self):
        from elements import _TEST
        for i in _TEST:
            self.test1.add_element(i())
        self.maxDiff = None
        self.assertEqual("""
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
        <link rel="stylesheet" type="text/css" href="e3202aea761d3d587dfcfc43c6982565">
    </head>
    <body style="margin-top:-16px;">
            <div class="global " style=""><span class="" style=""></span><p class="" style=""></p><menu class="" style=""></menu><nav class="" style=""></nav><ul class="" style=""></ul><ol class="" style=""></ol><li class="" style=""></li><a class="" style="" href="#"></a><img class="" style="" src="#" alt="image"><div class="" style=""></div><section class="" style=""></section><aside class="" style=""></aside><footer class="" style=""></footer><form class="" style="" method="POST" name=""></form><input class="" style="" type="text" placeholder="Placeholder"><button class="" style="" type="">Button</button><header class="" style=""></header><textarea class="" style="" placeholder="Placeholder"></textarea><h1 class="" style=""></h1><hr><pre class="" style=""></pre><code class="" style=""></code><article class="" style=""></article></div>
        <script src="234c8514654bb7ed8a60ea905b6f98f0"></script>
        <script src="13b2a30e265e18a6fd0792cc3fd7a09c"></script>
        <script src="9a9569e9d73f33740eada95275da7f30"></script>
        <script>hljs.initHighlightingOnLoad();</script>
    </body>
</html>""", self.test1.__str__())

    def test_set_background(self):
        self.test1.set_background({"color": "test"})
        self.assertEqual("""
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
        <link rel="stylesheet" type="text/css" href="e3202aea761d3d587dfcfc43c6982565">
    </head>
    <body style="margin-top:-16px;">
            <div class="global " style="color:test; "></div>
        <script src="234c8514654bb7ed8a60ea905b6f98f0"></script>
        <script src="13b2a30e265e18a6fd0792cc3fd7a09c"></script>
        <script src="9a9569e9d73f33740eada95275da7f30"></script>
        <script>hljs.initHighlightingOnLoad();</script>
    </body>
</html>""", self.test1.__str__())

    def test_set_title(self):
        self.test1.set_title("TEST")
        self.assertEqual("""
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
        <title>TEST</title>
        <meta charset="%s">
        <base href="/">
        <link rel="icon" href="favicon.ico" type="image/x-icon"/>
        <link rel="shortcut icon" href="favicon.ico" type="image/x-icon"/>
        <link rel="stylesheet" type="text/css" href="e3202aea761d3d587dfcfc43c6982565">
    </head>
    <body style="margin-top:-16px;">
            <div class="global " style=""></div>
        <script src="234c8514654bb7ed8a60ea905b6f98f0"></script>
        <script src="13b2a30e265e18a6fd0792cc3fd7a09c"></script>
        <script src="9a9569e9d73f33740eada95275da7f30"></script>
        <script>hljs.initHighlightingOnLoad();</script>
    </body>
</html>""", self.test1.__str__())
