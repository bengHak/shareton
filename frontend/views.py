from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'frontend/login.html', {})

def main(request):
    return render(request, 'frontend/index/index.html', {})
    
def detail(request, name='학교이름'):
    return render(request, 'frontend/detail/detail.html',{'name':name})


def payment(request):
    return render(request, 'frontend/payment.html', {})


def payment_done(request):
    return render(request, 'frontend/payment_done.html', {})
