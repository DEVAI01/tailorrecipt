from django import forms 


class UserLogin(forms.Form):
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':"form-control border-0",'placeholder':'EMAIL'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':"form-control border-0",'placeholder':'PASSWORD'}))
    
    
class UserRegister(forms.Form):
    
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':"form-control border-0",'placeholder':'NAME'}))
    email=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':"form-control border-0",'placeholder':'EMAIL'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':"form-control border-0",'placeholder':'PASSWORD'}))
    mobile=forms.IntegerField(label='Mobile NO:',widget=forms.TextInput(attrs={'class':"form-control border-0",'placeholder':'MOBILE'}))
    
    


