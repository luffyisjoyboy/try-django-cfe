from django.contrib import admin
from django.urls import path, include
from .views import home_view
from accounts.views import login_view, logout_view, register_view

urlpatterns = [
    path('', home_view),
    path('pantry/recipes/', include('recipes.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
]
