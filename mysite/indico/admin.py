from django.contrib import admin
from indico.models import About, AboutItem, Slider, SliderItem
from solo.admin import SingletonModelAdmin


# Register your models here.

admin.site.register(SliderItem)
admin.site.register(Slider,SingletonModelAdmin)
admin.site.register(AboutItem)
admin.site.register(About,SingletonModelAdmin)