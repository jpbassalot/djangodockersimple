


from django.http import HttpResponse
from django.shortcuts import render

# Landing page route
def root(request):
    return render(request, 'index.html')