"""
URL configuration for Blog30 project.

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
from django.conf.urls.static import static

from Blog30 import settings
from posts.views import hello_view, now_date_view, goodbye_view
from products import views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('hello/', hello_view),
    path('now_date/', now_date_view),
    path('goodbye/', goodbye_view),

    path('products/', views.products_view),
    path('products/<int:id>/', views.product_detail_view),
    path('products/create/', views.product_create_view),
    path('products/categories/create', views.category_create_view),
    path('products/review/create', views.review_create_view),

    path('categories/', views.categories_view),

    path('users/register/', users_views.register_view),
    path('users/login/', users_views.login_view),
    path('users/logout/', users_views.logout_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
