from django.db import models

# Create your models here.
#   """
#   Django model is a python class and it becomes a table in your database.
#    Evertimme you update your model , make sure you migrate the changes
#   """
 
 
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name}"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateTimeField( blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title}"