from frontpy.frontpy import *
menu = InlineMenu({"background":"black"},{"Home":"/", "Quick guide":"/quickGuide"},"#ffffff",BrandText("Front-py","#00ee00"))

@serve("/")
def index(request):
    page = Page("Sample","utf-8",{"background":"#dddddd"})
    greenText = Text()
    greenText.color = "#00cc00"
    articles = RowArticles("Three facts about %s 0.0.1(pre-alpha)" % greenText("Front-py"))
    articles.config(horizontalDistance="50px",horizontalLine=True,headersLevel=2)
    articles.addArticle("The first fact","Every page of the website is written with %s" % greenText("framework"))
    articles.addArticle("The second fact","You have to use only %s 3.x to write both front and back-end" % greenText("python"))
    articles.addArticle("The third fact","Everything that has been writtent to create this %s is here:%s" % (greenText("page"), Image("test.png","Code")))
    foot = Text("&copy DimonLuk")
    foot._addClass("mx-auto")
    footer = Footer(foot)
    page.addElement(menu,articles,footer)
    return page

@serve("/quickGuide")
def quickGuide(request):
    page = Page("QuickGuide","utf-8")
    page.addElement(menu)
    return page

@serve("/<any>")
def test(request):
    page = Page("%s" % request.path[1:],"utf-8",{"background-color":"whitesmoke"})
    page.addElement(menu)
    return page

runApp()
