from django import forms
from myapp.models import *
from django.conf import settings
import logging
from django.forms import ModelForm, inlineformset_factory

class SysUserForm(forms.ModelForm):
    #CustomerId = forms.ModelChoiceField(queryset=Customer.objects.all())


    class Meta:
        model = SysUser
        fields = '__all__'