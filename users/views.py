import json

import requests
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.shortcuts import (
    redirect,
    render,
)
from django.contrib.auth.decorators import login_required

from .forms import (
    CustomLoginForm,
    RegisterForm,
    SearchForm
)
from .decorators import only_authenticated_user, redirect_authenticated_user
from searchPage.views import SearchPage


def home_view(request):
    return render(request, 'users/home.html')


@redirect_authenticated_user
def login_view(request):
    error = None
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, username=form.cleaned_data['username_or_email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('users:home')
            else:
                error = 'Invalid Credentials'
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form, 'error': error})


@only_authenticated_user
@login_required
def logout_view(request):
    logout(request)
    return redirect('users:login')


@redirect_authenticated_user
def registeration_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.source = 'Register'
            user.save(True)
            messages.success(request, _(f'User created!'))
            return redirect('users:login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def search_view(request):
    error = None
    if request.method == 'POST':
        form = SearchForm(request.POST)

        response = SearchPage().get(request, form.data['query'])
        news_data = response[0][:10]

        if form.is_valid():
            return render(request, 'users/search_results.html', {'news': news_data, 'query': form.data['query']})
    else:
        return render(request, 'users/search.html', {'form': SearchForm(), 'error': error})



'''

ok",
   "articles":[
      {
         "url":"https://www.npr.org/2023/08/30/1196802338/rudy-giuliani-defamation-georgia-election-workers",
         "title":"Rudy Giuliani is liable for defaming 2 Georgia election workers, a judge says",
         "author":"Jaclyn Diaz",
         "source":{
            "id":null,
            "name":"NPR"
         },
         "content":"Rudy Giuliani speaks outside the Fulton County jail in Atlanta on Aug. 23, before he surrendered on 13 felony charges related to efforts to try to overturn the 2020 election.\r\nBrynn Anderson/AP\r\nRudy… [+1695 chars]",
         "urlToImage":"https://media.npr.org/assets/img/2023/08/30/ap23235736770062_wide-11076d1edc2a90598bb623bc4aa002e5f8f6fb4a-s1400-c100.jpg",
         "description":"Judge Beryl Howell's decision means that a trial will commence in this case to decide how much Rudy Giuliani must pay Ruby Freeman and Wandrea \"Shaye\" Moss.",
         "publishedAt":"2023-08-30T16:59:08Z"
      },
      {
         "url":"https://github.com/natalie-lang/natalie",
         "title":"Natalie – a work-in-progress Ruby compiler, written in Ruby and C++",
         "author":"natalie-lang",
         "source":{
            "id":null,
            "name":"Github.com"
         },
         "content":"Natalie is a very early-stage work-in-progress Ruby implementation.\r\nIt provides an ahead-of-time compiler using C++ and gcc/clang as the backend.\r\nAlso, the language has a REPL that performs increme… [+4826 chars]",
         "urlToImage":"https://opengraph.githubassets.com/436ec4605cb8680ca2c346e92ad6082dd08ba6aca4d02deb984b94fdf36d5da4/natalie-lang/natalie",
         "description":"a work-in-progress Ruby compiler, written in Ruby and C++ - GitHub - natalie-lang/natalie: a work-in-progress Ruby compiler, written in Ruby and C++",
         "publishedAt":"2023-09-24T07:40:53Z"
      },
      {
         "url":"https://railsatscale.com/2023-08-29-ruby-outperforms-c/",
         "title":"Ruby Outperforms C: Breaking the Catch-22",
         "author":"Aaron Patterson",
         "source":{
            "id":null,
            "name":"Railsatscale.com"
         },
         "content":"Ruby Outperforms C: Breaking the Catch-22\r\nRuby is an expressive, and fun language to write.\r\nIt helps us get our job done quickly by allowing us to easily get our thoughts written down as executable… [+17353 chars]",
         "urlToImage":null,
         "description":"YJIT’s ability to improve performance by adapting to run-time behavior can increase the speed of our code in a way that dropping down to C can’t. As such, I think we should reconsider the common wisdom that “rewriting our Ruby in C” is the ideal path to perfo…",
         "publishedAt":"2023-09-07T17:43:12Z"
      },
'''