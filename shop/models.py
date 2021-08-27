from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BrandModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class CarTagModel(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'car tag'
        verbose_name_plural = 'car tags'


class CarModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cars')
    price = models.FloatField()
    discount = models.PositiveIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    short_description = models.TextField()
    long_description = RichTextUploadingField()
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='cars'
    )
    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.PROTECT,
        related_name='cars'
    )
    tags = models.ManyToManyField(
        CarTagModel,
        related_name='cars'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'car'
        verbose_name_plural = 'cars'
