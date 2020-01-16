from django.urls import path
from .views      import ProductRegister, MainImageUpload, CategoryView

urlpatterns = [
    path('/productregister', ProductRegister.as_view()),
    path('/mainimageupload', MainImageUpload.as_view()),
    path('/categoryview', CategoryView.as_view()),
]