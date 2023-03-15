from django.urls import path
from app1Webpage import views

urlpatterns=[
    path('', views.webpage, name="webpage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('contact_save/', views.contact_save, name="contact_save"),
    path('contactview/', views.contactview, name="contactview"),
    path('product/', views.product, name="product"),
    path('discategory/<itemcatg>', views.discategory, name="discategory"),
    path('prodetails/<int:dataid>', views.prodetails, name="prodetails"),
    path('login/',views.login,name='login'),
    path('loginsave/',views.loginsave,name='loginsave'),
    path('customerdetails/', views.customerdetails, name='customerdetails'),
    path('logoutfn/', views.logoutfn, name='logoutfn'),
    path('cart/', views.cart, name='cart'),
    path('cartview/', views.cartview, name='cartview'),
    path('deleteitem/<int:dataid>', views.deleteitem, name='deleteitem')

]