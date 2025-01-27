from bs4 import BeautifulSoup
from django.contrib.auth.models import AbstractUser
from django.db import models


class County(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Judet"
        verbose_name_plural = "Județele"


class Lake(models.Model):
    name = models.CharField(max_length=255)
    google_map_iframe = models.TextField()  # Contains the full iframe HTML
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='lakes')  # Add the ForeignKey here

    @property
    def google_map_src(self):
        # Parse the iframe and extract the src attribute
        try:
            soup = BeautifulSoup(self.google_map_iframe, 'html.parser')
            iframe = soup.find('iframe')
            return iframe['src'] if iframe else None
        except Exception:
            return None

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lacuri sau Balti"
        verbose_name_plural = "Lacuri sau Balti"


class SectionImage(models.Model):
    SECTION_CHOICES = [
        ('hero-section', 'Imaginea intra in pagina'),
        ('welcome-section', 'Imagine sectiunea de bine ati venit'),
        ('fishing-explore-section', 'Imagine sectiunea de explorare'),
        ('testimonial-section', 'Imagine sectiunea de testimonial'),
        ('promo-section', 'Sectiunea de promotii'),
    ]

    section_name = models.CharField(max_length=100, verbose_name="Numele modificari",
                                    help_text="Nume pentru urmarirea modificari")
    image = models.ImageField(upload_to='section_images/', verbose_name="Imagine",
                              help_text="Imaginea noua pe care o incarci.")
    css_identifier = models.CharField(
        max_length=100,
        choices=SECTION_CHOICES, verbose_name="Sectiunea la care vrei sa ii schimbi imaginea:",
        help_text="Identificatorul CSS pentru secțiune. In ce sectiune din prima pagina vrei sa schimbi poza."
    )

    def __str__(self):
        return f"{self.section_name} ({self.css_identifier})"

    def get_image_url(self):
        if self.image and self.image.url:
            return self.image.url
        return '/static/images/default.png'

    class Meta:
        verbose_name = "Sectiunea de modificarea a pozelor"
        verbose_name_plural = "Sectiunea de modificarea a pozelor"


class ClubButtonLink(models.Model):
    button_text = models.CharField(max_length=100, default="Alăturați-vă clubului",
                                   help_text="Textul care vrei sa fie afisat pe butonul verde")
    button_link = models.URLField(help_text="Introdu URL unde vrei sa redirectioneze butonul verde")

    def __str__(self):
        return self.button_text

    class Meta:
        verbose_name = "Actualizarea linkului de la butonul verde"
        verbose_name_plural = "Actualizarea linkului de la butonul verde"


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    nume = models.CharField(max_length=255)
    oras = models.CharField(max_length=255)
    data_nasteri = models.DateField(null=True, blank=True)
    poza_profil = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    numar_telefon = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Actualizarea linkului de la butonul verde"
        verbose_name_plural = "Actualizarea linkului de la butonul verde"


css_identifier = models.CharField(
    max_length=100,
    help_text="CSS identifier for the section.",
    unique=True,
    default="default-section"
)


class TutorialCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie Tutorial"
        verbose_name_plural = "Categorii Tutoriale"


class TutorialVideo(models.Model):
    title = models.CharField(max_length=255)
    iframe_code = models.TextField(help_text="Codul iframe pentru video-ul YouTube.")
    category = models.ForeignKey(TutorialCategory, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="videos")
    youtuber_account = models.CharField(max_length=255, help_text="Numele canalului YouTube al creatorului.",
                                        blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Video Tutorial"
        verbose_name_plural = "Videouri Tutoriale"


class Product(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField()
    category = models.CharField(max_length=255, blank=True, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_url = models.URLField()  # Link către produs

    def __str__(self):
        return self.title
