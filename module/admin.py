from django.contrib import admin

from .models import Module, Forum_wrap, Activitie_wrap, Wiki_wrap, Quiz_wrap, Material_wrap

admin.site.register(Module)
admin.site.register(Forum_wrap)
admin.site.register(Activitie_wrap)
admin.site.register(Wiki_wrap)
admin.site.register(Quiz_wrap)
admin.site.register(Material_wrap)