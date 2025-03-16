from django.db import models



class FarmerQuery(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    contact = models.CharField(max_length=100, null=False, blank=False)
    query_text = models.TextField(blank=True, null=True)
    voice_message = models.FileField(upload_to="voice_messages/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.contact}"

class Blog(models.Model):
    title = models.CharField(max_length=200,null=False)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title