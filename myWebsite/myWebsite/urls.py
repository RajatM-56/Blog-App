"""
URL configuration for myWebsite project.

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
from blog import views as blog_views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.Home.as_view(), name='home'),
    path('user/<str:username>/', blog_views.UserPostView.as_view(), name='user_posts'),
    path('about/', blog_views.about, name='about'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', 
            email_template_name='mail/password_reset_email.txt',
            subject_template_name='mail/password_reset_subject.txt'),
            name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name = 'users/password_reset_confirm.html',
        ), 
        name='password_reset_confirm'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
        name='password_reset_done'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
        name='password_reset_complete'),
    path('post/<int:pk>/', blog_views.PostView.as_view(), name='post'),
    path('posts/new/', blog_views.PostCreateView.as_view(), name='create_post'),
    path('posts/<int:pk>/update/', blog_views.PostUpdateView.as_view(), name='update_post'),
    path('posts/<int:pk>/delete/', blog_views.DeletePostView.as_view(), name='delete_post'),
    path('profile/<str:username>/', user_views.userProfile, name='user_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
