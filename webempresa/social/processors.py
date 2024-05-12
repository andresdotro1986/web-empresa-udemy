# se pone en el settings TEMPLATE --> context processors y sirve para usar contextos generales,
# sin tener  que ponerlo en cada funcion, se puede llamar desde cualquier template

from .models import Link

def ctx_dict(request):
    ctx={}
    links=Link.objects.all()
    for link in links:
        ctx[link.key]= link.url
    return ctx