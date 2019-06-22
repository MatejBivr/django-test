from django.shortcuts import render

posts = [
  {
    'author': 'some guy',
    'title': 'some blog post',
    'content': 'some content',
    'date_posted': 'june 2019'
  },
  {
    'author': 'some guy',
    'title': 'some blog post 2',
    'content': 'some content 2',
    'date_posted': 'june 2019'
  },
  {
    'author': 'some guy',
    'title': 'some blog post 3',
    'content': 'some content 3',
    'date_posted': 'june 2019'
  },
  {
    'author': 'some guy',
    'title': 'some blog post 4',
    'content': 'some content 4',
    'date_posted': 'june 2019'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})