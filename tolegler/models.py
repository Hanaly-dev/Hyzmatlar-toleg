from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    ulanyjy = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    telefon = models.CharField(max_length=15, blank=True, null=True)
    salgy = models.TextField(blank=True, null=True)
    suraty = models.ImageField(upload_to='media/images/', blank=True, null=True)
    doglan_guni = models.DateField(blank=True, null=True) 

    def __str__(self):
        return self.ulanyjy.username
    
    class Meta:
        verbose_name_plural="Profiller"
class Hyzmat(models.Model):
    ady = models.CharField(max_length=50, unique=True)
    hyzmat_barada=models.TextField(null=True, blank=True)
    suraty=models.ImageField(upload_to='media/images/',blank=True,null=True)

    def __str__(self):
        return self.ady
    
    class Meta:
        verbose_name_plural="Hyzmatlar"

class Toleg(models.Model):
    TOLEG_USULY = [
        ('nagt', 'Nagt'),
        ('nagt dal', 'Nagt Däl'),
    ]
    ulanyjy = models.ForeignKey(User, on_delete=models.CASCADE)
    hyzmat = models.ForeignKey(Hyzmat, on_delete=models.CASCADE)
    mukdar = models.DecimalField(max_digits=10, decimal_places=2)
    senesi = models.DateField(auto_now_add=True)
    toleg_usuly = models.CharField(max_length=20, choices=TOLEG_USULY)

    def __str__(self):
        return f"{self.ulanyjy.username} - {self.hyzmat} - {self.mukdar} TMT ({self.toleg_usuly})"

    class Meta:
        verbose_name_plural="Tölegler"
        
class Habarlar(models.Model):
    goyan= models.ForeignKey(User, on_delete=models.CASCADE)
    ady=models.CharField(max_length=50,unique=True)
    goylan_senesi = models.DateTimeField(auto_now_add=True)
    beyany=models.TextField(blank=True, null=True)
    suraty=models.ImageField(upload_to='media/images/',blank=True,null=True)
    
    def __str__(self):
        return f"{self.goyan} - {self.ady}"
    class Meta:
        verbose_name_plural="Habarlar"
    
    