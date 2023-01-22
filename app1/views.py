from django.contrib.auth import  authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from app1.models import registeration_data,category_data,product_data
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def sampl_page(request):
    return render(request,"index.html")
def Add_admin(request):
    return render(request,"Addadmin.html")
def show_data(request):
    if request.method=="POST":
        na = request.POST.get('name')
        mb = request.POST.get('mobile')
        em = request.POST.get('mail')
        im = request.FILES['img[]']
        un = request.POST.get('name2')
        pa = request.POST.get('pass')
        cp = request.POST.get('cpass')
        obj = registeration_data(name=na, mobile=mb, email=em,image=im, username=un, password=pa, confirmpassword=cp)
        obj.save()
        return redirect(Add_admin)
def peopledata(request):
    details = registeration_data.objects.all()
    return render(request,"showdata.html", {'details':details})
def editpage(request,dataid):
    details= registeration_data.objects.get(id=dataid)
    print(details)
    return render(request,"Editdata.html",{'details':details})
def updatedata(request, dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        mb = request.POST.get('mobile')
        em = request.POST.get('mail')
        try:
            img = request.FILES['img[]']
            fs = FileSystemStorage()
            im = fs.save(img.name, img)
        except MultiValueDictKeyError:
            im=registeration_data.objects.get(id=dataid).image
        un = request.POST.get('name2')
        pa = request.POST.get('pass')
        cp = request.POST.get('cpass')
        registeration_data.objects.filter(id=dataid).update(name=na, mobile=mb, email=em,image=im, username=un, password=pa, confirmpassword=cp)
        return redirect(peopledata)
def deletedata(request, dataid):
    data = registeration_data.objects.filter(id=dataid)
    data.delete()
    return redirect(peopledata)
def category(request):
    return render(request,"Addcategory.html")
def categoryitem(request):
    if request.method=="POST":
        na = request.POST.get('name')
        ds = request.POST.get('content')
        im = request.FILES['img[]']
        obj = category_data(name=na, content=ds, image=im)
        obj.save()
        return redirect(category)
def items(request):
    details = category_data.objects.all()
    return render(request, "categorydata.html", {'details': details})
def edititems(request,dataid):
    details= category_data.objects.get(id=dataid)
    print(details)
    return render(request,"Editcategory.html",{'details':details})
def updatecategory(request, dataid):
    if request.method=="POST":
        na = request.POST.get('name')
        ds = request.POST.get('content')
        try:
            img = request.FILES['img[]']
            fs = FileSystemStorage()
            im = fs.save(img.name, img)
        except MultiValueDictKeyError:
            im=category_data.objects.get(id=dataid).image
        category_data.objects.filter(id=dataid).update(name=na, content=ds, image=im,)
        return redirect(items)
def deledata(request, dataid):
    data = category_data.objects.filter(id=dataid)
    data.delete()
    return redirect(items)
def adproduct(request):
    details=category_data.objects.all()
    return render(request, "Addproduct.html",{'details':details})
def products(request):
    if request.method=="POST":
        cat = request.POST.get('cat')
        na = request.POST.get('name')
        rs = request.POST.get('price')
        qn = request.POST.get('quantity')
        ds = request.POST.get('content')
        im = request.FILES['img[]']
        obj = product_data(category=cat,name=na, price=rs, quantity=qn, descrption=ds, image=im)
        obj.save()
        return redirect(adproduct)
def productview(request):
    details = product_data.objects.all()
    return render(request,"displayproduct.html",{'details':details})
def editproduct(request,dataid):
    details= product_data.objects.get(id=dataid)
    da = category_data.objects.all()
    return render(request,"EditProducts.html",{'details':details, 'da':da})
def updateproduct(request, dataid):
    if request.method=="POST":
        cat = request.POST.get('cat')
        na = request.POST.get('name')
        rs = request.POST.get('price')
        qn = request.POST.get('quantity')
        ds = request.POST.get('content')
        try:
            img = request.FILES['img[]']
            fs = FileSystemStorage()
            im = fs.save(img.name, img)
        except MultiValueDictKeyError:
            im=product_data.objects.get(id=dataid).image
        product_data.objects.filter(category=cat,name=na, price=rs, quantity=qn, descrption=ds, image=im)
        return redirect(productview)
def deleproduct(request, dataid):
    data = product_data.objects.get(id=dataid)
    data.delete()
    return redirect(productview)
def logindata(request):
    return render(request,"adminlogin.html")
def loginpage(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(sampl_page)
            else:
                return redirect(logindata)
        else:
            return redirect(logindata)
def customerlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(logindata)



