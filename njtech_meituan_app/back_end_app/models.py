from django.db import models

# Create your models here.

class Book(models.Model):
    book_name = models.CharField(max_length = 64)
    add_time = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return self.book_name


class Purchase_Order(models.Model):
    food_id = models.IntegerField()
    customer_id = models.IntegerField()
    order_time = models.DateTimeField(auto_now=True)
    remarks = models.CharField(max_length = 512)    
    amount_money = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField()
    status = models.IntegerField(default = 0)

class Food(models.Model):
    category_id = models.IntegerField()
    name = models.CharField(max_length = 12,default = "NULL")
    amount_money = models.DecimalField(max_digits=20, decimal_places=2)
    introduction = models.CharField(max_length = 512)
    isexpired = models.BooleanField(default = False)
    add_time = models.DateTimeField(auto_now = True)
    stop_time = models.DateTimeField(auto_now = True)
    picUrl1 = models.CharField(max_length = 30,default = "NULL")
    picUrl2 = models.CharField(max_length = 30,default = "NULL")
    picUrl3 = models.CharField(max_length = 30,default = "NULL")
    picUrl4 = models.CharField(max_length = 30,default = "NULL")
    
class Customer(models.Model):
    mobile_phone = models.BigIntegerField(20)
    sex = models.IntegerField(1,default = 0)
    nickname = models.CharField(max_length = 12)   
    passport = models.CharField(max_length = 18)   
    create_time = models.DateTimeField(auto_now = True)
    isdeleted = models.BooleanField(default = False)
    password = models.CharField(max_length = 20,blank=False,default = "")  
    avatar = models.CharField(max_length = 30,default = "NULL")
    
class Food_Category(models.Model):
    name = models.CharField(max_length = 20)
    remarks = models.CharField(max_length = 512)
    isDelete = models.BooleanField(default = False)

class Shopping_Cart(models.Model):
    customer_id = models.IntegerField()
    food_id = models.IntegerField()
    quantity = models.IntegerField()
    amount_money = models.DecimalField(max_digits=20,decimal_places = 2)
    last_add_time = models.DateTimeField(auto_now = True)
    isselected = models.BooleanField(default = True)
    isdeleted= models.BooleanField(default = False)
    remarks = models.CharField(max_length = 512)
    
class Administrator(models.Model):
    name = models.CharField(max_length = 12)
    password = models.CharField(max_length = 20,blank=False,default = "")
    isdeleted= models.BooleanField(default = False)
    
class Complaints(models.Model):
    purchase_order_id = models.IntegerField()
    customer_id = models.IntegerField()
    content = models.CharField(max_length = 512)
    create_time = models.DateTimeField(auto_now = True)
    isdeleted = models.BooleanField(default = False)
