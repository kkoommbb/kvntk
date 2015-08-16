from django.contrib import admin

from .models import Article

from .models import Painter

from .models import Author

from .models import Category

from .models import Magazine




admin.site.register(Painter)

admin.site.register(Author)

admin.site.register(Category)

admin.site.register(Magazine)



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors', 'magazine')
    list_filter = ['magazine']

admin.site.register(Article, ArticleAdmin)

# Register your models here.
