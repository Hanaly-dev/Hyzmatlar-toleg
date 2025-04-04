from django.contrib import admin
from .models import*

admin.site.register(Hyzmat)
admin.site.register(Toleg)
admin.site.register(Profil)
admin.site.register(Habarlar)



admin.site.site_header = "Töleg hyzmatlarynyň we hasabatlarynyň dolandyryş paneli"
admin.site.site_title = "Dolandyryş Paneli"
admin.site.index_title = ""