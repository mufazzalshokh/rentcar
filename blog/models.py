from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    video = models.FileField(upload_to='videos/%y', null=True, blank=True)
    content = RichTextUploadingField()
    brand = models.CharField(max_length=20)
    product_code = models.CharField(max_length=30)
    availability = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    tags = models.ManyToManyField(PostTagModel, related_name='posts')
    short_description = models.TextField(null=True, blank=True)
    long_description = RichTextField(null=True, blank=True)
    extra_content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_prev(self):
        return self.get_previous_by_created_at()

    def get_next(self):
        return self.get_next_by_created_at()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class CommentModel(models.Model):
    post = models.ForeignKey(
        PostModel,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name=_('post')
    )
    name = models.CharField(max_length=30, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=_('phone'))
    comment = models.TextField(verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


def __str__(self):
    return self.name


class Meta:
    verbose_name = _('comment')
    verbose_name_plural = _('comments')
