from django.db import models

class Author(models.Model):
    pass

class Article(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.  
          
    title = models.CharField(max_length=1000, unique=True) #Like a VARCHAR field  
    abstract = models.TextField() #Like a TEXT field  
    authors = models.ForeignKey(Author)
    published = models.DateTimeField() #Like a DATETIME field  
#    added = models.DateTimeField() # when was this added to database

    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just 
        return self.title

