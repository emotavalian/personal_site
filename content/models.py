from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator, URLValidator
from django.core.exceptions import ValidationError
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# for checking size of file for bigger video file can code another method
def file_size_limit(value, max_size_mb=5):
    limit = max_size_mb * 1024 * 1024
    if value.size > limit:
        raise ValidationError(f"File size must be under {max_size_mb}MB")


class Post(models.Model):
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()

    image = models.ImageField(blank=True, null=True,
        upload_to='images/',
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg']), file_size_limit]
    )
    video = models.FileField(blank=True, null=True,
        upload_to='videos/',
        validators=[FileExtensionValidator(['mp4', 'mov']), file_size_limit]
    )
    video_url = models.URLField(validators=[URLValidator()],blank=True, null=True)



    file = models.FileField(
        upload_to='files/',
        validators=[FileExtensionValidator(['pdf', 'docx']), file_size_limit]
    )

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# for watching youtube url it should be embedded
    def embed_youtube_url(self):
        if self.video_url and 'https://www.youtube.com' in self.video_url:
            video_id = self.video_url.split('v=')[-1].split('&')[0]
            return f"https://www.youtube.com/embed/{video_id}"
        return None




    def __str__(self):
        return self.title
