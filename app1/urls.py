from django.urls import path
from app1 import views


urlpatterns=[
    path('sampl_page/',views.sampl_page, name="sampl_page"),
    path('Add_admin/',views.Add_admin, name="Add_admin"),
    path('show_data/',views.show_data, name="show_data"),
    path('peopledata/', views.peopledata, name="peopledata"),
    path('editpage/<int:dataid>/', views.editpage, name="editpage"),
    path('updatedata/<int:dataid>/', views.updatedata, name="updatedata"),
    path('deletedata/<int:dataid>/', views.deletedata, name="deletedata"),
    path('category/', views.category, name="category"),
    path('categoryitem/', views.categoryitem, name="categoryitem"),
    path('items/', views.items, name="items"),
    path('edititems/<int:dataid>/', views.edititems, name="edititems"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name="updatecategory"),
    path('deledata/<int:dataid>/', views.deledata, name="deledata"),
    path('adproduct/', views.adproduct, name="adproduct"),
    path('products/', views.products, name="products"),
    path('productview/', views.productview, name="productview"),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name="updateproduct"),
    path('deleproduct/<int:dataid>/', views.deleproduct, name="deleproduct"),
    path('logindata/', views.logindata, name="logindata"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('customerlogout/', views.customerlogout, name="customerlogout")
]