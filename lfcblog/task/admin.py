from django.contrib import admin
from django import forms
try:
    from simplemde.widgets import SimpleMDEWidget  # type: ignore
except Exception:  # Fallback if simplemde isn't available to the analyzer
    from django.forms import Textarea as SimpleMDEWidget  # type: ignore
from .models import Post

# Register your models here.

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SimpleMDEWidget(),
        }


class PostAdmin (admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    list_filter = ('status', 'created_on', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'created_on']
    form = PostForm

admin.site.register(Post, PostAdmin)
