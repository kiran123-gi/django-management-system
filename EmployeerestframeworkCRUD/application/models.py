from django.db import models

class employess(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=50)
    esal = models.FloatField()
    company = models.CharField(max_length=50)
    desi = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.ename} was working as {self.desi}"
    


