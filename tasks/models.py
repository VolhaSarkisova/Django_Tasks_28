from django.db import models
from users.models import Users

STATUSES = (
    ("1", "В ожидании"),
    ("2", "В процессе"),
    ("3", "Завершено"),
)

class Tasks(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name="Task name",
                            help_text="Enter a task name")
    description = models.TextField(max_length=3000,
                            verbose_name="Task description",
                            help_text="Enter a task description")
    users = models.ForeignKey(Users,
                              related_name='tasks',
                              on_delete=models.CASCADE)
    status = models.CharField(max_length=11,
                              choices=STATUSES,
                              default="В ожидании")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField()

    class Meta:
        ordering = ('-date_creation',)
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name