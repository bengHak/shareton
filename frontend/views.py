from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'frontend/index/index.html', {})
    
def detail(request):
    return render(request, 'frontend/detail/detail.html',{})