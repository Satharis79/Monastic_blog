from django.urls import path
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from .views import MonkView, signup, MonkUpdateView, monk_list

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='main/login.html', next_page='home'), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/<pk>', MonkView.as_view(), name='profile'),
    path('update/', login_required(MonkUpdateView.as_view()), name='update'),
    path('signup/', signup, name='signup'),    
    path('monastery/', monk_list, name='monastery'),    
]