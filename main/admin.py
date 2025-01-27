from django.contrib import admin
from django.utils.html import format_html
from .models import County, Lake, SectionImage, ClubButtonLink, TutorialVideo, TutorialCategory, Product

# Check if SectionImage is already registered
if not admin.site.is_registered(SectionImage):
    @admin.register(SectionImage)
    class SectionImageAdmin(admin.ModelAdmin):
        list_display = ('section_name', 'css_identifier', 'image_preview')

        def image_preview(self, obj):
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)

        image_preview.short_description = "Preview"

# Check if ClubButtonLink is already registered
if not admin.site.is_registered(ClubButtonLink):
    @admin.register(ClubButtonLink)
    class ClubButtonLinkAdmin(admin.ModelAdmin):
        list_display = ('button_text', 'button_link')


# Models registration and customization
@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the county name in the admin list view


@admin.register(Lake)
class LakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'county')  # Display the lake name and its related county
    list_filter = ('county',)  # Add a filter for the county field
    search_fields = ('name',)  # Allow searching by lake name
    fieldsets = (
        (None, {
            'fields': ('name', 'county', 'google_map_iframe'),
            'description': 'Paste the full iframe HTML from Google Maps Embed for the selected lake.',
        }),
    )


@admin.register(TutorialCategory)
class TutorialCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TutorialVideo)
class TutorialVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'youtuber_account', 'date_added')
    list_filter = ('category', 'date_added')
    search_fields = ('title', 'youtuber_account')

    actions = ['duplicate_video']

    def duplicate_video(self, request, queryset):
        for video in queryset:
            video.id = None  # Set ID to None to create a new instance
            video.title = f"{video.title} (Copy)"
            video.save()

        self.message_user(request, f"{queryset.count()} video(s) duplicated successfully.")

    duplicate_video.short_description = "Duplicate selected videos"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'current_price', 'old_price', 'image_preview')

    def image_preview(self, obj):
        return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image_url)

    image_preview.short_description = "Preview"

    actions = ['duplicate_product']

    def duplicate_product(self, request, queryset):
        for product in queryset:
            product.id = None  # Set ID to None to create a new instance
            product.title = f"{product.title} (Copy)"
            product.save()

        self.message_user(request, f"{queryset.count()} product(s) duplicated successfully.")

    duplicate_product.short_description = "Duplicate selected products"
