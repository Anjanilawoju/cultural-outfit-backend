"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.views import AddtoCartViewSet, HotDealsView,OurPicksView,DressListView, NewariDress, TamangDress, GurungDress, SherpaDress, MagarDress, TharuDress, NewArrival,get_dresses

from rest_framework.routers import DefaultRouter

# Create a router for the viewset
router = DefaultRouter()
router.register(r'cart', AddtoCartViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dresses/', DressListView.as_view(), name='dress-list'),
    path('dresses/<int:id>/',get_dresses , name='get_dresses'),
    path('hot-deals/', HotDealsView.as_view(), name='hot-deals'),
    path('our-picks/', OurPicksView.as_view(), name='our-picks'),
    path('newari/', NewariDress.as_view(), name='newari-dress'),
    path('tamang/', TamangDress.as_view(), name='tamang-dress'),
    path('gurung/', GurungDress.as_view(), name='gurung-dress'),
    path('sherpa/', SherpaDress.as_view(), name='sherpa-dress'),
    path('magar/', MagarDress.as_view(), name='magar-dress'),
    path('tharu/', TharuDress.as_view(), name='tharu-dress'),
    path('new-arrival/', NewArrival.as_view(),name='new-arrival'),
    path('', include(router.urls)), 
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
