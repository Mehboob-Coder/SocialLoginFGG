from django.shortcuts import render

# Create your views here.
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from SocialLoginFGG.settings import GOOGLE_REDIRECT_URL
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = GOOGLE_REDIRECT_URL
    client_class = OAuth2Client

class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return "http://127.0.0.1"
    
class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = "http://127.0.0.1:8000/accounts/github/login/callback/"
    client_class = OAuth2Client

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    # callback_url = "http://127.0.0.1:8000/dj-rest-auth/facebook/callback/"
    client_class = OAuth2Client

