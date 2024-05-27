

from django.views.generic.base import TemplateView

from indico.models import Slider
# Create your views here.

class Index (TemplateView):
    template_name="indico/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all().first()

        return context
    
class About (TemplateView):
    template_name="indico/about-us.html"


class Service (TemplateView):
    template_name="indico/services-1.html"


class Contact (TemplateView):
    template_name="indico/contact.html"