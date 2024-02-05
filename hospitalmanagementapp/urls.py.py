from django.urls import path
from.views import home, pat,show,edit,update,delete,aboutus,submit

urlpatterns=[
    path('',home,name='home'),
    path('aboutus',aboutus,name='aboutus'),
    path('submit',submit,name='submit'),
    path('pat',pat,name='pat'),
    path('show',show,name='show'),
    path('edit/<int:id>',edit,name='edit'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
]

