from django.shortcuts import render,redirect
from .models import photo,addcategory,userprofile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    category = request.GET.get('category')
    categories = addcategory.objects.all()
    
    if category:
        photos = photo.objects.filter(categories__category=category)
    else:
        photos = photo.objects.all()
    
    context = {
        'categories': categories,
        'photos': photos,
    } 
    return render(request, "index.html", context)



def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        cat_id = request.POST.get('category')
        image = request.FILES.get('image')
        des = request.POST.get('description')
        cat = addcategory.objects.get(pk=cat_id)  
        final_image = photo.objects.create(user = request.user,categories=cat, title=title, description = des, image=image)
        return redirect('home')
    categories = addcategory.objects.all()
    context = {
        'category': categories,
    }
    return render(request, 'add.html', context)

def viewPhoto(request,pk):
    photos = photo.objects.get(id=pk)
    categories = addcategory.objects.all()
    context = {
        'category' : categories,
        'photos' : photos
    }
    return render(request,'photo.html',context)

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        print(username,password1,password2)
        if password1 != password2:
            messages.error(request,"password is not matched")
            return redirect('register')
        user=User.objects.create_user(username=username ,password=password1 )
        messages.success(request,"account is created just now")
        return redirect('userlogin')
    return render(request,"register.html")
    
def userlogin(request):
    if request.method == "POST":
        usrname=request.POST.get('username')
        password1=request.POST.get('password')
        user=authenticate(request,username=usrname,password=password1)
        if user == None:
            messages.error(request,"check your password or username")
            return redirect('userlogin')
        login(request,user)
        return redirect('home')
    
    return render(request,"login.html")

def userlogout(request):
    logout(request)
    return redirect('userlogin')

def updateImg(request,pk):
    if request.method=='POST':
        title=request.POST.get('title')
        cat=request.POST.get('category')
        cate=addcategory.objects.get(id=cat)
        image=request.FILES.get('image')
        imgs=photo.objects.get(id=pk)
        # print(title,cat,img)
        if image ==None:
        #     final_img=photo.objects.update(user=request.user,catogories=cate,title=title1,description=text)

        # final_img=photo.objects.update(user=request.user,catogories=cate,title=title1,img=img1,description=text)
            imgs.title=title
            imgs.categories=cate
            imgs.save()

       
        imgs.title=title
        imgs.categories=cate
        imgs.image=image
        imgs.save()
        

        return redirect('home')
    category=addcategory.objects.all()
    photos=photo.objects.get(id=pk)
    
    context={
        'category':category,
        'photo':photos,
    } 
    return render(request,"update.html",context)

def delete(request,pk):
    photo.objects.get(id=pk).delete()
    return redirect("home")

def search(request):
    if request.method == "POST":
        search_term = request.POST.get("search")
        photos = photo.objects.filter(title__contains=search_term)
    else:
        photos = photo.objects.all()
    categories = addcategory.objects.all()
    context = {
        'category': categories,
    }
    return render(request, 'search.html', {'photos': photos, **context})

from django.core.exceptions import ObjectDoesNotExist

def userdetails(request):
    user = request.user
    photos = photo.objects.filter(user=user)
    counts = photos.count()
    try:
        profile = userprofile.objects.get(user=user)
    except ObjectDoesNotExist:
        profile = None
    context={
        'user': user,
        'photos': photos,
        'count': counts,
        'profile': profile,
    }
    return render(request,'userdetails.html',context)

@login_required
def editProfileImage(request):
    profile = userprofile.objects.get(user=request.user)
    if request.method == 'POST':
        print("hello")
        image = request.FILES.get('image')
        profile.image = image
        profile.save()
        return redirect('userdetails')

    return render(request,'editProfileImage.html')
@login_required
def editProfile(request):
    user = request.user
    try:
        profile = user.userprofile
    except userprofile.DoesNotExist:
        profile = userprofile.objects.create(user=user)
    if request.method == 'POST':
        uname = request.POST.get('username')
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        about = request.POST.get('about')
        user.first_name = fname
        user.last_name = lname
        user.username = uname
        user.email = email
        if profile:
            profile.about = about
            if 'image' in request.FILES:
                profile.image = request.FILES['image']
            profile.save()
        user.save()
        return redirect('userdetails')
    return render(request, 'editProfile.html', {'user': user, 'profile': profile})



def myPhotos(request):
    user_photos = photo.objects.filter(user=request.user)
    return render(request, 'myPhotos.html', {'photos': user_photos})



