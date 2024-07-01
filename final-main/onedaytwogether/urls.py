from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from onedaytwogether import views as onedaytwogether_view
from onedaytwogether.views import *

app_name = 'onedaytwogether'

urlpatterns = [
    path('', onedaytwogether_view.HomeView.as_view(), name='index'),
    path('Destination/', onedaytwogether_view.DestinationView.as_view(), name='Destination'),
    path('Shop/', onedaytwogether_view.ShopView.as_view(), name='shop'),
    path('Shop/<str:category>/', ShopCategoryView.as_view(), name='shopcategory'),
    path('ShopDetail/<str:id>/', onedaytwogether_view.ShopDetailView.as_view(), name='detail'),
    path('Contact/', onedaytwogether_view.ContactView.as_view(), name='contact'),
    path('Cart/', onedaytwogether_view.CartView.as_view(), name='cart'),
    path('Cart/Purchase/', onedaytwogether_view.PurchaseView.as_view(), name='purchase'),
    path('Cart/Delete/<str:id>/', onedaytwogether_view.CartDeleteView.as_view(), name='cartdelete'),
    path('Aboutus/', onedaytwogether_view.AboutusView.as_view(), name='Aboutus'),
    path('Login/', onedaytwogether_view.LoginView.as_view(), name='Login'),
    path('Signup/', onedaytwogether_view.SignupView.as_view(), name='Signup'),
    path('Logout/', onedaytwogether_view.LogoutView.as_view(), name='Logout'),
    path('CompleteProfile/', onedaytwogether_view.CompleteProfile.as_view(), name='CompleteProfile'),
    path('Onedaytowgther/Admin/Booking/', onedaytwogether_view.AdminBookingView.as_view(), name='AdminBooking'),
    path('Onedaytowgther/Admin/Booking/Approve/<str:id>/', onedaytwogether_view.AdminBookingApproveView.as_view(), name='AdminBookingApprove'),
    path('Onedaytowgther/Admin/Booking/Decline/<str:id>/', onedaytwogether_view.AdminBookingDeclineView.as_view(), name='AdminBookingDecline'),
    path('Booking/', onedaytwogether_view.BookingView.as_view(), name='Booking'),
    path('Booking/Delete/<str:id>/', onedaytwogether_view.BookingDeleteView.as_view(), name='Bookingdelete'),
    path('Account/', onedaytwogether_view.Userdata.as_view(), name='Account'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
