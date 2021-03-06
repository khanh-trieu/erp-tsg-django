

from django.db import models

# Create your models here.
from app_common import Timer



class employees(models.Model):
    code = models.CharField(max_length=250, blank=True,null=True)
    title = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title + ' - ' + self.code


class fields(models.Model):
    code = models.CharField(max_length=250, blank=True,null=True)
    title = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title + ' - ' + self.code


class provinces(models.Model):
    code = models.CharField(max_length=250, blank=True,null=True)
    title = models.CharField(max_length=250, blank=True)

    def create_or_no_update(self,code):
        item_type = provinces.objects.filter(title=self)
        if item_type.count() == 0:
            item_phone_type = provinces.objects.create(title=self, code=code)
            return item_phone_type
        return item_type.first()

    def __str__(self):
        return self.title + ' - ' + self.code


class districts(models.Model):
    code = models.CharField(max_length=250, blank=True,null=True)
    title = models.CharField(max_length=250, blank=True)

    def create_or_no_update(self,code):
        item_type = districts.objects.filter(title=self)
        if item_type.count() == 0:
            item_phone_type = districts.objects.create(title=self, code=code)
            return item_phone_type
        return item_type.first()

    def __str__(self):
        return self.title + ' - ' + self.code


class wards(models.Model):
    code = models.CharField(max_length=250, blank=True,null=True)
    title = models.CharField(max_length=250, blank=True)

    def create_or_no_update(self,code):
        item_type = wards.objects.filter(title=self)
        if item_type.count() == 0:
            item_phone_type = wards.objects.create(title=self, code=code)
            return item_phone_type
        return item_type.first()

    def __str__(self):
        return self.title + ' - ' + self.code


class countrys(models.Model):
    code = models.CharField(max_length=250, blank=True,null=True)
    title = models.CharField(max_length=250, blank=True)

    def create_or_no_update(self,code):
        item_type = countrys.objects.filter(title=self)
        if item_type.count() == 0:
            item_phone_type = countrys.objects.create(title=self, code=code)
            return item_phone_type
        return item_type.first()

    def __str__(self):
        return self.title + ' - ' + self.code


class phone_type(models.Model):
    code = models.CharField(max_length=250, blank=True,null=True)
    title = models.CharField(max_length=250, blank=True)

    def create_or_no_update(self):
        item_type = phone_type.objects.filter(code = self)
        if item_type.count() == 0:
            item_phone_type = phone_type.objects.create(title=self,code=self)
            return item_phone_type
        return item_type.first()

    def __str__(self):
        return self.title + ' - ' + self.code


class account_channel_phones(models.Model):
    '''Lo???i s??? ??i???n tho???i'''
    phone_type = models.ForeignKey(phone_type,on_delete=models.CASCADE,default=None,blank=True, null=True)
    phone_number = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.phone_number + '_' + str(self.phone_type)


class account_channel_emails(models.Model):
    email = models.CharField(max_length=250, blank=True)

    def create_or_no_update(self):
        item_type = account_channel_emails.objects.filter(email = self)
        if item_type.count() == 0:
            new_email= account_channel_emails.objects.create(email=self)
            return new_email
        return item_type.first()

    def __str__(self):
        return self.email

class type_company(models.Model):
    personal='personal'
    enterprise ='enterprise'
    type = (
        (personal,'C?? nh??n'),
        (enterprise,'Doanh nghi???p')
    )
    title = models.CharField(choices=type,max_length=100,null=True)

    def create_or_no_update(self):
        item_type = type_company.objects.filter(title = self)
        if item_type.count() == 0:
            type = type_company.objects.create(title=self)
            return type
        return item_type.first()

    def __str__(self):
        return self.title


class level_accounts(models.Model):
    code = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True)

    def create_or_no_update(self):
        try:
            item_type = level_accounts.objects.filter(title = self)
            if item_type.count() == 0:
                level_accounts.objects.create(title=self)
            return True
        except Exception as e:
            print(e)
            return False
    def __str__(self):
        return self.title + ' - ' + self.code


class capital_investments(models.Model):
    code = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True)

    def create_or_no_update(self):
        try:
            item_type = capital_investments.objects.filter(title = self)
            if item_type.count() == 0:
                capital_investments.objects.create(title=self)
            return True
        except Exception as e:
            print(e)
            return False
    def __str__(self):
        return self.title + ' - ' + self.code


class potentials(models.Model):
    code = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True)

    def create_or_no_update(self):
        try:
            item_type = potentials.objects.filter(title = self)
            if item_type.count() == 0:
                potentials.objects.create(title=self)
            return True
        except Exception as e:
            print(e)
            return False
    def __str__(self):
        return self.title + ' - ' + self.code


class accounts(models.Model):
    '''T??n account'''
    name = models.CharField(max_length=250, null=False)
    '''T??n ti???ng anh c???a account'''
    en_name = models.CharField(max_length=250, blank=True)
    '''M?? s??? thu???'''
    tax_code = models.CharField(max_length=100,null=False)
    '''representer: ng?????i ?????i di???n ph??p lu???t'''
    representer = models.CharField(max_length=100, blank=True, null=True)
    '''Ng??y ???????c c???p m?? s??? thu???'''
    tax_date_start = models.CharField(max_length=100, blank=True,null=True)
    '''Ng??y thu h???i m?? s??? thu???'''
    tax_date_close = models.CharField(max_length=100, blank=True,null=True)
    '''address: ?????a ch??? ti???ng vi???t'''
    address = models.CharField(max_length=250, blank=True, null=True)
    website = models.CharField(max_length=250, null=True, blank=True)
    email_provider = models.CharField(max_length=250, null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    number_of_pc = models.IntegerField(null=True, blank=True)
    number_of_server = models.IntegerField(null=True, blank=True)
    '''user id t???o account '''
    user_id = models.IntegerField(null=True)
    ''' account ???????c user ch??m s??c'''
    supporter_id = models.IntegerField(null=True)
    """contact_id"""
    contacts = models.CharField(max_length=250, null=True, blank=True)
    '''qu???c gia'''
    country = models.ForeignKey(countrys, on_delete=models.CASCADE, default=None, blank=True, null=True)
    '''m?? qu???c gia'''
    country_code = models.CharField(max_length=250, null=True, blank=True)
    '''t???nh th??nh'''
    province = models.ForeignKey(provinces, on_delete=models.CASCADE, default=None, blank=True, null=True)
    '''m?? t???nh th??nh'''
    province_code = models.CharField(max_length=250, null=True, blank=True)
    '''qu???n huy???n'''
    district = models.ForeignKey(districts, on_delete=models.CASCADE, default=None, blank=True, null=True)
    '''m?? qu???n huy???n'''
    district_code = models.CharField(max_length=250, null=True, blank=True)
    '''x?? ph?????ng'''
    ward = models.ForeignKey(wards, on_delete=models.CASCADE, default=None, blank=True, null=True)
    '''m?? x?? ph?????ng'''
    ward_code = models.CharField(max_length=250, null=True, blank=True)
    '''fields: l??nh v???c c??ng ty'''
    fields = models.CharField(max_length=250, blank=True, null=True)
    '''level c???a account'''
    level = models.ForeignKey(level_accounts, on_delete=models.CASCADE, default=None, blank=True, null=True)
    '''type: lo???i h??nh t??? ch???a'''
    type = models.ForeignKey(type_company, on_delete=models.CASCADE, null=True)
    '''Email c???a account'''
    emails = models.CharField(max_length=150, blank=True, null=True)
    '''S??? nh??n vi??n [list string]'''
    employee = models.ForeignKey(employees, on_delete=models.CASCADE, default=None, blank=True, null=True)
    '''s??? ??i???n tho???i [list string]'''
    phones = models.CharField(max_length=150, blank=True, null=True)
    '''ti???m n??ng'''
    potential = models.ForeignKey(potentials, on_delete=models.CASCADE, default=None, blank=True, null=True)
    '''V???n ?????u t???'''
    investment = models.ForeignKey(capital_investments, on_delete=models.CASCADE, default=None, blank=True, null=True)
    '''is_del: check ???? x??a hay ch??a
    # 0: ch??a
    # 1: ???? x??a'''
    is_del = models.IntegerField(default=0)
    '''Ng??y t???o'''
    created_date = models.IntegerField(default=Timer.get_timestamp_now())
    '''Ng??y update'''
    update_date = models.IntegerField(default=Timer.get_timestamp_now())

    def __str__(self):
        return 'name: ' + self.name + ' - mst: ' + self.tax_code




