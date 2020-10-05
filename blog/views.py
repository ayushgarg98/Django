from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.views import generic
from .models import Blog, Author, Entry
from .form import BlogForm

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Blog.objects.all()


class BlogView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog.html'


class EntryView(generic.DetailView):
    model = Entry
    template_name = 'blog/entry.html'


def get_blog(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['name'])
            # print(form.cleaned_data['tagline'])
            form.save()
            # form = BlogForm
            return HttpResponseRedirect('../')
    else:
        form = BlogForm()

    return render(request, 'blog/blog_form.html', {'form': form})


def saved(request):
    template = loader.get_template("blog/blog.html")
    return HttpResponse(template.render())


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('../')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)






