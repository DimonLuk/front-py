"""
I think that the best tutorial is the life example
The result of this tutorial you can see at the website
So you may find everything which has been done in this file
String by string you'll learn more and more about building applications with Fornt-py
So, let's start
It'll be a lot, A LOT of text here :))))))
"""
#To add your favicon.ico just put it in pages/media/ folder
from frontpy.frontpy import * #All necessary imports are here, you can watch this file if it's interesting to you to know how it works

#This block is used to create one theme for all pages
#It's easier to store this values in variables because changing one thing here will change everything in the website
backgroundColor = "#dddddd" #Grey color of the pages
brandColor = "red" #Nice red color of some text
brandText = Text() #Wrapping object that will be used below
brandText.color = brandColor #Some objects can be cinfigured in this way. To be honest all objects will have opportunity to be configured in such way but a bit later
pageParams = tuple(["utf-8",{"background":backgroundColor}]) #Some meta information about page. Encoding and background color.
#But you can set any background settings you want, using css properties
menu = InlineMenu({"background":"black"},{"Home":"/", "Objectives":"/objectives","User guide":"/userGuide","Tester guide":"/testerGuide","Developer guide":"/developerGuide"},"white",BrandText("Front-py",brandColor)) #This is menu.
foot = Text("&copy DimonLuk") #Content you want to be displayed can be passed as the last argument of the constructor
foot.position = "center"#Another settings
foot.color = "white"
footer = Footer(foot)#You can use objects from framework to build other objects of framework
footer.backgroundColor = "black"

@serve("/")#This says that the function bellow will handle requests from main page of the website wich address is address.com/ or without "/"
def index(request):#Each function has to take one parameter which is the request. Now request contains only method field
    if request.method == "GET":#So let's check the method which browser used. No only GET can be handled
        #We habe to create a content for page
        articles = RowArticles("Three facts about %s 0.0.1(pre-alpha)" % brandText("Front-py"),horizontalLine=True,headersLevel=2,horizontalDistance="50px")#Then create segment with articles. Where the first argument is segment header and here you can see how wrapping can be used. Here it makes "Front-py" red
        articles.addArticle("The first fact","This framework is attemp to combine the best ideas from Django, Flask, Angular and other frameworks but %s complicated application architecture" % brandText("without creating"))#Then we can use special method addArticle to add row article, you can see their appearence on the main page
        articles.addArticle("The second fact","You have to use only %s 3.x to write %s front and back-end" % (brandText("python"),brandText("both")))#The first argument is header of article, the second is content and the third is footer, but all arguments are optional you can left them empty.
        articles.addArticle("The third fact","Just see what you have to write on python (%s) and how many pure html you have to write to create the page you see:%s" % (brandText("including reusable components"),ContainerRow(Image("python1.png","Code",6),Image("html.png","Code",6))))#To add your own images put them into the pages/media/ folder and just write their full name as you can see here, the second argument us alt and the third is width of image in percent, height will be set proportionaly
    
        page = Page("Home",*pageParams)#Then you MUST create page, the first argument is title, the second we've defined early
        page.addElement(menu.addLinks({"Additional Link":"/nothing"},brandColor),articles,footer)#Then you MUST add some content to page
        return page#And then return the page to user









@serve("/objectives")#Another addres to be served
def objectives(request):
    if request.method == "GET":
        articles = Article(headersLevel=2)#Here you can find wrapping ideas. We just created object and configured it but it'll be used later as wrapper
        myList = NumberedList() #The same thing but you can add no configuration almost everything is predefined
        frontEnd = articles("Front-end",NumberedList({},"Reorgonaising folders","A lot of tests","Unnumbered list","Gallery","Forms","Tests","Customizing existing classes","Tests"))#Then it has been created three articles, using one wrap
        backEnd = articles("Back-end",NumberedList({},"Handling POST request","Grand tests of framework","Creating API to database","Tests"))
        experience = articles("Experience",NumberedList({},"Writing documentation","Create complete guides for users, developers and testers","Work with %s on github" % Link("https://github.com/DimonLuk/front-py/wiki","wiki")))
    
        preAlphaObjectives = ColumnArticles("%s pre-alpha objectives" % brandText("Front-py"),"",1,"center","50px",True,frontEnd,backEnd,experience)#Then this three articles has been add to column articles, meaning of arguments you can find bellow, empty string is footer
    
        alphaObjectives = ColumnArticles("%s alpha objectives" % brandText("Front-py"),headersLevel=1,position="center",verticalDistance="50px",horizontalLine=True)#Here you can see wrapping ideas just created object
    
        frontEnd = articles("Front-end",myList("Galleries","Carousels","Registartion","Log in","Permission system","Admin panel"))
        backEnd = articles("Back-end",myList("Registration","Log In","Permission system","Admin panel","Optional: write own server"))
        experience = articles("Experience",myList("Improve internal framework architecture","Improve API for users","Improve documentation and make complite guides for future beta version where API won't be changing"))
    
        alphaObjectives(frontEnd,backEnd,experience)#Then we wrap three articles as they are column articles
    
        betaObjectives = ColumnArticles("%s beta objectives" % brandText("Front-py"),headersLevel=1,position="center",verticalDistance="50px",horizontalLine=True)

        frontEnd = articles("Front-end",myList("Create simple API to make everything easily customizable","Test and improve"))
        backEnd = articles("Back-end",myList("Create simple API to make everythong easily customizable","Test and improve"))
        experience = articles("Experience",myList("Test and improve"))
    
        betaObjectives(frontEnd,backEnd,experience)

        page = Page("Objectives",*pageParams)#Then we have to create page
        page.addElement(menu,preAlphaObjectives,alphaObjectives,betaObjectives,footer)#add elements on it
        return page#And return to user

#The next interesting thing is at the end of the file
@serve("/userGuide")
def userGuide(request):
    guide = RowArticles(saveFormat=True,isCode=True)
    guide.addArticle("","""\"\"\"
I think that the best tutorial is the life example
The result of this tutorial you can see at the website
So you may find everything which has been done in this file
String by string you'll learn more and more about building applications with Fornt-py\n
So, let's start
It'll be a lot, A LOT of text here :))))))
\"\"\"
#To add your favicon.ico just put it in pages/media/ folder
from frontpy.frontpy import * #All necessary imports are here, you can watch this file if it's interesting to you to know how it works

#This block is used to create one theme for all pages
#It's easier to store this values in variables because changing one thing here will change everything in the website
backgroundColor = "#dddddd" #Grey color of the pages
brandColor = "red" #Nice red color of some text
brandText = Text() #Wrapping object that will be used below
brandText.color = brandColor #Some objects can be cinfigured in this way. To be honest all objects will have opportunity to be configured in such way but a bit later
pageParams = tuple(["utf-8",{"background":backgroundColor}]) #Some meta information about page. Encoding and background color.
#But you can set any background settings you want, using css properties
menu = InlineMenu({"background":"black"},{"Home":"/", "Objectives":"/objectives","User guide":"/userGuide","Tester guide":"/testerGuide","Developer guide":"/developerGuide"},"white",BrandText("Front-py",brandColor)) #This is menu.
foot = Text("&copy DimonLuk") #Content you want to be displayed can be passed as the last argument of the constructor
foot.position = "center"#Another settings
foot.color = "white"
footer = Footer(foot)#You can use objects from framework to build other objects of framework
footer.backgroundColor = "black"

@serve("/")#This says that the function bellow will handle requests from main page of the website wich address is address.com/ or without "/"
def index(request):#Each function has to take one parameter which is the request. Now request contains only method field
    if request.method == "GET":#So let's check the method which browser used. No only GET can be handled
        #We habe to create a content for page
        articles = RowArticles("Three facts about %s 0.0.1(pre-alpha)" % brandText("Front-py"),horizontalLine=True,headersLevel=2,horizontalDistance="50px")#Then create segment with articles. Where the first argument is segment header and here you can see how wrapping can be used. Here it makes "Front-py" red
        articles.addArticle("The first fact","This framework is attemp to combine the best ideas from Django, Flask, Angular and other frameworks but %s complicated application architecture" % brandText("without creating"))#Then we can use special method addArticle to add row article, you can see their appearence on the main page
        articles.addArticle("The second fact","You have to use only %s 3.x to write %s front and back-end" % (brandText("python"),brandText("both")))#The first argument is header of article, the second is content and the third is footer, but all arguments are optional you can left them empty.
        articles.addArticle("The third fact","Just compare:%s" % ContainerRow(Image("test.png","Code",50),Image("test.png","Code",50)))#To add your own images put them into the pages/media/ folder and just write their full name as you can see here, the second argument us alt and the third is width of image in percent, height will be set proportionaly
    
        page = Page("Home",*pageParams)#Then you MUST create page, the first argument is title, the second we've defined early
        page.addElement(menu.addLinks({"Additional Link":"/nothing"},brandColor),articles,footer)#Then you MUST add some content to page
        return page#And then return the page to user

@serve("/objectives")#Another addres to be served
def objectives(request):
    if request.method == "GET":
        articles = Article(headersLevel=2)#Here you can find wrapping ideas. We just created object and configured it but it'll be used later as wrapper
        myList = NumberedList() #The same thing but you can add no configuration almost everything is predefined
        frontEnd = articles("Front-end",NumberedList({},"Reorgonaising folders","A lot of tests","Unnumbered list","Gallery","Forms","Tests","Customizing existing classes","Tests"))#Then it has been created three articles, using one wrap
        backEnd = articles("Back-end",NumberedList({},"Handling POST request","Grand tests of framework","Creating API to database","Tests"))
        experience = articles("Experience",NumberedList({},"Writing documentation","Create complete guides for users, developers and testers","Work with %s on github" % Link("https://github.com/DimonLuk/front-py/wiki","wiki")))
    
        preAlphaObjectives = ColumnArticles("%s pre-alpha objectives" % brandText("Front-py"),"",1,"center","50px",True,frontEnd,backEnd,experience)#Then this three articles has been add to column articles, meaning of arguments you can find bellow, empty string is footer
    
        alphaObjectives = ColumnArticles("%s alpha objectives" % brandText("Front-py"),headersLevel=1,position="center",verticalDistance="50px",horizontalLine=True)#Here you can see wrapping ideas just created object
    
        frontEnd = articles("Front-end",myList("Galleries","Carousels","Registartion","Log in","Permission system","Admin panel"))
        backEnd = articles("Back-end",myList("Registration","Log In","Permission system","Admin panel","Optional: write own server"))
        experience = articles("Experience",myList("Improve internal framework architecture","Improve API for users","Improve documentation and make complite guides for future beta version where API won't be changing"))
    
        alphaObjectives(frontEnd,backEnd,experience)#Then we wrap three articles as they are column articles
    
        betaObjectives = ColumnArticles("%s beta objectives" % brandText("Front-py"),headersLevel=1,position="center",verticalDistance="50px",horizontalLine=True)

        frontEnd = articles("Front-end",myList("Create simple API to make everything easily customizable","Test and improve"))
        backEnd = articles("Back-end",myList("Create simple API to make everythong easily customizable","Test and improve"))
        experience = articles("Experience",myList("Test and improve"))
    
        betaObjectives(frontEnd,backEnd,experience)

        page = Page("Objectives",*pageParams)#Then we have to create page
        page.addElement(menu,preAlphaObjectives,alphaObjectives,betaObjectives,footer)#add elements on it
        return page#And return to user
        
@serve("/<any>")#This is very interesting part. If user send some request that hasn't been defined explicity you can handle it here. Patterns can be different "/<any>/page/<any>" "/123/<any>/Front-pyTheBest/<any>"
    def anypage(request):
        if request.method == "GET":
            page = Page("%s" % request.path[1:],*pageParams) 
            page.addElement(menu,Text("ANY"),footer)
            return page

runApp()#Then you can run app. By the default it will be on localhost:8000/
#You can change addres in port by writing runApp(address=192.3.3.245,port=2000) for example
#To tun the app, you have to open the terminal in the folder where sample.py is stored and type in your terminal:
#python sample.py 
#and you'll launch the copy of the webiste if you haven't changed anything
#Very important to create your own files ONLY where sample.py is stored
#If it'll be necessary I can make video guides :)""",saveFormat=True,isCode=True,lang="python",background={"background":backgroundColor})

    page = Page("User Guide",*pageParams)
    page.addElement(menu,guide,footer)
    return page
@serve("/testerGuide")
def testerGuide(request):
    page = Page("Tester Guide",*pageParams)
    page.addElement(menu,footer)
    return page

@serve("/developerGuide")
def testerGuide(request):
    page = Page("Developer Guide",*pageParams)
    page.addElement(menu,footer)
    return page

@serve("/<any>")#This is very interesting part. If user send some request that hasn't been defined explicity you can handle it here. Patterns can be different "/<any>/page/<any>" "/123/<any>/Front-pyTheBest/<any>"
def anypage(request):
    page = Page("%s" % request.path[1:],*pageParams)
    page.addElement(menu,Text("ANY"),footer)
    return page

runApp()#Then you can run app. By the default it will be on localhost:8000/
#You can change addres in port by writing runApp(address=192.3.3.245,port=2000) for example
#To tun the app, you have to open the terminal in the folder where sample.py is stored and type in your terminal:
#python sample.py 
#and you'll launch the copy of the webiste if you haven't changed anything
#Very important to create your own files ONLY where sample.py is stored
#If it'll be necessary I can make video guides :)
