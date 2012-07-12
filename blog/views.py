# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from models import post,comment 
from django.shortcuts import render_to_response

import re
def post_list(request):
    posts = post.objects.all()
    print type(post_list)
    print post_list
    my_temp = loader.get_template('blog/post_list.html')
    my_context =Context({'posts': posts})
    
    return HttpResponse(my_temp.render(my_context))

def post_detail(request, id, showComments=False):
    posts =  post.objects.get(pk = id)##similar to selct from ...where id=...
    comment = posts.comments.all()##rem rel_type from models?it connects a post to its comments and we can retrieve them this 
    my_context = Context({'posts':posts, 'comment' : comment})
    '''
    html = '<h3>'+str(result) + '</h3><br/>' + str(result.body)+'<br/><h5>COMMENTS</h5><br/>'
    comm=''
    for i in result.comments.all():
        print 'haha'
        comm+=i.body + '<br/>'
       ''' 
    return render_to_response('blog/post_detail.html', my_context)
    
def post_search(request, term):
    posts = post.objects.filter(body__contains = term)
    #context = Context({'posts' : posts, 'term' : term })
    '''
    for i in result:
        res +='<ul><li><em>'+str(i)+'</em></li></ul>'
     '''   
    return render_to_response('blog/post_search.html',{'posts' : posts, 'term' : term })

    

def home(request):
    print 'it works'
    return render_to_response('blog/base.html',{}) 
