from django import forms
from schools.models import School
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'school',
            'name',
            'contents',
            'excludes',
            'public'
        ]

    def __init__(self, user=None, *args,**kwargs):
        # print(kwargs.pop('user'))
        print(user)
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['school'].queryset = School.objects.filter(owner=user)#,item__isnull=True)#.exclude(item__isnull=False)
