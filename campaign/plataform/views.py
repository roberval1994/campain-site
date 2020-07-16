from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request, 'Index.html', {})

def about_me(request):
    return render(request, 'about_me.html', {})