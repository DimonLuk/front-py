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
background_color = "#dddddd" #Grey color of the pages
brand_color = "red" #Nice red color of some text
brand_text = Text() #Wrapping object that will be used below
brand_text.color = brand_color #Some objects can be cinfigured in this way. To be honest all objects will have opportunity to be configured in such way but a bit later
page_params = tuple(["utf-8",{"background":background_color}]) #Some meta information about page. Encoding and background color.
#But you can set any background settings you want, using css properties
menu = Inline_menu({"background":"black"},[{"Home":"/"},{"Git":"https://github.com/DimonLuk/front-py"},{"Documentation":"https://github.com/DimonLuk/front-py/wiki"}, {"Objectives":"/objectives"},{"User guide":"/userGuide"},{"Tester guide":"/testerGuide"},{"Developer guide":"/developerGuide"}],"white",Brand_text("Front-py",brand_color)) #This is menu.
foot = Text("&copy DimonLuk") #Content you want to be displayed can be passed as the last argument of the constructor
foot.position = "center"#Another settings
foot.color = "white"
footer = Footer(foot)#You can use objects from framework to build other objects of framework
footer.background_color = "black"

@serve("/")#This says that the function bellow will handle requests from main page of the website wich address is address.com/ or without "/"
def index(request):#Each function has to take one parameter which is the request. Now request contains only method field
    if request.method == "GET":#So let's check the method which browser used. No only GET can be handled
        #We habe to create a content for page
        articles = Row_articles("Three facts about %s 0.0.1(pre-alpha)" % brand_text("Front-py"),horizontal_line=True,headers_level=2,horizontal_distance="50px")#Then create segment with articles. Where the first argument is segment header and here you can see how wrapping can be used. Here it makes "Front-py" red
        articles.add_article("The first fact","This framework is attemp to combine the best ideas from Django, Flask, Angular and other frameworks but %s complicated application architecture" % brand_text("without creating"))#Then we can use special method addArticle to add row article, you can see their appearence on the main page
        articles.add_article("The second fact","You have to use only %s 3.x to write %s front and back-end" % (brand_text("python"),brand_text("both")))#The first argument is header of article, the second is content and the third is footer, but all arguments are optional you can left them empty.
        articles.add_article("The third fact","Just see what you have to write on python (%s) and how many pure html you have to write to create the page you see:%s" % (brand_text("including reusable components"),Container_row(Image("python1.png","Code",6),Image("html.png","Code",6))))#To add your own images put them into the pages/media/ folder and just write their full name as you can see here, the second argument us alt and the third is width of image in percent, height will be set proportionaly
    
        page = Page("Home",*page_params)#Then you MUST create page, the first argument is title, the second we've defined early
        page.add_element(menu.add_links({"Additional Link":"/nothing"},brand_color),articles,footer)#Then you MUST add some content to page
        return page#And then return the page to user









@serve("/objectives")#Another addres to be served
def objectives(request):
    if request.method == "GET":
        articles = Article(headers_level=2)#Here you can find wrapping ideas. We just created object and configured it but it'll be used later as wrapper
        myList = Numbered_list() #The same thing but you can add no configuration almost everything is predefined
        front_end = articles("Front-end",Numbered_list({},"Reorgonaising folders","A lot of tests","Unnumbered list","Gallery","Forms","Tests","Customizing existing classes","Tests"))#Then it has been created three articles, using one wrap
        back_end = articles("Back-end",Numbered_list({},"Handling POST request","Grand tests of framework","Creating API to database","Tests"))
        experience = articles("Experience",Numbered_list({},"Writing documentation","Create complete guides for users, developers and testers","Work with %s on github" % Link("https://github.com/DimonLuk/front-py/wiki","wiki")))
    
        pre_alpha_objectives = Column_articles("%s pre-alpha objectives" % brand_text("Front-py"),"",1,"center","50px",True,front_end,back_end,experience)#Then this three articles has been add to column articles, meaning of arguments you can find bellow, empty string is footer
    
        alpha_objectives = Column_articles("%s alpha objectives" % brand_text("Front-py"),headers_level=1,position="center",vertical_distance="50px",horizontal_line=True)#Here you can see wrapping ideas just created object
    
        front_end = articles("Front-end",myList("Galleries","Carousels","Registartion","Log in","Permission system","Admin panel"))
        back_end = articles("Back-end",myList("Registration","Log In","Permission system","Admin panel","Optional: write own server"))
        experience = articles("Experience",myList("Improve internal framework architecture","Improve API for users","Improve documentation and make complite guides for future beta version where API won't be changing"))
    
        alpha_objectives(front_end,back_end,experience)#Then we wrap three articles as they are column articles
    
        beta_objectives = Column_articles("%s beta objectives" % brand_text("Front-py"),headers_level=1,position="center",vertical_distance="50px",horizontal_line=True)

        front_end = articles("Front-end",myList("Create simple API to make everything easily customizable","Test and improve"))
        back_end = articles("Back-end",myList("Create simple API to make everythong easily customizable","Test and improve"))
        experience = articles("Experience",myList("Test and improve"))
    
        beta_objectives(front_end,back_end,experience)

        page = Page("Objectives",*page_params)#Then we have to create page
        page.add_element(menu,pre_alpha_objectives,alpha_objectives,beta_objectives,footer)#add elements on it
        return page#And return to user

#The next interesting thing is at the end of the file
@serve("/userGuide")
def userGuide(request):
    guide = Row_articles(save_format=True,is_code=True)
    guide.add_article("","""\"\"\"
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
background_color = "#dddddd" #Grey color of the pages
brand_color = "red" #Nice red color of some text
brand_text = Text() #Wrapping object that will be used below
brand_text.color = brand_color #Some objects can be cinfigured in this way. To be honest all objects will have opportunity to be configured in such way but a bit later
page_params = tuple(["utf-8",{"background":background_color}]) #Some meta information about page. Encoding and background color.
#But you can set any background settings you want, using css properties
menu = Inline_menu({"background":"black"},{"Home":"/", "Objectives":"/objectives","User guide":"/userGuide","Tester guide":"/testerGuide","Developer guide":"/developerGuide"},"white",Brand_text("Front-py",brand_color)) #This is menu.
foot = Text("&copy DimonLuk") #Content you want to be displayed can be passed as the last argument of the constructor
foot.position = "center"#Another settings
foot.color = "white"
footer = Footer(foot)#You can use objects from framework to build other objects of framework
footer.background_color = "black"

@serve("/")#This says that the function bellow will handle requests from main page of the website wich address is address.com/ or without "/"
def index(request):#Each function has to take one parameter which is the request. Now request contains only method field
    if request.method == "GET":#So let's check the method which browser used. No only GET can be handled
        #We habe to create a content for page
        articles = Row_articles("Three facts about %s 0.0.1(pre-alpha)" % brand_text("Front-py"),horizontal_line=True,headers_level=2,horizontal_distance="50px")#Then create segment with articles. Where the first argument is segment header and here you can see how wrapping can be used. Here it makes "Front-py" red
        articles.add_article("The first fact","This framework is attemp to combine the best ideas from Django, Flask, Angular and other frameworks but %s complicated application architecture" % brand_text("without creating"))#Then we can use special method addArticle to add row article, you can see their appearence on the main page
        articles.add_article("The second fact","You have to use only %s 3.x to write %s front and back-end" % (brand_text("python"),brand_text("both")))#The first argument is header of article, the second is content and the third is footer, but all arguments are optional you can left them empty.
        articles.add_article("The third fact","Just compare:%s" % Container_row(Image("test.png","Code",50),Image("test.png","Code",50)))#To add your own images put them into the pages/media/ folder and just write their full name as you can see here, the second argument us alt and the third is width of image in percent, height will be set proportionaly
    
        page = Page("Home",*page_params)#Then you MUST create page, the first argument is title, the second we've defined early
        page.add_element(menu.add_links({"Additional Link":"/nothing"},brand_color),articles,footer)#Then you MUST add some content to page
        return page#And then return the page to user

@serve("/objectives")#Another addres to be served
def objectives(request):
    if request.method == "GET":
        articles = Article(headers_level=2)#Here you can find wrapping ideas. We just created object and configured it but it'll be used later as wrapper
        myList = Numbered_list() #The same thing but you can add no configuration almost everything is predefined
        front_end = articles("Front-end",Numbered_list({},"Reorgonaising folders","A lot of tests","Unnumbered list","Gallery","Forms","Tests","Customizing existing classes","Tests"))#Then it has been created three articles, using one wrap
        back_end = articles("Back-end",Numbered_list({},"Handling POST request","Grand tests of framework","Creating API to database","Tests"))
        experience = articles("Experience",Numbered_list({},"Writing documentation","Create complete guides for users, developers and testers","Work with %s on github" % Link("https://github.com/DimonLuk/front-py/wiki","wiki")))
    
        pre_alpha_objectives = Column_articles("%s pre-alpha objectives" % brand_text("Front-py"),"",1,"center","50px",True,front_end,back_end,experience)#Then this three articles has been add to column articles, meaning of arguments you can find bellow, empty string is footer
    
        alpha_objectives = Column_articles("%s alpha objectives" % brand_text("Front-py"),headers_level=1,position="center",vertical_distance="50px",horizontal_line=True)#Here you can see wrapping ideas just created object
    
        front_end = articles("Front-end",myList("Galleries","Carousels","Registartion","Log in","Permission system","Admin panel"))
        back_end = articles("Back-end",myList("Registration","Log In","Permission system","Admin panel","Optional: write own server"))
        experience = articles("Experience",myList("Improve internal framework architecture","Improve API for users","Improve documentation and make complite guides for future beta version where API won't be changing"))
    
        alpha_objectives(front_end,back_end,experience)#Then we wrap three articles as they are column articles
    
        beta_objectives = Column_articles("%s beta objectives" % brand_text("Front-py"),headers_level=1,position="center",vertical_distance="50px",horizontal_line=True)

        front_end = articles("Front-end",myList("Create simple API to make everything easily customizable","Test and improve"))
        back_end = articles("Back-end",myList("Create simple API to make everythong easily customizable","Test and improve"))
        experience = articles("Experience",myList("Test and improve"))
    
        beta_objectives(front_end,back_end,experience)

        page = Page("Objectives",*page_params)#Then we have to create page
        page.add_element(menu,pre_alpha_objectives,alpha_objectives,beta_objectives,footer)#add elements on it
        return page#And return to user
        
@serve("/<any>")#This is very interesting part. If user send some request that hasn't been defined explicity you can handle it here. Patterns can be different "/<any>/page/<any>" "/123/<any>/Front-pyTheBest/<any>"
    def anypage(request):
        if request.method == "GET":
            page = Page("%s" % request.path[1:],*page_params) 
            page.add_element(menu,Text("ANY"),footer)
            return page

run_app()#Then you can run app. By the default it will be on localhost:8000/
#You can change addres in port by writing run_app(address=192.3.3.245,port=2000) for example
#To tun the app, you have to open the terminal in the folder where sample.py is stored and type in your terminal:
#python sample.py 
#and you'll launch the copy of the webiste if you haven't changed anything
#Very important to create your own files ONLY where sample.py is stored
#If it'll be necessary I can make video guides :)""",save_format=True,is_code=True,lang="python",background={"background":background_color})

    page = Page("User Guide",*page_params)
    page.add_element(menu,guide,footer)
    return page
@serve("/testerGuide")
def testerGuide(request):
    if request.method == "GET":
        guide = Row_articles()
        guide(text="I don't think that this project is so big to write very big instruction here. But I can give some advices. Try to create your own website with classes are presented in frontpy module. If you have any troubles, make screenshot of error, write some description and send this to me or try to fix it by yourself but at first read %s. My address is %s. Also you can try to create your own user-friendly classes but it's about Developer guide." % (Link("/developerGuide", "this guide"),Link("mailto:lds4ever2000@gmail.com","lds4ever2000@gmail.com")))
        page = Page("Tester Guide",*page_params)
        page.add_element(menu,guide,footer)
        return page

@serve("/developerGuide")
def testerGuide(request):
    if request.method == "GET":
        guide = Row_articles()
        guide("Developer codex :)",Numbered_list({},"No matter how it's difficult to create class, the only matter is how simple in use this class","Each class has to balance between simplicity and customizability","Each class has to redefine (if necessary) wrapping syntax","Almost every argument of any constructor or any method has to be predefined by author","But none of these rules are not aimed to reduce your creativity)))"))
        guide(text="More information you can find %s" % Link("https://github.com/DimonLuk/front-py/wiki","here"))
        page = Page("Developer Guide",*page_params)
        page.add_element(menu,guide,footer)
        return page

@serve("/<any>")#This is very interesting part. If user send some request that hasn't been defined explicity you can handle it here. Patterns can be different "/<any>/page/<any>" "/123/<any>/Front-pyTheBest/<any>"
def anypage(request):
    page = Page("%s" % request.path[1:],*page_params)
    page.add_element(menu,footer)
    return page

run_app()#Then you can run app. By the default it will be on localhost:8000/
#You can change addres in port by writing run_app(address=192.3.3.245,port=2000) for example
#To tun the app, you have to open the terminal in the folder where sample.py is stored and type in your terminal:
#python sample.py 
#and you'll launch the copy of the webiste if you haven't changed anything
#Very important to create your own files ONLY where sample.py is stored
#If it'll be necessary I can make video guides :)
