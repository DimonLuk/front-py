import os
import sys
import json
import importlib
PATH = "application"
def prepare_import():
    framework = os.path.join(os.getcwd(),PATH)
    sys.path.append(framework)      
    for dirs,subdirs,files in os.walk(framework):
        if not "__pycache__" in dirs:   
            sys.path.append(dirs)

if __name__ == "__main__":
    if sys.argv[1] == "start" and len(sys.argv) == 2:
        prepare_import()
        params = {}
        with open(os.path.join(PATH,"config.json"),"r") as file:
            params = json.load(file)
        app = importlib.import_module(params["source_file"])
        app.run_app(address=params["address"],port=params["port"])
    elif sys.argv[1] == "config" and len(sys.argv) == 2:
        params = {}
        source_file = input("Enter the filename where you application is (for example sample): ")
        if not source_file:
            raise ValueError("Please enter the filename it's required")
        address = input("Enter the addres you want to host (localhost is default): ")
        if not address:
            address = "localhost"
        port = input("Enter the port you want to host (8000 is default): ")
        if port:
            port = int(port)
        elif not port:
            port = 8000
        with open(os.path.join(PATH,"config.json"),"w") as file:
            json.dump({"source_file":source_file,"address":address,"port":port},file)
    elif sys.argv[1] == "test" and len(sys.argv) == 2:
        prepare_import()
        test = importlib.import_module("functions")
        test.unittest.main()
    elif sys.argv[1] == "docs" and len(sys.argv) == 3:
        prepare_import()
        docs = importlib.import_module(sys.argv[2])
        print(docs.__dict__[sys.argv[2]].__doc__)
    elif sys.argv[1] == "tutorial" and len(sys.argv) == 2:
        print("""
\"\"\"
I suppose that the best guide is the life example, so let's start

Firstly you have to get Front-py. It can be done by dowloading and unpacking zip archive, or
by cloning repositiry with you terminal:
$ git clone https://github.com/DimonLuk/front-py.git

* - '$' shows that the message after it has to be written in terminal or command line, you mustn't place any spaces in your terminal, just write the command

Then open your command line or terminal at the root of the project (where app.py file is located).
Then type in your terminal or command line:
$ python app.py start

Afer doing this you'll be able to go to your browser and open page with addres: http://localhost:8000/

If you want to change address you can type in your terminal or command line:
$ python app.py config

If you want to use your own file, you have to write its name (without .py) during the configuration

If you want to read this guide at your computer, you can write:
$ python app.py tutorial

To see documentation you should write:
$ python app.py docs <Class_or_function_name>
\"\"\"

#So, now let's see what the framework can do

#The first thing which is required is importing everything you need to develop your own pages
from front_py import * 

#Then you can setup your global variables that will make single style for all pages
background_color = "#dddddd" #Grey
brand_color = "red"
brand_text = Text() #Will be used as wrapper for text elements
brand_text.color = brand_color #Some parameters can be set using 'dot' notation
crossed_text = Text()
crossed_text.decor = "crossed"
page_params = tuple(["utf-8",{"background":background_color}]) #Then specife parameters for page, its encoding and background color

#Now it's a good idea to create menu which will contain all links to all your pages
#For the moment of writing this tutorial it's avaliable one style of menu, Inline_menu, to read more, write in your terminal or command line:
#$ python app.py docs Inline_menu
#But I suppose that your IDE should show you info about this class
menu = Inline_menu({"background":"black"},[{"Home":"/"},{"Git":"https://github.com/DimonLuk/front-py"},{"Documentation":"https://github.com/DimonLuk/front-py/wiki"}, {"Objectives":"/objectives"},{"User guide":"/userGuide"},{"Tester guide":"/testerGuide"},{"Developer guide":"/developerGuide"}],"white",Brand_text("Front-py",brand_color)) 

#Then it's a good idea to create one footer for all your pages
foot = Text("&copy DimonLuk")
foot.position = "center"
foot.color = "white"
footer = Footer(foot)
footer.background_color = "black"


#Now it's time to create some page
#At first it's required to specify whcih address you want to serve
#It can be done in this way:
@serve("/")
#If you configure your addres to loclahost and port to 8000, than addres which the function below will serve is http://localhost:8000/
#Name of the function below is not important, here you can write anything you want, even some hash, but do you realy want to do this?
def index(request):
    #This function takes one parametr whcih is request that browser has sent
    #But this request is simplified

    #Then we have to check what method the request has. At the moment of writing this tutorial you can handle only GET
    if request.method == "GET":
        #Then you can begin creating your content.
        #Sooner it'll be API between DB and the framework but for this moment all data should be hard-coded
        articles = Row_articles("Three facts about %s 0.0.1(pre-alpha)" % brand_text("Front-py"),horizontal_line=True,headers_level=2,horizontal_distance="50px")
        #Above you can see wrapping syntax, exactly at:
        #'"Three facts about %s 0.0.1(pre-alpha)" % brand_text("Front-py")'
        #You see that you can create one style and then wrap some content in this object
        #And also you can insert any object thinking that's just a string
        #Then you can yous 'brand_text' again
        articles.add_article("The first fact","This framework is attemp to combine the best ideas from Django, Flask, Angular and other frameworks but %s complicated application architecture" % brand_text("without creating"))
        articles.add_article("The second fact","You have to use only %s 3.x to write %s front and back-end" % (brand_text("python"),brand_text("both")))
        articles.add_article("The third fact","Just see what you have to write on python (%s) and how many pure html you have to write to create the page you see:%s" % (brand_text("including reusable components"),Container_row(Image("python1.png","Code",6),Image("html.png","Code",6))))
        #Or instead of wrapping content you can use special methods to add content.
        #Then create page, using parameters that has been defined above
        page = Page("Home",*page_params)
        #And of course place our elements to page
        page.add_element(menu.add_links({"Additional Link":"/nothing"},brand_color),articles,footer)
        return page #If you want the page to be seen in browser, you have just return it

# At the section below you can see more about wrapping syntax
# After 'objectives' function you can find very important feature of the framework
@serve("/objectives")
def objectives(request):
    if request.method == "GET":
        articles = Article(headers_level=2)
        myList = Numbered_list()
        front_end = articles("Front-end",Numbered_list({},"%s" % crossed_text("Reorganising packages"),"Unit tests","Unnumbered list","Gallery","Forms","Tests","Customizing existing classes","Tests"))
        back_end = articles("Back-end",Numbered_list({},"Handling POST request","Grand tests of framework","Creating API to database","Tests"))
        experience = articles("Experience",Numbered_list({},"Writing documentation","Create complete guides for users, developers and testers","Work with %s on github" % Link("https://github.com/DimonLuk/front-py/wiki","wiki")))
    
        pre_alpha_objectives = Column_articles("%s pre-alpha objectives" % brand_text("Front-py"),"",1,"center","50px",True,front_end,back_end,experience)
    
        alpha_objectives = Column_articles("%s alpha objectives" % brand_text("Front-py"),headers_level=1,position="center",vertical_distance="50px",horizontal_line=True)
    
        front_end = articles("Front-end",myList("Galleries","Carousels","Registartion","Log in","Permission system","Admin panel"))
        back_end = articles("Back-end",myList("Registration","Log In","Permission system","Admin panel","Optional: write own server"))
        experience = articles("Experience",myList("Improve internal framework architecture","Improve API for users","Improve documentation and make complite guides for future beta version where API won't be changing"))
    
        alpha_objectives(front_end,back_end,experience)
    
        beta_objectives = Column_articles("%s beta objectives" % brand_text("Front-py"),headers_level=1,position="center",vertical_distance="50px",horizontal_line=True)

        front_end = articles("Front-end",myList("Create simple API to make everything easily customizable","Test and improve"))
        back_end = articles("Back-end",myList("Create simple API to make everythong easily customizable","Test and improve"))
        experience = articles("Experience",myList("Test and improve"))
    
        beta_objectives(front_end,back_end,experience)

        page = Page("Objectives",*page_params)
        page.add_element(menu,pre_alpha_objectives,alpha_objectives,beta_objectives,footer)#add elements on it
        return page
# So, you can serve some pattern requests.
# For example, this config will serve all others requests, that hasn't been defined above
# Or you can write something like this:
# @serve("/&ltany&gt/page/&ltany&gt")
@serve("/<any>")
def anypage(request):
    #To get info about custom request, you can work with request.path
    if request.method == "GET":
        page = Page("%s" % request.path[1:],*page_params)
        page.add_element(menu,request.path,footer)
        return page                 
""")
    else:
        print("""
Avaliable commands:
    start - to start app
    config - to setup configuration of application
    test - to start unittests for all modules
    docs Class_or_function_name - to get documentation about class or function
        """)
