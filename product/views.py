import jwt
import json
import bcrypt
import re
import boto3
import requests

from .models          import Categories, Products

from django.views     import View
from django.http      import JsonResponse, HttpResponse
from django.shortcuts import render



class CategoryView(View):
    def post(self, request):
        data = json.loads(request.body)
        Categories_list = [
            {
                'categories' : category.category
            }
        for category in Categories.objects.filter(category__icontains=data['word'])]
           
        return JsonResponse ({"SEARCHED_CATEGORIES" : Categories_list})









class MainImageUpload(View):
    
    s3_client = boto3.client(
        's3',
        aws_access_key_id = 'AKIAUCQD4ZIUFG4IE2GX',
        aws_secret_access_key = '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'
        )
    
    def post(self, request):
        file = request.FILES['filename']
     
        self.s3_client.upload_fileobj(
            file, 
            "django-justsell-s3",
            file.name,
            ExtraArgs={
                "ContentType": file.content_type
            }
        ) 
        image_url = f"https://django-justsell-s3.s3.us-east-2.amazonaws.com/{file.name}" 
        
        
        return JsonResponse({"URL" : f"{image_url}"}, status = 200)
        


class ProductRegister(View):
    def post(self, request):
        data = json.loads(request.body)
        
        Products(
            category_id = data["category"],
            product_name = data["product_name"],
            brand = data["brand"],
            product_tax = data["product_tax"],
            supply_price = data["supply_price"],
            sale_price = data["sale_price"],
            stock_amount = data["stock_amount"],
            minimum_buying = data["minimum_buying"],
            vendorcode = data["vendorcode"],
            delivery_company = data["delivery_company"],
            delivery_fee = data["delivery_fee"],
            return_delivery_fee = data["return_delivery_fee"],
            start_delivery_address = data["start_delivery_address"],
            start_delivery_address_code = data["start_delivery_address_sigungucode"],
            return_delivery_address = data["return_delivery_address"],
            return_delivery_address_code = data["return_delivery_address_sigungucode"],
            search_keyword = data["search_keyword"],
            adult_restricted = data["adult_restricted"],
            user_id = data["user"],
            ).save()
        return JsonResponse({'message':'SUCCESS'}, status = 200)