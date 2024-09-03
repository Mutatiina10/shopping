from django.shortcuts import render

# Create your views here.

'''''
def index(request):
    return render(request, 'onlineapp/index.html')
    '''''
def products(request):
    return render(request, 'onlineapp/product_list.html')