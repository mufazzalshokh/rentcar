from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class PostTagModel(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post tag'
        verbose_name_plural = 'post tags'


class PostModel(models.Model):
    title = models.CharField(max_length=512)
    image = models.ImageField(upload_to='posts')
    content = RichTextUploadingField()
    brand = models.CharField(max_length=20)
    product_code = models.CharField(max_length=30)
    # reward_point
    availability = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()
    tags = models.ManyToManyField(PostTagModel, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
