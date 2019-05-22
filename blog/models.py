from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_data = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        # returns only slice of 100words
        return self.body[:100]

    def pub_data_pretty(self):
        return self.pub_data.strftime('%b %e %Y')
