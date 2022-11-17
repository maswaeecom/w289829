import random
from datetime import datetime
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

def random_string():
    return str(random.randint(1000000000, 9999999999))

class newlotteries(models.Model):
    id = models.IntegerField(primary_key = True)  
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    expired_at = models.DateTimeField(default=datetime.now, blank=True)      
    created_by = models.CharField(max_length=100, default="Null")
    status = models.CharField(max_length=50, default="open")
    timing = models.IntegerField(max_length=100, null=True)
    price = models.IntegerField(max_length=100, null=True)
    
    class  Meta:  #new
        verbose_name_plural  =  "Lotteries 15 Min"

    def __int__(self) -> str:
        return self.id


class newlotteriesthreem(models.Model):
    id = models.IntegerField(primary_key = True)  
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    expired_at = models.DateTimeField(default=datetime.now, blank=True)      
    created_by = models.CharField(max_length=100, default="Null")
    status = models.CharField(max_length=50, default="open")
    timing = models.IntegerField(max_length=100, null=True)
    price = models.IntegerField(max_length=100, null=True)

    class  Meta:  #new
        verbose_name_plural  =  "Lotteries 3 Min"

    def __str__(self) -> str:
        return self.id


class newlotteriesnine(models.Model):
    id = models.IntegerField(primary_key = True)  
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    expired_at = models.DateTimeField(default=datetime.now, blank=True)      
    created_by = models.CharField(max_length=100, default="Null")
    status = models.CharField(max_length=50, default="open")
    timing = models.IntegerField(max_length=100, null=True)
    price = models.IntegerField(max_length=100, null=True)

    class  Meta:  #new
        verbose_name_plural  =  "Lotteries 10 Min"

    def __str__(self) -> str:
        return self.id

class BetSingle(models.Model):
    amount = models.IntegerField(max_length=100)
    number = models.IntegerField(max_length=100, null=True)
    evenorodd = models.CharField(max_length=100, null=True)
    period = models.IntegerField(max_length=100)
    better = models.IntegerField(max_length=100)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    timing = models.IntegerField(max_length=100, null=True)
    winnningamount= models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class  Meta:  #new
        verbose_name_plural  =  "All Bets"

    def __str__(self):
        return self.period

class Result(models.Model):
    period = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    result = models.IntegerField(null=True)
    status = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100, null=True)

class Resultthreem(models.Model):
    period = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    result = models.IntegerField(null=True)
    status = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100, null=True)

class Resultnine(models.Model):
    period = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    result = models.IntegerField(null=True)
    status = models.CharField(max_length=100)
    price = models.IntegerField(max_length=100, null=True)
    
    
class Member(models.Model):
    userid = models.CharField(unique=True,  max_length=200)   
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(null=True)
    password = models.CharField(max_length=100, null=True)
    sponsor = models.CharField(max_length=100, null=True)
    username = models.CharField(unique=True ,max_length=50,null=True)
    join_date = models.DateField(null=True)
    status = models.CharField(max_length=20, null=True)
    walletaddress = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=50, null=True)
    
    class  Meta:  #new
        verbose_name_plural  =  "All Member" 

    def __str__(self):
        return self.userid

    def add_proof_tag(self):
       if self.add_proof != '':           
           return mark_safe('<img src="%suploads/%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.add_proof))

    def photo_tag(self):
       if self.photo != '':           
           return mark_safe('<img src="%suploads/%s" width="50" height="50" />' % (f'{settings.MEDIA_URL}', self.photo)) 

    

class Kyc(models.Model):
    userid= models.IntegerField(null=True)
    id_proof = models.ImageField(upload_to="uploads", blank=True, null= True)
    address_proof = models.ImageField(upload_to="uploads", blank=True, null= True)
    photo = models.ImageField(upload_to="uploads", blank=True, null= True)

    class  Meta:  #new
        verbose_name_plural  =  "Member KYC" 

    def __str__(self):
        return self.userid



class Earning(models.Model):
    userid= models.IntegerField(null=True)
    username = models.CharField(max_length=200, null=True)
    amount= models.DecimalField(max_digits=10, decimal_places=2, null=True)
    type = models.CharField(max_length=20, null=True)
    levels = models.IntegerField(null=True)
    ref_id = models.IntegerField(null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=20, null=True)

    class  Meta:  #new
        verbose_name_plural  =  "Member Earnings" 

    


class Epin(models.Model):
    epin= models.IntegerField(unique=True)
    amount= models.IntegerField(null=True)
    issue_to = models.IntegerField(null=True)
    generate_time = models.DateField(null=True)
    generated_by = models.CharField(max_length=100, default='Admin')
    used_by = models.IntegerField(null=True)
    used_time = models.DateField(null=True)
    status = models.CharField(max_length=20, default='un used')

    def save(self, *args, **kwargs):
        self.epin = random.randint(99999999999, 999999999999)
        super(Epin, self).save(*args, **kwargs)

    class  Meta:  #new
        verbose_name_plural  =  "E-Pins" 

class Coderequest(models.Model):
    username = models.CharField(max_length=200,null=False, default="null")
    hash = models.CharField(max_length=200)
    hash_type = models.CharField(max_length=20)
    amount = models.IntegerField(null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=20)
    close_date= models.DateField(null=True)

    class  Meta:  #new
        verbose_name_plural  =  "Chips Requests" 


class Rewards(models.Model):
    userid= models.IntegerField(null=True)
    reward_name = models.CharField(max_length=100, null=True)
    date = models.DateField(null=True)
    status = models.CharField(max_length=20, null=True)
    paid_date= models.DateField(null=True)

    class  Meta:  #new
        verbose_name_plural  =  "Member Rewards" 


class Wallet(models.Model):
    username= models.CharField(max_length=100, null=True)
    balance = models.DecimalField(max_digits=19, decimal_places=2, null=True)

    class  Meta:  #new
        verbose_name_plural  =  "Member Wallet" 


class Widhdraw_requests(models.Model):
    userid= models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=10, null=True)
    tax = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateField(null=True)
    status= models.CharField(max_length=20, null=True)
    paid_date = models.DateField(null=True)
    trans_detail = models.TextField(null=True)

    class  Meta:  #new
        verbose_name_plural  =  "Make Payment"