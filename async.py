from front_py import *


@serve("/")
def index(request):
    if request.method == "GET":
        page = Page("Home", url="/test")
        return page

@serve("/test")
def test(request):
    if request.method == "GET":
        return "<script>$(window).on('load', function(){$.ajax({url:'http://localhost:8000%s',success:function(data){$('.global').html(data)}})});</script><h1>Test</h1>" % request.path
