from django.db   import models
from user.models import Users


class CategoriesQuerySet(models.QuerySet):
    def keywords(self, keyword):
        return self.filter(name__icontains='f{}')

class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoriesQuerySet(self.model, using=self._db)
        
    def keywords(self, keyword):
        return self.get_queryset().keywords(keyword)

class Categories(models.Model):
    category = models.CharField(max_length = 200)
    objects = CategoryManager()
    class Meta:
        db_table = 'Categories'
    

# class DeliveryCompany(models.Model):
#     deliverycompany = models.CharField(max_length = 50)
    
#     class Meta:
#         db_table = 'DeliveryCompany'    

class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length = 200)
    brand = models.CharField(max_length = 50)
    product_tax = models.BooleanField(default=True)
    supply_price  = models.IntegerField(null = False)
    sale_price = models.IntegerField(null = False)
    stock_amount = models.IntegerField(default = 999)
    minimum_buying = models.IntegerField(default = 1)
    vendorcode = models.CharField(max_length = 50)
    delivery_company = models.CharField(max_length=50, default="선우택배")
    delivery_fee = models.IntegerField(null = False)
    return_delivery_fee = models.IntegerField(null = False)
    start_delivery_address = models.CharField(max_length = 200)
    start_delivery_address_code = models.CharField(max_length = 50, null=True)
    return_delivery_address = models.CharField(max_length = 200)
    return_delivery_address_code = models.CharField(max_length = 50, null=True)
    search_keyword = models.CharField(max_length = 200)
    adult_restricted = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=1)
    
    class Meta:
        db_table = 'Products'
        
    
# class Products_DeliveryCompany(models.Model):
#     products = models.ForeignKey("Products", on_delete=models.SET_NULL, null=True)
#     delivery_company = models.ForeignKey("DeliveryCompany", on_delete=models.SET_NULL, null=True)
    
#     class Meta:
#         db_table = "Products_DeliveryCompany"