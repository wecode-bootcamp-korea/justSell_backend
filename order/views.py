import jwt
import json
import bcrypt
import re

from .models          import OrderStatus, Orderers, Receivers, Orders
from utils            import login_decorator
from django.views     import View
from django.http      import JsonResponse
from django.shortcuts import render



class OrdersView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        Orders_list = [
            {
                'order_id' : order.id,
                'order_status' : order.order_status.order_status,
                'orderer_name' : order.orderer.orderer_name,
                'orderer_phone_number' : order.orderer.orderer_phone_number,
                'receiver_name' : order.receiver.receiver_name,
                'receiver_phone_number' : order.receiver.receiver_phone_number,
                'receiver_address' : order.receiver.receiver_address,
                'receiver_address_code' : order.receiver.receiver_address_code,
                'product_name' : order.product.product_name,
                'product_supply_price' : order.product.supply_price,
                'product_sale_price' : order.product.sale_price,
                'product_stock_amount' : order.product.stock_amount,
                'product_vendorcode' : order.product.vendorcode,
                'product_delivery_company' : order.product.delivery_company,
                'product_deliver_fee' : order.product.delivery_fee,
                'order_memo' : order.order_memo,
                'order_date' : order.created_at
            }
        for order in Orders.objects.select_related('receiver').filter(user=request.user, order_status=data['order_status'])]
        
        return JsonResponse({'USER_ORDERS': Orders_list}, status=200)