from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} {self.image} {self.created_at}'

    def likes_count(self):
        return self.likes.all().count()


class Like(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, blank=True, on_delete=models.CASCADE, related_name='likes')


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.author} {self.text} {self.created_at}'


