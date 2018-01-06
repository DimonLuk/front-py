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
INVALID_INSERTION_MESSAGE = "You can't use '%s', please try some object from the framework library"
class InvalidInsertion(Exception):
    def __init__(self,message):
        super().__init__(message)
class EmptyWebPage(Exception):
    def __init__(self):
        super().__init__("You can't leave page empty, try to add some content with addElement method")


class CoreMeta(type):
    """
    This metaclass add special methods of replacing and cleaning after replacing elements.
    It's because simple '%s' usage is not comfortable
    """
    def __new__(cls,name,bases,dct):
        dct["_replace"] = _replace()
        dct["_clean"] = _clean()
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
    Inner methods (user mustn't use this methods):
        _addStyle - to add css style to html element
        _addClass - to add class to html element
        This list may be extended
    Inner fields (user mustn't use this variables):
        _element - shows which html element to be created
        _isClosing - shows if the element has closing tag or not. True - has
        _isAddAttrs - shows if the method has to have attributes. True - has to
        _attributes - list or tuple of attributes that has to be added to the element
        _template
        Threre are fields that has been listed in the __init__ method
        Other service fields are described in class
    Public methods (which user can use):
        render - removes all replacement expression
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
        self._cls = cls
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
        self._content = content
        for i in self._content:
            if type(i) is str:#If content is str
                if "content" in self._indexesList:#and it's field to add content
                    self._replace(self,i,self._indexesList["content"])
            else:#If content is some object
                if "content" in self._indexesList:
                    try:
                        self._replace(self,i._template,self._indexesList["content"])
                    except AttributeError:
                        raise InvalidInsertion(INVALID_INSERTION_MESSAGE % i)
    def render(self):
        """
        Preparing object to be used. REQURIED METHOD
        """
        for i in self._indexesList:#Clean all replacement expressions
            self._clean(self,0)
