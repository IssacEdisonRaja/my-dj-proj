#from django.forms import ModelForm
from django import forms
from .models import *

class SWMS_Form(forms.ModelForm):

    class Meta:
        model = Steel_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }
class SWMS1_Form(forms.ModelForm):

    class Meta:
        model = Steel1_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }

class SWMS2_Form(forms.ModelForm):

    class Meta:
        model = Steel2_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }
class SWMS3_Form(forms.ModelForm):

    class Meta:
        model = Steel3_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }
class SWMS4_Form(forms.ModelForm):

    class Meta:
        model = Steel4_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }
class SWMS5_Form(forms.ModelForm):

    class Meta:
        model = Steel5_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }

class SWMS6_Form(forms.ModelForm):

    class Meta:
        model = Steel6_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }

class SWMS7_Form(forms.ModelForm):

    class Meta:
        model = Steel7_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }

class SWMS8_Form(forms.ModelForm):

    class Meta:
        model = Steel8_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }
class SWMS9_Form(forms.ModelForm):

    class Meta:
        model = Steel9_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }
class SWMS10_Form(forms.ModelForm):

    class Meta:
        model = Steel10_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }
class SWMS11_Form(forms.ModelForm):

    class Meta:
        model = Steel11_records
        fields = '__all__'
        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }

class SWMS12_Form(forms.ModelForm):

    class Meta:
        model = Steel12_records
        fields = '__all__'

        widgets = {
            'Date':forms.DateInput(attrs={'class':"form-control"}),
            'Manager_name':forms.TextInput(attrs={'class':"form-control"}),
            'Task':forms.TextInput(attrs={'class':"form-control"}),
        }

class was1_Form(forms.ModelForm):
    class Meta:
        model = was_rec1
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }
class was2_Form(forms.ModelForm):
    class Meta:
        model = was_rec2
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }
class was3_Form(forms.ModelForm):
    class Meta:
        model = was_rec3
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }        
class was4_Form(forms.ModelForm):
    class Meta:
        model = was_rec4
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }
class was5_Form(forms.ModelForm):
    class Meta:
        model = was_rec5
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }        
class was6_Form(forms.ModelForm):
    class Meta:
        model = was_rec6
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }        
class was7_Form(forms.ModelForm):
    class Meta:
        model = was_rec7
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }        
class was8_Form(forms.ModelForm):
    class Meta:
        model = was_rec8
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }     
class was9_Form(forms.ModelForm):
    class Meta:
        model = was_rec9
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }   

class was10_Form(forms.ModelForm):
    class Meta:
        model = was_rec10
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }        
class was11_Form(forms.ModelForm):
    class Meta:
        model = was_rec11
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        }   

class was12_Form(forms.ModelForm):
    class Meta:
        model = was_rec12
        fields='__all__'

        widgets = {
            'W_BD':forms.DateInput(attrs={'class':"form-control"}),
            'Tot_weight':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_SD':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_ED':forms.DateInput(attrs={'class':"form-control"}),
            'Rcy_expense':forms.NumberInput(attrs={'class':"form-control"}),
            'Slud_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_EP_wei':forms.NumberInput(attrs={'class':"form-control"}),
            'Dus_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'Slud_buyer':forms.TextInput(attrs={'class':"form-control"}),
            'O_all_profit':forms.NumberInput(attrs={'class':"form-control"}),
            'Rcy_Team':forms.TextInput(attrs={'class':"form-control"}),
        } 

    