from django.db  import models
from PIL        import Image


class CompanyContact(models.Model):
    company_manager_name = models.CharField(max_length = 50)
    company_manager_phone_number = models.CharField(max_length = 50)
    company_manager_email = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'CompanyContact'


class InvitationCodes(models.Model):
    invitation_codes = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'InvitationCodes'

class Users(models.Model):
    user_email = models.CharField(max_length = 200, unique=True)
    password = models.CharField(max_length = 200)
    company_name = models.CharField(max_length = 50)
    company_registeration_number = models.CharField(max_length = 50)
    
    ########
    # company_registeration_image = models.ImageField(default='default.jpg', upload_to='company_registeration_image')
    company_phone_number = models.CharField(max_length = 50, null=True)
    representative_name = models.CharField(max_length = 50)
    online_distributor_certification_text = models.CharField(max_length = 100)
    # online_distributor_certification_image =
    company_contact_id = models.ForeignKey(CompanyContact, on_delete=models.CASCADE, null=True)    
    banking_company = models.CharField(max_length = 50)
    banking_number = models.CharField(max_length = 50)
    banking_account_name = models.CharField(max_length = 50)
    # banking_account_image =
    invitation_codes = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    
    
    class Meta:
        db_table = 'Users'