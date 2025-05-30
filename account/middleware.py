from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
from blueapps.account.models import User


class JWTAuthenticationMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        全局 JWT 鉴权中间件，使 request.user 可用
        """
        # if getattr(request., "login_exempt", False):
        #     return None
        if getattr(request, "_login_exempt", False):
            return None
        # request.user = User.objects.get(username="admin")
        # request._cached_user = request.user
        # return None
        auth = JWTAuthentication()
        try:
            auth_result = auth.authenticate(request)
            if auth_result:
                user, validated_token = auth_result
                request.user = user
                request._cached_user = user
                return None
            
        except (InvalidToken, AuthenticationFailed):
            pass
        request.user = AnonymousUser()
        return HttpResponseRedirect(redirect_to="/#/login/")
