"""linksphere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from social import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',views.SignupView.as_view(),name="signup"),
    path('',views.SigninView.as_view(),name="signin"),
    path('index',views.IndexView.as_view(),name="index"),
    path('logout',views.SignoutView.as_view(),name="signout"),
    path("profile/<int:pk>/change",views.ProfileUpdateView.as_view(),name='profile-update'),
    path("profile/<int:pk>",views.ProfileDetailsView.as_view(),name="profile-details"),
    path("profile/all",views.ProfileListView.as_view(),name="profile-list"),
    path("profile/<int:pk>/follow",views.FollowView.as_view(),name="follow"),
    path('post/<int:pk>/like',views.PostLikeView.as_view(),name="like"),
    path('post/<int:pk>/comments/add',views.CommentView.as_view(),name="comment"),
    path("profile/<int:pk>/block",views.ProfileBlockView.as_view(),name="block"),
    path("stories/add",views.StorieCreateView.as_view(),name="story-create")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
