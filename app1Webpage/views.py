from django.shortcuts import render,redirect
from django.contrib import messages
from app1.models import registeration_data,category_data,product_data,contact_data
from app1Webpage.models import Customerdetails

# Create your views here.
def webpage(request):
    details = category_data.objects.all()
    return render(request,"homepage.html",{'details':details})

def aboutpage(request):
    return render(request,"about.html")

def contactpage(request):
    return render(request,"contact.html")

def contact_save(request):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('mail')
        sb = request.POST.get('sub')
        ms = request.POST.get('message')

        obj = contact_data(name=na, email=em, subject=sb, message=ms)
        obj.save()
        return redirect(contactpage)
def contactview(request):
    details = contact_data.objects.all()
    return render(request,"contact_Details.html",{'details':details})

def product(request):
    details = product_data.objects.all()
    return render(request,"products.html",{'details':details})

def discategory(request, itemcatg):
    data = category_data.objects.all()
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    details = product_data.objects.filter(category=itemcatg)
    context = {
        'details': details,
        'catg': catg,
        'data': data
    }
    return render(request, "displaycategory.html", context)

def prodetails(request, dataid):
    details = product_data.objects.get(id=dataid)
    return render(request,"productdetail.html", {"details":details})
def login(request):
    return render(request,"customerloginpage.html")

def loginsave(request):
    if request.method=="POST":
        u = request.POST.get('user')
        e = request.POST.get('email')
        p = request.POST.get('pass')
        c = request.POST.get('cpass')
        if p == c:
            obj = Customerdetails(username=u,email=e,password=p,confirmpassword=c)
            obj.save()
            messages.success(request,"User Register Successfully")
            return redirect(login)
        else:
            messages.warning(request,"Sorry.... Invalid Username Or Password")
            return render(request,'customerloginpage.html',{'msg':"Sorry......password not matched "})

def customerdetails(request):
    if request.method == "POST":
        u = request.POST.get('user')
        p = request.POST.get('pass')
        if Customerdetails.objects.filter(username=u, password=p).exists():
            # obj = LoginRegister(username=u, password=p).values('email','id').first()
            request.session['user']=u
            request.session['pass']=p
            messages.success(request,"User Login successfully")

            # request.session['email']=data['email']
            # request.session['userid']=data['id']
            return redirect(webpage)
        else:
            messages.warning(request,"Sorry.... Invalid Username Or Password")

            return render(request, 'customerloginpage.html', {'msg': "Sorry... password not matched."})

def cart(request):
    return render(request,"Cart_Product.html")




