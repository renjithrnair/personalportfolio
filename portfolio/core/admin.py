# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .views import *

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(RecentWork)
admin.site.register(Client)
