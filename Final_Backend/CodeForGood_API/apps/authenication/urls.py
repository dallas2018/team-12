from django.conf.urls import url

from .views import * 


urlpatterns = [
    url(r'^register-user/?$' , RegistrationAPIView.as_view()),
    url(r'^login/?$', LoginAPIView.as_view()),
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^complete-user/?$', CompleteUserRetrieveAPIView.as_view()),
    url(r'^profile/?$',User_Profile_View.as_view()),

]

