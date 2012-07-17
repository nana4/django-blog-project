# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from models import post, comment 
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect



import re
def post_list(request):
    posts = post.objects.all()
    print type(post_list)
    print post_list
    my_temp = loader.get_template('blog/post_list.html')
    my_context =Context({'posts': posts})
    return HttpResponse(my_temp.render(my_context))

class CommentForm(ModelForm):
    class Meta:
        model = comment #displays the attributes of a p'cular class (comment)in this 				#case
        exclude=['post']
        
@csrf_exempt
def post_detail(request, id, showComments=False):
    posts =  post.objects.get(pk = id)##similar to select from ...where id=...
    				      ##remember rel_type from models?it connects a 					      ##post to its comments and we can retrieve 					      ##them this way
    '''
    html = '<h3>'+str(result) + '</h3><br/>' + str(result.body)+'<br/><h5>COMMENTS</ h5><br/>'
    comm=''
    for i in result.comments.all():
        print 'haha'
        comm+=i.body + '<br/>'
       ''' ##previously
    
    if request.method == 'POST':
	comm = comment(post = posts)
	form = CommentForm(request.POST, instance=comm)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()
    comments = posts.comments.all()
    #my_context = Context({'posts':posts, 'comment' : comments, 'form':form})
    return render_to_response('blog/post_detail.html', {'posts':posts, 'comments' : comments, 'form':form})

@csrf_exempt   
def edit_comment(request, id):
	comment_edit = comment.objects.get(pk = id)
    	if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment_edit)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(comment_edit.post.get_absolute_url())
        else:
           form = CommentForm(instance = comment_edit)
           return render_to_response('blog/post_detail.html',{'form':form, 'comment':comment_edit,})	
def post_search(request, term):
    posts = post.objects.filter(body__icontains = term)
    '''
    for i in result:
        res +='<ul><li><em>'+str(i)+'</em></li></ul>'
     '''   
    return render_to_response('blog/post_search.html',{'posts' : posts, 'term' : term })
def __unicode__(self):
    return self.title

@csrf_exempt     
def home(request):
    #print 'it works'
    return render_to_response('blog/base.html',{}) 

