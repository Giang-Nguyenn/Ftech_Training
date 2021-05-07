from .models import Tenant1

def get_tenants_map():
    return {
        "host1.localhost": "host1",
        "host2.localhost": "host2",
    }

def hostname_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(':')[0].lower()


def tenant_from_request(request):
    hostname = hostname_from_request(request)
    subdomain_prefix = hostname.split('.')[0]
    return Tenant.objects.filter(subdomain_prefix=subdomain_prefix).first()