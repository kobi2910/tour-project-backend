from django.db import models
# from django.contrib.auth.models import User
from user_accounts.models import CustomUser
from django.utils import timezone

class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (str): The title of the post.
        content (str): The content of the post.
        author (CustomUser): The author of the post. only is_guide == True can create a post.
        date (datetime): The date and time when the post was created.
    """
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey(
        CustomUser,
        to_field='username',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(default=timezone.now)

