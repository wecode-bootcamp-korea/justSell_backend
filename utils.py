import jwt
import json
import requests

from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from user.models                import Users
from justsell_settings          import SMS_AUTH_ID, SMS_SERVICE_SECRET, SMS_FROM_NUMBER,SMS_URL, justsell_SECRET



def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)
            print(justsell_SECRET)
            payload = jwt.decode(access_token, justsell_SECRET['secret'], algorithm='HS256')
            user = Users.objects.get(id=payload["id"])
            request.user = user
        except jwt.DecodeError:
            return  JsonResponse({'message' : 'INVALID_TOKEN'}, status=401)
        except Users.DoesNotExist:
            return JsonResponse({'de_message':'INVALID_USER'}, status = 400)
        # except TypeError:
        #     return JsonResponse({'de_message':'INVALID_VALUE'}, status = 400)
        except KeyError:
            return JsonResponse({'de_message': 'INVALID'}, status = 400)
        return func(self, request, *args, **kwargs)
    return wrapper
    
    
    
def SmsService(phone_number, name, information):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'x-ncp-auth-key': f'{SMS_AUTH_ID}',
        'x-ncp-service-secret':f'{SMS_SERVICE_SECRET}',
    }
    data = {
        'type':'SMS',
        'contentType':'COMM',
        'countryCode':'82',
        'from':f'{SMS_FROM_NUMBER}',
        'to':[
            f'{phone_number}',
            ],
        'subject':'WISO-PROJECT',
        'content':f'{name}님! {information}'
    }
    requests.post(SMS_URL, headers=headers, json=data)