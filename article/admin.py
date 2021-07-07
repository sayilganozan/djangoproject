from django.contrib import admin

# Register your models here.
#Modellerimizi admin panelinde görmek istiyorsak register model yapmalıyız.


# aynı klasördeki model'e git:
from .models import Article,Comment


#Admin panelinde göstermek için kayıt etmemiz gerekiyor:

admin.site.register(Comment)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    list_display_links = ["title","created_date"]
    search_fields = ["title"]

    list_filter = ["created_date"]

    # article admin ile article'ı bağlamak için;
    class Meta: 

        model = Article

