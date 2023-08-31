from django.db import models
# Create your models here.
class Users(models.Model):
    login = models.CharField(max_length=255,
                            verbose_name="User login",
                            help_text="Enter a user login")
    mail = models.EmailField()
    password = models.CharField(max_length=255,
                            verbose_name="User password",
                            help_text="Enter a user password")
    class Meta:
        ordering = ('login',)
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.login
