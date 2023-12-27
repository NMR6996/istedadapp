from django.db import models

class AdminQeydiyyatForm(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    telNo_basliq = models.CharField(null=True, max_length=50)
    telNo = models.CharField(max_length=50)
    rayon = models.CharField(max_length=50)
    mekteb = models.CharField(max_length=50)
    sinif = models.CharField(max_length=50)
    blok = models.CharField(max_length=50)
    xdil = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.fname}"
    
class AdminSinaqQeydiyyatForm(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    telNo_basliq = models.CharField(null=True, max_length=50)
    telNo = models.CharField(max_length=50)
    rayon = models.CharField(max_length=50)
    mekteb = models.CharField(max_length=50)
    sinif = models.CharField(max_length=50)
    blok = models.CharField(max_length=50)
    xdil = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.fname}"
    
class AdminElaqeForm(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    telNo = models.CharField(max_length=50)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=1500)

    def __str__(self):
        return f"{self.fname}"