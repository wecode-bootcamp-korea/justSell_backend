from django.urls import path
from .views      import (
    SignUp, 
    SignIn, 
    InvitationCodeCheck,
    CompanyRegisterationImageUpload,
    OnlineDistributorCertificationImageUpload,
    BankingAccountImageUpload
)

urlpatterns = [
    path('/signup', SignUp.as_view()),
    path('/signin', SignIn.as_view()),
    path('/invitationcode', InvitationCodeCheck.as_view()),
    path('/companyregistertationimageupload', CompanyRegisterationImageUpload.as_view()),
    path('/onlinedistributorcertificationimageupload', OnlineDistributorCertificationImageUpload.as_view()),
    path('/bankingaccountimageupload', BankingAccountImageUpload.as_view()),
]