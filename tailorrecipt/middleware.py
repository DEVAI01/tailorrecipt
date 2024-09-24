# from django.shortcuts import redirect
# from django.urls import reverse

# class LoginRequiredMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # URLs that don't require login
#         open_urls = [reverse('login'), reverse('register'), reverse('index')]

#         if not request.session.get('email') and request.path not in open_urls:
#             return redirect('login')

#         response = self.get_response(request)

#         # Add cache control headers to prevent caching
#         response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
#         response['Pragma'] = 'no-cache'
#         response['Expires'] = '0'

#         return response
    
    
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import urlencode

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URLs that don't require login
        open_urls = [reverse('login'), reverse('register'), reverse('index'), reverse('logout')]

        if not request.session.get('email') and request.path not in open_urls:
            params = urlencode({'next': request.get_full_path()})
            return redirect(f"{reverse('login')}?{params}")

        response = self.get_response(request)

        # Add cache control headers to prevent caching
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'

        return response