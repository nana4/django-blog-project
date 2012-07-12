from django.contrib import admin
from django.db import models

class post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    #author =models.CharField(max_length=60)
    created = models.DateField(auto_now = True)
    updated = models.DateField(auto_now = True)

    def __unicode__(self):
        return self.body
    
    def first_60(self):
        return self.body[:60]
'''
    @models.permalink    def get_abs_url(self):
        return ('post_detail', [self.id], {'showComments' : True}
        '''

class comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length=60)
    created = models.DateField()
    updated = models.DateField()
    post = models.ForeignKey(post, related_name='comments')##just like post id

    def __unicode__(self):
        return self.author
    

    def first_sixty(self):
        return self.body[:60]
    
class CommentInline(admin.TabularInline):
	model = comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('body', 'title')
    list_filter = ('created', 'updated')
    search_fields = ('title', 'body')
    inlines = [CommentInline]
    


class CommentAdmin(admin.ModelAdmin):
	list_display = ( 'author', 'first_sixty', 'created', 'updated','post')
	list_filter = ('created', 'author', 'updated' )
	#inlines = [CommentInline]

	
    
admin.site.register(post,PostAdmin)
admin.site.register(comment,CommentAdmin) 

