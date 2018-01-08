"""
This is core module of application. It contains all exceptions types, CoreMeta and CoreElement which is the main feature of the framework
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
INVALID_INSERTION_MESSAGE = "You can't use '%s', please try some object from the framework library"
class InvalidInsertion(Exception):
    def __init__(self,message):
        super().__init__(message)
class EmptyWebPage(Exception):
    def __init__(self):
        super().__init__("You can't leave page empty, try to add some content with addElement method")
class UnlinkedElementsError(Exception):
    def __init__(self,message):
        super().__init__(message)
class MissingParametrError(Exception):
    def __init__(self,message):
        super().__init__(message)
class UnsupportedFeature(Exception):
    def __init__(self,message):
        super().__init__(message)
class CoreMeta(type):
    """
    This metaclass add special methods of replacing and cleaning after replacing elements.
    It's because simple '%s' usage is not comfortable
    """
    def __new__(cls,name,bases,dct):
        dct["_replace"] = _replace()
        dct["_clean"] = _clean()
        dct["_generateTrigger"] = _generateTrigger
        dct["_generateTarget"] = _generateTarget
        return super(CoreMeta,cls).__new__(cls,name,bases,dct)

class _replace:
    """
    This class presents special replacing method which is something like '%s' but more specific
    """
    def __call__(self,it,content,index):
        """
        'it' object that contains 'template' field where 'content' will be inserted in place of replacement expression which index is equals to 'index'
        """
        toRm = 0 #Position where the content to be inserted
        count = 0 #Shows which replacement expression has been found
        for i in range(len(it._template)):
            if it._template[i-2]=="|" and it._template[i-1] == "|" and it._template[i]=="|":#Finding replacment expr
                toRm = i-2
                if count == index:#If it's the required expression stop
                    break
                else:
                    count = count + 1
        if toRm != 0:#If we found sth
            it._template = it._template[:toRm] + content + "|||" + it._template[toRm+3:]
class _clean:
    """
    This class presents special cleaning method because replacement method leaves junk which is '|||'.
    """
    def __call__(self,it,index):
        """
        'it' is object that contains 'template' field and 'index' is the index of replacement expression to be removed
        """
        toRm = 0#Position in the 'template' where the replacement expremession to be removed
        count = 0#Shows current expression
        for i in range(len(it._template)): 
            if it._template[i-2] == "|" and it._template[i-1] == "|" and it._template[i]=="|":#Found some expression
                toRm = i-2#Remeber its position
                if count == index:#If it's the one is required
                    break
                else:
                    count = count +1
        if toRm != 0:#If sth has been found
            it._template = it._template[:toRm] + it._template[toRm+3:]

def _generateTrigger(self):
    """
    Generetaes classname for html element which will be trigger for some event
    """
    import datetime
    trigger = "%s" % datetime.datetime.now()
    trigger = trigger.split(" ")
    trigger = trigger[0].split("-") + trigger[1].split(".")
    trigger = trigger[0:3] + trigger[3].split(":") + trigger[4:]
    trigger = "".join(trigger) #All operations just remove all signs which is not numbers and creates one unique string
    return trigger
def _generateTarget(self,trigger):
    """
    Generates classname for html element which will be changed during the event
    """
    return trigger+"Target"
class WebPage(metaclass=CoreMeta):
    """
    It represents the html document with filename, title and encoding (Parametres may change)
    """
    def __init__(self,filename,title,encoding):
        self.filename = filename
        self.title = title
        self.encoding = encoding
        self._template = """
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
        <!DOCTYPE html>
        <html>
            <head>
                <title>|||</title>
                <meta charset="|||">
                <link rel="stylesheet" type="text/css" href="./../styles/bootstrap.css">
            </head>
            <body>
            <div class="global">
            |||
            </div>
            <script src="./../scripts/jquery-3.2.1.min.js"></script>
            <script src="./../scripts/bootstrap.min.js"></script>
            <script src="./../scripts/script.js"></script>
            </body>
        </html>
        """
        self._replace(self,self.title,0)#add title
        self._replace(self,self.encoding,1)#add encoding
        self._clean(self,0)#clean fileds to add
        self._clean(self,0)#clean filed to add
    def addElement(self,*content):
        self._content = content
        """
        Add any additional objects to body
        """
        for i in content:
            try:
                i._render() #remove replacement expression
                self._replace(self,i._template,0)
            except AttributeError:
                raise InvalidInsertion(INVALID_INSERTION_MESSAGE % i)
    def load(self):
        """
        Creats html file
        """
        try:
            for i in range(len(self._content)):
                self._clean(self,0)
        except AttributeError:
            raise EmptyWebPage()
        with open("pages/html/%s.html" % self.filename,"w") as file:
            file.write(self._template)

class CoreElement(metaclass=CoreMeta):
    """
    This class presents is used to build core elements which is simple html tags
    Private methods (user mustn't use this methods):
        _addStyle - to add css style to html element
        _addClass - to add class to html element
        _render - removes all replacement expression
        This list may be extended
    Private fields (user mustn't use this variables):
        _element - shows which html element to be created
        _isClosing - shows if the element has closing tag or not. True - has
        _isAddAttrs - shows if the method has to have attributes. True - has to
        _attributes - list or tuple of attributes that has to be added to the element
        _template - DOM representation of the object
    Public fields:
        addContent - adds any content into element if it's possible
    """
    def __init__(self,element,isClosing,isAddAttrs,attributes):
        self._element = element
        self._isClosing = isClosing
        self._attributes = attributes
        self._index = 0#Shows which attribute from _attributes is now in processing
        self._isAddAttrs = isAddAttrs
        self._indexesList = dict()#Dictionary which will contain {nameOfAttribute:indexToInsertContent}
        if self._isClosing:#If tag has to be closed
            self._template = """<%s|||>|||</%s>""" % (element,element)
        else:#If tag doesn't have to be closed
            self._template = """<%s|||>""" % element
        if self._isAddAttrs:
            for i in attributes:
                self._replace(self," "+i+'="|||"',self._index) #Add attribute
                self._indexesList[i] = self._index#Save the name of attribute and its index(for _replace method)
                self._index += 1
            self._clean(self,self._index)#And clean replacement expression which has been used to add attributes
            if self._isClosing:#If tag has to be closed then
                self._indexesList["content"] = self._index#It can have some content
        else:
            self._clean(self,self._index)#If no attributes just clean replacement expression for attributes
            if self._isClosing:
                self._indexesList["content"] = self._index#If tag has to be closed then save index for _replace method
    def _addStyle(self,styles):
        """
        Add style to html element
        styles - JSON like object which contains css properties like {"name":"value"}
        """
        self._styles = styles
        if "style" in self._indexesList:
            for i in self._styles:
                self._replace(self,"%s:%s; " % (i,self._styles[i]),self._indexesList["style"])
    def _addClass(self,*cls):
        """
        Add classes
        *cls - tuple of classes to be added
        """
        self._cls = cls#represents classes of html tag
        if "class" in self._indexesList:
            for i in self._cls:
                self._replace(self,"%s " % i,self._indexesList["class"])
    def _addAttrValue(self,attr,value):
        if attr in self._indexesList:
            self._replace(self,value,self._indexesList[attr])

                    
    def addContent(self,*content):
        """
        Add content which is str or any object that contains _template field
        """
        self._content = content#Represents content to be added to 'self' object
        for i in self._content:
            if type(i) is str:#If content is str
                if "content" in self._indexesList:#and it's field to add content
                    self._replace(self,i,self._indexesList["content"])
            else:#If content is some object
                if "content" in self._indexesList:
                    try:
                        import copy
                        cop = copy.deepcopy(i)#Deep copy because original object can be chenged later
                        cop._render()
                        self._replace(self,cop._template,self._indexesList["content"])
                    except AttributeError:
                        raise InvalidInsertion(INVALID_INSERTION_MESSAGE % i)
    def _render(self):
        """
        Preparing object to be used. REQURIED METHOD
        """
        for i in self._indexesList:#Clean all replacement expressions
            self._clean(self,0)
    def _linkElements(self,targets=[]):
        """
        Links number of elemnts to make them avaliable to add event. self is a trigger, other elements are targets
        """
        self._trigger = self._generateTrigger() #classname for tag which will emit the event
        self._target = self._generateTarget(self._trigger)#classname for tag which will be changed during the event
        if targets:
            for i in targets:
                try:#If sth not from framework has been passed
                    if "class" in i._indexesList:
                        i._replace(i, "%s " % self._target,i._indexesList["class"])
                    else:
                        raise MissingParametrError("Add attribute 'class' for html element %s" % i)
                except AttributeError:
                    raise InvalidInsertion(INVALID_INSERTION_MESSAGE % i)
        else:
            raise UnlinkedElementsError("You haven't linked any elements to create events between them")
        if "class" in self._indexesList:
            try:#Just for safety
                self._replace(self,"%s " % self._trigger,self._indexesList["class"])
            except AttributeError:
                raise InvalidInsertion(INVALID_INSERTION_MESSAGE % self)
        else:
            raise MissingParametrError("Add attribute 'class' for html element %s" % i)
    def _addScript(self,toDo):
        """
        Creates jquery interpritation of event for browsers
        """
        with open("./pages/scripts/script.js","a") as script:
            script.write(toDo)
    def onClick(self,toDo,targets=[],params={}):
        """
        Args:
        the first - some predefined word
        the second - elemetns which have to be involved as targets
        the third - dictionary with parametres if they are required
        """
        self._linkElements(targets)
        self._onClickParams = params
        if toDo == "changeColor":
            self._addScript(";(function(){var changed = false;var color = $('.%s').css('color');$('.%s').click(function(event){event.stopPropagation();if(changed){$('.%s').css({'color':color});changed = false;}else{$('.%s').css({'color':'%s'});changed = true;}});})();"%(self._target,self._trigger,self._target,self._target,self._onClickParams["color"]))
        else:
            raise UnsupportedFeature("'%s' event for click is unsupported, please write to author lds4ever2000@gmail.com" % toDo)






###############################################################
"""
Server Side
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
def makeName(address):
    address = address.split("/")
    address = "_aa".join(address)
    return address
class CoreHttpProcess(BaseHTTPRequestHandler):
    def __init__(self,a,b,c):
        super().__init__(a,b,c)
    def do_GET(self):
        self._sendResponse()
        self.name = makeName(self.path)
        try:
            self.wfile.write(bytes(self.__class__.__dict__[self.name]()._template.encode("utf-8")))
        except KeyError as kr:
            pass
    def _sendResponse(self):
        self.send_response(200)
        self._sendHeaders()
    def _sendHeaders(self):
        self.send_header("Content-type","text/html")
        self.end_headers()

def serve(address):
    def decorator(fn,address=address):
        def decorated(address=address):
            address = makeName(address)
            setattr(CoreHttpProcess,address,fn)
        decorated()
        return decorated
    return decorator
def runApp(server=HTTPServer,handler=CoreHttpProcess,port=8000):
    serverAddress = ("",port)
    http = server(serverAddress,handler)
    http.serve_forever()
