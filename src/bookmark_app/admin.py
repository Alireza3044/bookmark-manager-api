from django.contrib import admin
from bookmark_app import models

admin.site.register([models.Category, models.Bookmark])
