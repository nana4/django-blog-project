# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from models import post, comment 


def post_list(request):
    post_list = post.objects.all()
    
   # print type(post_list)
    #print post_list
    
    return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
    result =  post.objects.get(pk=id)
    html = '<h3>'+str(result) + '</h3><br/>' + str(result.body)+'<br/><h5>COMMENTS</h5><br/>'
    comm=''
    for i in result.comments.all():
        comm+=i.body + '<br/><br/>'
    return HttpResponse(html+comm)
    
def post_search(request, term):
    result = post.object.all()
    #s_res = re.search(r'.*', re)
    return HttpResponse(result)
    
    

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
