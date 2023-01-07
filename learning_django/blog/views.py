from django.shortcuts import render

posts = [
  {
    'author': 'Tim Collins',
    'title': 'Blog post',
    'content' : 'First post content',
    'date_posted': 'January 7th, 2023'
  },
  {
    'author': 'Dieter Rams',
    'title': '10 Principles of design',
    'content' : 'Dieter was here',
    'date_posted': 'January 7th, 2023'
  }
]

def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', {'title': 'about'})
