from frontpy.frontpy import *

#This block is used to create one theme for all pages
backgroundColor = "#dddddd"
brandColor = "red" 
brandText = Text()
brandText.color = brandColor
pageParams = tuple(["utf-8",{"background":backgroundColor}])
menu = InlineMenu({"background":"black"},{"Home":"/", "Objectives":"/objectives","User guide":"/userGuide","Tester guide":"/testerGuide","Developer guide":"/developerGuide"},"white",BrandText("Front-py",brandColor))
foot = Text("&copy DimonLuk")
foot.position = "center"
foot.color = "white"
footer = Footer(foot)
footer.backgroundColor = "black"

@serve("/")
def index(request):
    if request.method == "GET":
        articles = RowArticles("Three facts about %s 0.0.1(pre-alpha)" % brandText("Front-py"),horizontalLine=True,headersLevel=2,horizontalDistance="50px")
        articles.addArticle("The first fact","This framework is attemp to combine the best ideas from Django, Flask, Angular and other frameworks but %s complicated application architecture" % brandText("without creating"))
        articles.addArticle("The second fact","You have to use only %s 3.x to write %s front and back-end" % (brandText("python"),brandText("both")))
        articles.addArticle("The third fact","Just compare:%s" % ContainerRow(Image("test.png","Code",50),Image("test.png","Code",50)))
    
        page = Page("Home",*pageParams)
        page.addElement(menu.addLinks({"Additional Link":"/nothing"},brandColor),articles,footer)
        return page









@serve("/objectives")
def objectives(request):
    if request.method == "GET":
        articles = Article(headersLevel=2)
        myList = NumberedList() 
        frontEnd = articles("Front-end",NumberedList({},"Reorgonaising folders","A lot of tests","Unnumbered list","Gallery","Forms","Tests","Customizing existing classes","Tests"))
        backEnd = articles("Back-end",NumberedList({},"Handling POST request","Grand tests of framework","Creating API to database","Tests"))
        experience = articles("Experience",NumberedList({},"Writing documentation","Create complete guides for users, developers and testers","Work with %s on github" % Link("https://github.com/DimonLuk/front-py/wiki","wiki")))
    
        preAlphaObjectives = ColumnArticles("%s pre-alpha objectives" % brandText("Front-py"),"",1,"center","50px",True,frontEnd,backEnd,experience)
    
        alphaObjectives = ColumnArticles("%s alpha objectives" % brandText("Front-py"),headersLevel=1,position="center",verticalDistance="50px",horizontalLine=True)
    
        frontEnd = articles("Front-end",myList("Galleries","Carousels","Registartion","Log in","Permission system","Admin panel"))
        backEnd = articles("Back-end",myList("Registration","Log In","Permission system","Admin panel","Optional: write own server"))
        experience = articles("Experience",myList("Improve internal framework architecture","Improve API for users","Improve documentation and make complite guides for future beta version where API won't be changing"))
    
        alphaObjectives(frontEnd,backEnd,experience)
    
        betaObjectives = ColumnArticles("%s beta objectives" % brandText("Front-py"),headersLevel=1,position="center",verticalDistance="50px",horizontalLine=True)

        frontEnd = articles("Front-end",myList("Create simple API to make everything easily customizable","Test and improve"))
        backEnd = articles("Back-end",myList("Create simple API to make everythong easily customizable","Test and improve"))
        experience = articles("Experience",myList("Test and improve"))
    
        betaObjectives(frontEnd,backEnd,experience)

        page = Page("Objectives",*pageParams)
        page.addElement(menu,preAlphaObjectives,alphaObjectives,betaObjectives,footer)
        return page

@serve("/userGuide")
def userGuide(request):
    page = Page("User Guide",*pageParams)
    page.addElement(menu,footer)
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

@serve("/<any>")
def anypage(request):
    page = Page("%s" % request.path[1:],*pageParams)
    page.addElement(menu,Text("ANY"),footer)
    return page

runApp()
