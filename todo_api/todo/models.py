from django.db import models
from django.contrib.auth.models import User

NEW_STATUS = "NEW"
COMPLETE_STATUS = "COMPLETE"
STATUS_CHOICE = [
    (NEW_STATUS, NEW_STATUS),
    (COMPLETE_STATUS, COMPLETE_STATUS)
]

class Todo(models.Model):
    name                    = models.CharField(max_length=256)
    description             = models.CharField(max_length=512)
    user_id                 = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_completion      = models.DateTimeField()
    status                  = models.CharField(
                                max_length=30,
                                choices=STATUS_CHOICE,
                                default=NEW_STATUS,
                            )
    date_of_creation        = models.DateTimeField(auto_now_add=True)
    date_of_modification    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} | {self.name}" 


