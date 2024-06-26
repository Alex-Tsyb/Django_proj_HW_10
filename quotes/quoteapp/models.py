from django.db import models


class Author(models.Model):
    fullname = models.CharField(max_length=100, null=False, unique=True)
    born_date = models.CharField(max_length=30, null=False)
    born_location = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)    

    def __str__(self):
        return f"{self.fullname}"


class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Quote(models.Model):
    quote = models.CharField(max_length=1100, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)   
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.quote}"
