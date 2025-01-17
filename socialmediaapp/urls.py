"""
URL configuration for socialmediaapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import user_login,index,register,edit
from posts.views import post_create,feed,like_post
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',index,name='index'),
    path('users/login/',user_login,name='login'),
    path('users/logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('users/password_change/',auth_views.PasswordChangeView.as_view(template_name='users/password_change_form.html'),name='password_change'),
    path('users/password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),name='password_change_done'),
    path('users/password_reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset_form.html'),name='password_reset'),
    path('users/password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('users/reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('users/reset/done',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('users/register/',register,name='register'),
    path('users/edit/',edit,name='edit'),
    path('posts/create/',post_create,name='post_create'),
    path('posts/feed/',feed,name="feed"),
    path('posts/like/',like_post,name="like")
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
