from django.http import HttpResponse
import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
    # return HttpResponseNotFound("<h1>Page not found</h1>") 으로 404 에러 출력
