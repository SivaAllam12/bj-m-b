from django.db import models


class Blog(models.Model):
    title=models.CharField(max_length=300)
    pub_date=models.DateField()
    body=models.TextField(max_length=300)
    image=models.ImageField()

    def __str__(self):
        return self.title;