from .views import *

def cat(request):
    catr=cate.objects.all()
    return {'j':catr}
