from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm
from django.contrib.auth.forms import SetPasswordForm

urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/<product_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
    path('plus-cart/', views.plus_cart, name='plus_cart'),
    path('minus-cart/', views.minus_cart, name='minus_cart'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment-done/', views.payment_done, name='payment-done'),
    path('profile/', views.MyProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    # path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', views.logout_page, name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=SetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
