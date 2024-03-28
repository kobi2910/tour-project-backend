from django.db import models

class Contact_us(models.Model):
    """
    Model representing a contact form submission.
    """

    name       = models.CharField(max_length=50)
    email      = models.EmailField()
    subject    = models.CharField(max_length=100)
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

