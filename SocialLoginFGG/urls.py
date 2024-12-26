from django.contrib import admin
from django.urls import path, include

from accounts.views import GoogleLoginView, UserRedirectView, GithubLogin, FacebookLogin
from rest_framework.response import Response
from rest_framework.views import APIView
class APIRootView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            'google_login': request.build_absolute_uri('/google/'),
            'github_login': request.build_absolute_uri('/github/'),
            'facebook_login': request.build_absolute_uri('/facebook/'),
        })
 
urlpatterns = [

 
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls'), name='socialaccount_signup'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('google/', GoogleLoginView.as_view(), name='google_login'),
    path('github/', GithubLogin.as_view(), name='github_login'),
    path('facebook/', FacebookLogin.as_view(), name='facebook_callback'),
    path('redirect/', UserRedirectView.as_view(), name='redirect'),
    path('', APIRootView.as_view(), name='api_root')
]