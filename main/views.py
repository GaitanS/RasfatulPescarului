from django.shortcuts import render, get_object_or_404
from .models import County, SectionImage, ClubButtonLink, TutorialVideo, TutorialCategory
from django.http import JsonResponse

from .models import Product


def homepage(request):
    products = Product.objects.all()[:4]  # Obține ultimele 20 de produse
    section_images = SectionImage.objects.all()
    club_button = ClubButtonLink.objects.first()
    return render(request, 'index/index.html', {
        'section_images': section_images,
        'club_button': club_button,
        'products': products
    })


def harta(request):
    club_button = ClubButtonLink.objects.first()
    section_images = SectionImage.objects.all()
    counties = County.objects.prefetch_related('lakes').all()
    return render(request, 'harta.html', {
        'counties': counties,
        'section_images': section_images,
        'club_button': club_button,

    })


def tutoriale(request, category_id=None):
    club_button = ClubButtonLink.objects.first()
    section_images = SectionImage.objects.all()
    categories = TutorialCategory.objects.all()
    if category_id:
        selected_category = get_object_or_404(TutorialCategory, id=category_id)
        videos = selected_category.videos.all()
    else:
        selected_category = None
        videos = TutorialVideo.objects.all()

    return render(request, 'tutoriale.html', {
        'categories': categories,
        'videos': videos,
        'selected_category': selected_category,
        'section_images': section_images,
        'club_button': club_button,

    })


# Admin Dashboard
def admin_dashboard(request):
    return render(request, "admin/dashboard.html")


def filter_videos_by_category(request, category_id):
    videos = TutorialVideo.objects.filter(category__id=category_id)
    video_data = [
        {
            "title": video.title,
            "iframe_code": video.iframe_code,
            "youtuber_account": video.youtuber_account,
            "date_added": video.date_added.strftime('%d %B %Y'),
        }
        for video in videos
    ]
    return JsonResponse({"videos": video_data})
