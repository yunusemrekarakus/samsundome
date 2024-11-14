import requests
from .models import İzleyizi
from django.utils import timezone

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        ip_address = self.get_client_ip(request)
        location = self.get_location(ip_address)
        device_info = self.get_device_info(request)

        İzleyizi.objects.create(
            ip_address=ip_address,
            location=location,
            device_info=device_info
        )

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_location(self, ip_address):
        # İp adresini kullanarak lokasyon bilgisini almak için uygun bir servis kullanılabilir.
        # Bu örnekte, bir API çağrısı yaparak ipstack servisini kullanıyoruz.
        api_key = '38fa5f28321b4f13b979efec492a72e9'
        url = f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}'
        response = requests.get(url)
        data = response.json()
        return data.get('city', '')

    def get_device_info(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        return user_agent