from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=255, default='')
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tag, self).save()


class Category(models.Model):
    title = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title


class Feed(models.Model):
    title = models.CharField(max_length=100, default='')
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    description = models.TextField(default='')
    author = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return f"Author:{self.author},Title: {self.title},Date: {self.date}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Feed, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])



class FeedComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by " + self.user.email

