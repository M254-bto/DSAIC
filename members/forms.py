from django import forms
from django.db.models import fields
from django import forms
from .models import MemberModel


class MemberCreateForm(forms.ModelForm):
    class Meta:
        model = MemberModel
        fields = (
            'first_name', 'last_name', 'reg', 'course', 'year'
        )
