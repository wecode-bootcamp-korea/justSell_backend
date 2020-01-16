from django.db        import models
from django.shortcuts import render
from product.models   import Products
from user.models      import Users


class OrderStatus(models.Model):
    order_status = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "OrderStatus"
    
    
    
class Orderers(models.Model):
    orderer_name = models.CharField(max_length = 50)
    orderer_phone_number = models.CharField(max_length = 50)
    
    class Meta:
        db_table = "Orderers"


class Receivers(models.Model):
    receiver_name = models.CharField(max_length = 50)
    receiver_phone_number = models.CharField(max_length = 50)
    receiver_address = models.CharField(max_length = 200)
    receiver_address_code = models.CharField(max_length=50, null=True)
    class Meta:
        db_table = "Receivers"

class Orders(models.Model):
    order_status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    orderer = models.ForeignKey(Orderers, on_delete=models.CASCADE)
    receiver =  models.ForeignKey(Receivers, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    order_memo = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    class Meta:
        db_table = "Orders"