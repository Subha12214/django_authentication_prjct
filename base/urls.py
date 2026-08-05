from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),
    path('delete_h/<int:id>',delete_h,name='delete_h'),
    path('complete_h/<int:id>',complete_h,name='complete_h'),
    path('delete_c/<int:id>',delete_c,name='delete_c'),
    path('restore_c/<int:id>',restore_c,name='restore_c'),
    path('delete_t/<int:id>',delete_t,name='delete_t'),
    path('restore_t/<int:id>',restore_t,name='restore_t'),
    path('complete_allh/',complete_allh,name='complete_allh'),
    path('delete_allh/',delete_allh,name='delete_allh')
]