from django.db import models

class Steel_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=200,null=True)

class Steel1_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel2_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel3_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel4_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel5_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel6_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel7_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel8_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel9_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel10_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel11_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class Steel12_records(models.Model):
   Date = models.DateField(null=True)
   Manager_name=models.CharField(max_length=200,null=True)
   Task=models.CharField(max_length=500,null=True)

class was_rec1(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)

class was_rec2(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)

class was_rec3(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)

class was_rec4(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)


class was_rec5(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)

class was_rec6(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)

class was_rec7(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)

class was_rec8(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)

class was_rec9(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)

class was_rec10(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)



class was_rec11(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)

class was_rec12(models.Model):
   W_BD = models.DateField(null=True)
   Tot_weight = models.FloatField(null=True)
   Slud_wei=models.FloatField(null=True)
   Dus_wei=models.FloatField(null=True)
   Rcy_SD=models.DateField(null=True)
   Rcy_ED=models.DateField(null=True)
   Rcy_expense=models.FloatField(null=True)
   Slud_EP_wei=models.FloatField(null=True)
   Dus_EP_wei=models.FloatField(null=True)
   Dus_buyer=models.CharField(max_length=200,null=True)
   Slud_buyer=models.CharField(max_length=200,null=True)
   O_all_profit=models.FloatField(null=True)
   Rcy_Team=models.CharField(max_length=200,null=True)      