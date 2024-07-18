from django import forms
import uuid


# class AddCustumer(forms.Form):
#     custumername=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':"form-control bg-transparent",'placeholder':'NAME'}))
#     custumermobile=forms.IntegerField(label='Mobile NO:',widget=forms.TextInput(attrs={'class':"form-control bg-transparent",'placeholder':'MOBILE'}))
#     deliverdate=forms.DateField(label='Delivery Date',widget=forms.DateInput(attrs={'class':"form-control bg-transparent",'type':'Date'})) 
#     Serial_no = forms.UUIDField(initial=uuid.uuid4, widget=forms.HiddenInput)
#     Emailid=forms.CharField(label='Email',widget=forms.TextInput(attrs={'class':"form-control bg-transparent",'placeholder':'EMAIL'}))
    
class AddCustumer(forms.Form):
    custumername = forms.CharField(
        label='Name',
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Enter Name'
        })
    )
    custumermobile = forms.CharField(
        label='Mobile No.',
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'placeholder': 'Enter Mobile No.'
        })
    )
    deliverdate = forms.DateField(
        label='Delivery Date',
        widget=forms.DateInput(attrs={
            'class': "form-control",
            'type': 'date'
        })
    )
    Serial_no = forms.UUIDField(initial=uuid.uuid4, widget=forms.HiddenInput)

    Emailid = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'placeholder': 'Enter Email'
        })
    )
class due(forms.Form):
    custumer_id=forms.IntegerField(label='custumer_id',widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'custumer_id'}))
    due_amount=forms.IntegerField(label='due_amount:',widget=forms.TextInput(attrs={'class':"form-control",'placeholder':'due_amount'}))
    date=forms.DateField(label='Date',widget=forms.DateInput(attrs={'class':"form-control",'type':'Date'})) 
    