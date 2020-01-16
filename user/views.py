import jwt
import json
import bcrypt
import re
import boto3

from justsell.settings  import SECRET_KEY
from .models            import Users, CompanyContact, InvitationCodes
from utils              import SmsService

from django.views           import View
from django.http            import JsonResponse
from django.db              import IntegrityError
from django.shortcuts       import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



class InvitationCodeCheck(View):
    def post(self, request):
        data = json.loads(request.body)
        invitation_codes_list = []
        for codes in InvitationCodes.objects.all():
            invitation_codes_list.append(codes.invitation_codes)
        if data['invitation_code'] in invitation_codes_list:
            return JsonResponse({'message':'SUCCESS'}, status = 200) 
        else:
            return JsonResponse({'message':'NOT_INVITED_USER'}, status = 401)


class CompanyRegisterationImageUpload(View):
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


class OnlineDistributorCertificationImageUpload(View):
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

class BankingAccountImageUpload(View):
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








class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)
        check_password = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        try:
            validate_email(data["user_email"])
            if len(data["password"]) < 8 :
                return JsonResponse({'message':'PASSWORD_SHORT'}, status = 400)
            if not check_password.match(data["password"]) :
                return JsonResponse({'message':'UNSATISFIED_PASSWORD'}, status = 400)
            # if InvitationCodes.objects.filter(invitation_codes = data["invitation_codes").Doesnotexists():
            #     return JsonResponse({'message' : 'NO_MAtCHING_IVITATION_CODES'}) 
            if CompanyContact.objects.filter(company_manager_email=data["company_manager_email"]).exists():
                return JsonResponse({'MESSAGE': 'OVERLAPED_COMPANY_MANAGER_EMAIL'}, status= 402)
                
            else :
                hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt())
                
                
                CompanyContact(
                    company_manager_name = data["company_manager_name"],
                    company_manager_phone_number = data["company_manager_phone_number"],
                    company_manager_email = data["company_manager_email"],
                    ).save()
                    
                contact_info = CompanyContact.objects.get(company_manager_email = data["company_manager_email"])
       
                
                Users(
                    user_email = data["user_email"],
                    password = hashed_password.decode('utf-8'),
                    company_name = data["company_name"],
                    company_registeration_number = data['company_registeration_number'],
                    # company_registeration_image = image파일
                    company_phone_number = data["company_phone_number"],
                    representative_name = data["representative_name"],
                    online_distributor_certification_text = data['online_distributor_certification_text'],
                    # online_distributor_certification_image = data['online_distributor_certification_image']
                    company_contact_id = contact_info,
                    banking_company = data['banking_company'],
                    banking_number = data['banking_number'],
                    banking_account_name = data['banking_account_name'],
                    invitation_codes = data['invitation_codes'],
                    ).save()
                
                phone_number = data['company_manager_phone_number']
                name = data["company_manager_name"]    
                sign_in_information = "저스트셀 회원가입을 축하합니다 :)" 
                
                SmsService(phone_number, name, sign_in_information)
                
                return JsonResponse({'message':'SUCCESS'}, status = 200)
        
        except ValidationError:
            return JsonResponse({'message':'NOT_EMAIL'}, status = 400 )
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)
        except IntegrityError:
            return JsonResponse({'message':'EXCEPTED_DATA'}, status= 401)




class SignIn(View):
    def post(self, request):
        data = json.loads(request.body)
        check_password = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
        try:
            validate_email(data["user_email"])
            user = Users.objects.get(user_email = data["user_email"])
            if not check_password.match(data["password"]) :
                return JsonResponse({'message':'UNSATISFIED_PASSWORD'}, status = 400)
            if bcrypt.checkpw(data["password"].encode('utf-8'), user.password.encode('utf-8')):
                access_token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm = 'HS256')
                return JsonResponse({'access_token':access_token.decode('utf-8')}, status = 200)
            else:
                return JsonResponse({'message':'INVALID_PASSWORD'}, status = 401)
        except Users.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status = 400)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)
        except ValidationError:
            return JsonResponse({'message': 'NOT_EMAIL'}, status = 400)
        except TypeError:
            return JsonResponse({'message': 'INVALID_VALUE'}, status = 400)