from django.urls import path
from django.contrib.auth.views import LoginView

from .views import (
                    #login_view,
                    get_cookie_view,
                    set_cookie_view,
                    get_session_view,
                    set_session_view,
                    logout_view,
                    MylogoutView,
                    AboutMeView,
                    RegistrView,
                    HelloVIew,
) 

app_name = 'myauth'

urlpatterns = [
    #path("login/", login_view, name="login"),
    path("login/", LoginView.as_view(
        template_name="myauth/login.html",
        redirect_authenticated_user=True,
        ),
        name="login"),
    path("cookie/get/", get_cookie_view, name="cookie-get"),
    path("cookie/set/", set_cookie_view, name="cookie-set"),

    path("session/get/", get_session_view, name="session-get"),
    path("session/set/", set_session_view, name="session-set"),

    path("logout/", MylogoutView.as_view(), name="logout"),
    path("about-me/", AboutMeView.as_view(), name="about-me"),
    path("register/", RegistrView.as_view(), name="register"),

    path("hello/", HelloVIew.as_view(), name="hello"),
]