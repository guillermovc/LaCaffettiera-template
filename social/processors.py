from .models import Link

def ctx_dict(request):
    ctx = {}
    # Consulta a la base de datos
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
        
    return ctx