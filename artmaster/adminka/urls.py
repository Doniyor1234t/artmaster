from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', menyu),
    path('authorization', userLogin),
    path('logout', userLogout),
    path('listframe', listframe),
    path('listsomething', listsomething),
    path('listart', listart),
    path('addart', addart),
    path('addframe', addframe),
    path('addsomething', addsomething),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
