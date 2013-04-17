from django.http import HttpResponse
from django.template import Context, loader

from core.models import Article

def index(request):
    article_list = Article.objects.all()
    template = loader.get_template('core/list_site_content.html')
    context = Context({'article_list': article_list})

    return HttpResponse(template.render(context))
