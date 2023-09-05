from django.db import models
from django.contrib.auth.models import User
from tasks.models import Tasks
from users.models import Users


# from django.contrib.auth.models import User


# Create your models here.
class Comments(models.Model):
    task = models.ForeignKey(Tasks,
                             on_delete=models.CASCADE,
                             related_name="comments_task")
    user = models.ForeignKey(Users,
                             on_delete=models.CASCADE,
                             related_name="comments_user")
    text = models.TextField(max_length=3000,
                            verbose_name="Comment",
                            help_text="Enter a comment")
    date_creation = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name='replies')

    def __str__(self):
        return f"{self.user} ({self.date_creation}) comment: {self.text}"

    class Meta:
        verbose_name_plural = "Comments"
        ordering = ("-date_creation", )

    @property
    def children(self):
        return Comments.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False