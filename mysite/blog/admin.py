from django.contrib import admin
from .models import Post

admin.site.register(Post)

from .models import Voetbalspelers

admin.site.register(Voetbalspelers)
