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
from exceptions import *
from constants import *
from http.server import HTTPServer
from back_end import Core_http_process


def make_name(address):
    """Creates special name which will be added to Core_http_process attributes.
    Because names are built from http requests they contain '/', this function repleces it with '_aa'.
    !!!Not imported to front_py package. Not for user usage!!!

    Parameters
    ----------
    address: string
        url of http request.
    """
    address = address.split("/")
    address = "_aa".join(address)
    return address


def serve(address):
    """Binds function to url which has to be served.

    Parameters
    ----------
    address: string
        request itself, for example, if you want to serve
        "http://localhost:8000/test" you have to pass only "/test".

    Usage: as decorator for function that will create some response
    """
    def decorator(fn, address=address):
        def decorated(address=address):
            address = make_name(address)
            setattr(Core_http_process, address, fn)
        decorated()
        return decorated
    return decorator


def run_app(address="localhost", server=HTTPServer,
            handler=Core_http_process, port=8000):
    """Runs the server and application.

    Parameters
    ----------
    address: string, default: "localhost"
        ip address to be served, default is 'localhost'.
    server: class extends HTTPServer
        server class which will serve the application, default is HTTPServer.
    handler: class extends Core_http_process
        class that will handle requests, default is Core_http_process.
    port: int, default: 8000
        port to be served, default is 8000
    """
    server_address = (address, port)
    http = server(server_address, handler)
    print("""
Front-py  Copyright (C) 2018  Dima Lukashov <lds4ever2000@gmail.com>
This program comes with ABSOLUTELY NO WARRANTY; for details see LICENSE.md.
This is free software, and you are welcome to redistribute it
under certain conditions; For details see LICENSE.md.\n""")
    print("Started server at %s on port %s" % (address, port))
    http.serve_forever()


"""
There are some functions which names are hashes.
They are used to load scripts and styles, one of them is used for unittests
"""


@serve("/%s" % BOOTSTRAP_CSS)
def je3202aea761d3d587dfcfc43c6982565(request):
    # createResponse(request,200,"text/css")
    with open("application/static/styles/bootstrap.css", "r") as bootstrap:
        return (bootstrap.read(), "text/css")


@serve("/%s" % JQUERY_3_2_1_MIN_JS)
def j234c8514654bb7ed8a60ea905b6f98f0(request):
    with open("application/static/scripts/jquery-3.2.1.min.js", "r") as jquery:
        return(jquery.read(), "script/javascript")


@serve("/%s" % BOOTSTRAP_MIN_JS)
def j13b2a30e265e18a6fd0792cc3fd7a09c(request):
    with open("application/static/scripts/bootstrap.min.js", "r") as bootstrap:
        return(bootstrap.read(), "script/javascript")


@serve("/%s" % SCRIPT_JS)
def j9a9569e9d73f33740eada95275da7f30(request):
    with open("application/static/scripts/script.js", "r") as script:
        return(script.read(), "script/javascript")


# For test purposes
@serve("/041bf0b5619389a866f6fff4a1556401cec9dced44b5e78cfbf0eda24ff8787e")
def j041bf0b5619389a866f6fff4a1556401cec9dced44b5e78cfbf0eda24ff8787e(request):
    return (
        "041bf0b5619389a866f6fff4a1556401cec9dced44b5e78cfbf0eda24ff8787e", "text/html")


import unittest
from threading import Thread
import urllib.request


class Test(unittest.TestCase):
    def test_serve_and_Core_http_process(self):
        server_thread = Thread(
            target=run_app, kwargs={
                "address": "localhost", "port": 8000})
        server_thread.start()
        result = urllib.request.urlopen(
            "http://localhost:8000/041bf0b5619389a866f6fff4a1556401cec9dced44b5e78cfbf0eda24ff8787e")
        self.assertEqual(
            b"041bf0b5619389a866f6fff4a1556401cec9dced44b5e78cfbf0eda24ff8787e",
            result.read())

    def test_make_name(self):
        self.assertEqual(
            "_aatest_aatest_aa041bf0b5619389a866f6fff4a1556401cec9dced44b5e78cfbf0eda24ff8787e",
            make_name(
                "/test/test/041bf0b5619389a866f6fff4a1556401cec9dced44b5e78cfbf0eda24ff8787e"))
