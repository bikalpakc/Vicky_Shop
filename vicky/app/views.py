from django.shortcuts import redirect, render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerProfileForm
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
 def get(self, request):
  topwears= Product.objects.filter(category='TW')
  bottomwears= Product.objects.filter(category='BW')
  mobiles= Product.objects.filter(category='M')
  if request.user.is_authenticated:
   no_of_items_in_cart=len(Cart.objects.filter(user=request.user))
  return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles, 'no_of_items_in_cart':no_of_items_in_cart})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
 def get(self, request, pk):
  product=Product.objects.get(pk=pk)
  if request.user.is_authenticated:
   no_of_items_in_cart=len(Cart.objects.filter(user=request.user))
  return render(request, 'app/productdetail.html', {'product':product, 'no_of_items_in_cart':no_of_items_in_cart})

@login_required(login_url='/accounts/login/') #login_url is optional but compulsary if Django cannot find login page by default.
def add_to_cart(request, product_id):
 product_id=product_id
 user=request.user
 product=Product.objects.get(id=product_id)
 cart=Cart(user=user, product=product)
 cart.save()
 return redirect('/cart/')

@login_required(login_url='/accounts/login/')
def cart(request):
 user=request.user
 cart_items=Cart.objects.filter(user=request.user)
 total_amount=0
 shipping_charge=70
 grand_total_amount=0
 for item in cart_items:
  total_amount = total_amount + (item.product.discounted_price * item.quantity)
  shipping_charge=70
 grand_total_amount=total_amount+shipping_charge
 if total_amount==0:
  shipping_charge=0
  grand_total_amount=0
  empty_cart_text="You have no items on your cart."
  context={'cart_items':cart_items,'total_amount': total_amount, 'shipping_charge': shipping_charge, 'grand_total_amount': grand_total_amount, 'empty_cart_text': empty_cart_text}
  return render(request, 'app/cart.html', context)
 
 else:
  context={'cart_items':cart_items,'total_amount': total_amount, 'shipping_charge': shipping_charge, 'grand_total_amount': grand_total_amount}
  return render(request, 'app/cart.html', context)

def plus_cart(request):
 if request.method == "GET":
  prod_id=request.GET['prod_id']
  print(prod_id)
  c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity+=1
  c.save()
  cart_items=Cart.objects.filter(user=request.user)
  total_amount=0
  shipping_charge=70
  grand_total_amount=0
  for item in cart_items:
    total_amount = total_amount + (item.product.discounted_price * item.quantity)
    shipping_charge=70
  grand_total_amount=total_amount+shipping_charge

  data={
   'quantity': c.quantity,
   'total_amount': total_amount,
   'shipping_charge': shipping_charge,
   'grand_total_amount': grand_total_amount,
  }
  return JsonResponse(data)
 
def minus_cart(request):
 if request.method == "GET":
  prod_id=request.GET['prod_id']
  print(prod_id)
  c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity-=1
  c.save()
  cart_items=Cart.objects.filter(user=request.user)
  total_amount=0
  shipping_charge=70
  grand_total_amount=0
  for item in cart_items:
    total_amount = total_amount + (item.product.discounted_price * item.quantity)
    shipping_charge=70
  grand_total_amount=total_amount+shipping_charge

  data={
   'quantity': c.quantity,
   'total_amount': total_amount,
   'shipping_charge': shipping_charge,
   'grand_total_amount': grand_total_amount,
  }
  return JsonResponse(data)
 
def remove_from_cart(request):
 if request.method == "GET":
  prod_id=request.GET['prod_id']
  print(prod_id)
  c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.delete()
  cart_items=Cart.objects.filter(user=request.user)
  total_amount=0
  shipping_charge=70
  grand_total_amount=0
  for item in cart_items:
    total_amount = total_amount + (item.product.discounted_price * item.quantity)
    shipping_charge=70
  grand_total_amount=total_amount+shipping_charge

  data={
   'total_amount': total_amount,
   'shipping_charge': shipping_charge,
   'grand_total_amount': grand_total_amount,
  }
  return JsonResponse(data)

@login_required(login_url='/accounts/login/')
def buy_now(request):
 return render(request, 'app/buynow.html')

@login_required(login_url='/accounts/login/')
def address(request):
 customer_data=Customer.objects.filter(user=request.user)
 for customer in customer_data:
        print(customer.name)

 if request.user.is_authenticated:
   no_of_items_in_cart=len(Cart.objects.filter(user=request.user))      
 return render(request, 'app/address.html', {'customer_data': customer_data, 'active': 'btn-primary', 'no_of_items_in_cart':no_of_items_in_cart})

@login_required(login_url='/accounts/login/')
def orders(request):
 user=request.user
 order_details=OrderPlaced.objects.filter(user=user)
 return render(request, 'app/orders.html', {'order_details': order_details})

def mobile(request, data=None):
 if data==None:
  mobiles=Product.objects.filter(category='M')
 elif data=='BKBS' or data=='Apple' or data=='Smoky' or data=='Samsung':
  mobiles=Product.objects.filter(category='M').filter(brand=data)
 elif data=='below-20k':
  mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=20000)
 elif data=='above-20k':
  mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=20000)

 if request.user.is_authenticated:
   no_of_items_in_cart=len(Cart.objects.filter(user=request.user))

 return render(request, 'app/mobile.html', {'mobiles': mobiles, 'no_of_items_in_cart':no_of_items_in_cart})

# def login(request):
#  return render(request, 'app/login.html')

def logout_page(request):
   logout(request)
   return redirect('/accounts/login/')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
 def get(self, request):
  form=CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html', {'form':form})
 
 def post(self, request):
  form=CustomerRegistrationForm(request.POST)
  if form.is_valid():
   form.save()
   messages.success(request, 'Congratulations!! Registered Successfully')
  return render(request, 'app/customerregistration.html', {'form':form})

@login_required(login_url='/accounts/login/')
def checkout(request):
 user=request.user
 cart_items=Cart.objects.filter(user=user)
 customer_details=Customer.objects.filter(user=user)
 total_amount=0
 shipping_charge=70
 grand_total_amount=0
 for item in cart_items:
  total_amount = total_amount + (item.product.discounted_price * item.quantity)
  shipping_charge=70
 grand_total_amount=total_amount+shipping_charge
 
 return render(request, 'app/checkout.html', {'cart_items': cart_items, 'customer_details': customer_details, 'total_amount': total_amount, 'shipping_charge': shipping_charge, 'grand_total_amount': grand_total_amount, 'paypal_client_id': settings.PAYPAL_CLIENT_ID})

@login_required(login_url='/accounts/login/')
def payment_done(request):
 user=request.user
 customer_id=request.GET.get('customer_id')
 customer=Customer.objects.get(id=customer_id)
 cart=Cart.objects.filter(user=user)
 for item in cart:
  order_placed=OrderPlaced(user=user, customer=customer, product=item.product, quantity=item.quantity)
  order_placed.save()
  item.delete()
 return redirect("orders")

@method_decorator(login_required, name='dispatch')
class MyProfileView(View):

  def get(self, request):
    form=CustomerProfileForm
    if request.user.is_authenticated:
     no_of_items_in_cart=len(Cart.objects.filter(user=request.user))
    return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary', 'no_of_items_in_cart':no_of_items_in_cart})
  
  def post(self, request):
   form=CustomerProfileForm(request.POST)
   if form.is_valid():
    user=request.user
    name=form.cleaned_data['name']
    locality=form.cleaned_data['locality']
    city=form.cleaned_data['city']
    zipcode=form.cleaned_data['zipcode']
    state=form.cleaned_data['state']

    var=Customer(user=user, name=name, locality=locality, city=city, zipcode=zipcode, state=state)
    var.save()
    messages.success(request, 'Account details updated Successfully.')

    return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

