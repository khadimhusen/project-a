from django.contrib import admin
from .models import Feed, Category, Tag ,FeedComment


# Register your models here.
@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ['author','title', 'description', 'price']


admin.site.register(Category)
# admin.site.register(Feed)
admin.site.register(Tag)
admin.site.register(FeedComment)