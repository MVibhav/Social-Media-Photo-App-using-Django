from django.shortcuts import render,redirect
from .forms import LoginForm,RegistrationForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserEditForm,ProfileEditForm
from posts.models import Post
# Create your views here.
def user_login(request):
     if(request.method=='POST'):
          form=LoginForm(request.POST)
          if form.is_valid():
               data=form.cleaned_data
               user=authenticate(request,username=data['username'],password=data['password'])
               if user is not None:
                    login(request, user)
                    return redirect('../../posts/feed')
               else:
                    return HttpResponse("Invalid credentials")
     else:
          form=LoginForm()
     return render(request,'users/login.html',{'form':form})

@login_required
def index(request):
     current_user=request.user
     posts=Post.objects.filter(user=current_user).order_by('-created')
     profile=Profile.objects.filter(user=current_user).first()
     return render(request,'users/index.html',{'posts':posts,'profile':profile})

def register(request):
     if request.method=='POST':
          user_form=RegistrationForm(request.POST)
          if(user_form.is_valid()):
               new_user=user_form.save(commit=False)
               new_user.set_password(user_form.cleaned_data['password'])
               new_user.save()
               Profile.objects.create(user=new_user)
               return redirect('login')
     else:
          user_form=RegistrationForm()
     return render(request,'users/register.html',{'user_form':user_form})

@login_required
def edit(request):
     if request.method=='POST':
          user_form=UserEditForm(instance=request.user,data=request.POST)
          profile_form=ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
          if(user_form.is_valid() and profile_form.is_valid()):
               user_form.save()
               profile_form.save()
               return redirect('index')
     else:
          user_form=UserEditForm(instance=request.user)
          profile_form=ProfileEditForm(instance=request.user.profile)
     return render(request,'users/edit.html',{'user_form':user_form,'profile_form':profile_form})