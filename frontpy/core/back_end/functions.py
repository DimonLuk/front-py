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
from Core_http_process import Core_http_process
from exceptions import *
from constants import *
from http.server import HTTPServer

def make_name(address):
    """
    Make unique name for function from request.path
    """
    address = address.split("/")
    address = "_aa".join(address)
    return address

def serve(address):
    """
    Function is used to put user definded function to the request handler
    """
    def decorator(fn,address=address):
        def decorated(address=address):
            address = make_name(address)
            setattr(Core_http_process,address,fn)
        decorated()
        return decorated
    return decorator

def run_app(address="localhost",server=HTTPServer,handler=Core_http_process,port=8000):
    server_address = (address,port)
    http = server(server_address,handler)
    print("""
Front-py  Copyright (C) 2018  Dima Lukashov <lds4ever2000@gmail.com>
This program comes with ABSOLUTELY NO WARRANTY; for details see LICENSE.md.
This is free software, and you are welcome to redistribute it
under certain conditions; For details see LICENSE.md.\n""")
    print("Started server at %s on port %s" % (address,port))
    http.serve_forever()

@serve("/%s"%BOOTSTRAP_CSS)
def je3202aea761d3d587dfcfc43c6982565(request):
    #createResponse(request,200,"text/css")
    with open("static/styles/bootstrap.css","r") as bootstrap:
        return (bootstrap.read(),"text/css")


@serve("/%s"%JQUERY_3_2_1_MIN_JS)
def j234c8514654bb7ed8a60ea905b6f98f0(request):
    with open("static/scripts/jquery-3.2.1.min.js","r") as jquery:
        return(jquery.read(),"script/javascript")


@serve("/%s"%BOOTSTRAP_MIN_JS)
def j13b2a30e265e18a6fd0792cc3fd7a09c(request):
    with open("static/scripts/bootstrap.min.js","r") as bootstrap:
        return(bootstrap.read(),"script/javascript")


@serve("/%s" % SCRIPT_JS)
def j9a9569e9d73f33740eada95275da7f30(request):
    with open("static/scripts/script.js","r") as script:
        return(script.read(),"script/javascript")
