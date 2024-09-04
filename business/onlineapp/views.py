from django.shortcuts import render, redirect
from .models  import Product
# Create your views here.

'''''
def index(request):
    return render(request, 'onlineapp/index.html')
    '''''
def products(request):
    return render(request, 'onlineapp/product_list.html')

def add_product(request):
     #handle your submissions
    if request.method == 'POST':
        #get form data
        product_name = request.POST['name']
        product_price = request.POST['price']
        product_quantity = request.POST['quantity']
        product_description = request.POST['description']
        product_category = request.POST['category']
        product_comment = request.POST['comment']
        product_image = request.FILES['image']
        #save to database]

       #accessing the fields in the models and saving the data form to our database.
        new_product = Product()
        new_product.product_name = product_name
        new_product.product_price = product_price
        new_product.product_quantity = product_quantity
        new_product.product_description = product_description
        new_product.product_category = product_category
        new_product.product_comment = product_comment
        new_product.product_image = product_image
        new_product.save()
        return redirect('product_list')
      # redirect to product list page after successful product addition.
      

    else:
        #if the request method is not POST, render the form
        return render(request, 'onlineapp/add_product.html')    