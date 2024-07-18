from django import forms 


class UserLogin(forms.Form):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':"form-control border-0",'placeholder':'EMAIL'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':"form-control border-0",'placeholder':'PASSWORD'}))
    
    
class UserRegister(forms.Form):
    RADIO_CHOICES=[
        ('Male','Male'),('Female','Female'),('Other','Other')
    ]
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':"form-control border-0",'placeholder':'NAME'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':"form-control border-0",'placeholder':'EMAIL'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':"form-control border-0",'placeholder':'PASSWORD'}))
    mobile=forms.IntegerField(label='Mobile NO:',widget=forms.TextInput(attrs={'class':"form-control border-0",'placeholder':'MOBILE'}))
    gender=forms.ChoiceField(label='Gender', choices=RADIO_CHOICES ,widget=forms.RadioSelect)
    dob=forms.DateField(label='DOB',widget=forms.DateInput(attrs={'class':"form-control border-0",'type':'Date'})) 
    


