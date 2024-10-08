from django.db import models

import uuid
from django.utils import timezone

class User(models.Model):
    userid=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=200)    
    mobile = models.CharField(max_length=10)
    date = models.DateTimeField('date published', default=timezone.localtime)
    status = models.IntegerField(default=0)
    role = models.CharField(default="custumer",max_length=10)

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}".format( self.userid,self.name, self.email, self.password, self.mobile,self.date,self.status,self.role)
    
class Addcustumer(models.Model):
    Tailorid=models.IntegerField(default=1)
    Custumerid=models.AutoField(primary_key=True)
    Custumer_name=models.CharField(max_length=100)
    Custumer_mobile=models.CharField(max_length=100)
    Delivery_date = models.DateField()
    Update=models.CharField(default="NOT UPDATED",max_length=100)
    Serial_no = models.CharField(max_length=200 ,unique=True)
    Current_date= models.DateTimeField('date published', default=timezone.now)
    Emailid=models.CharField(max_length=50)
    def save(self, *args, **kwargs):
        if not self.Serial_no: 
            # Generate a unique serial number using UUID
            self.Serial_no = str(uuid.uuid4().hex)[:12].upper()
        super().save(*args, **kwargs)
    
        
        
    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6}".format(self.Tailorid,self.Custumerid,self.Custumer_name,self.Custumer_mobile,self.Delivery_date,self.Serial_no,self.Current_date)    
    
class Upperdetsils(models.Model):
    Custumerid=models.ForeignKey(Addcustumer,on_delete=models.CASCADE)
    Catid=models.AutoField(primary_key=True)    
    Item=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Frontlength=models.CharField(max_length=100)
    Shoulder=models.CharField(max_length=100)
    Chest=models.CharField(max_length=100)
    Wrist=models.CharField(max_length=100)
    Hips=models.CharField(max_length=100)
    Sleeves=models.CharField(max_length=100)
    Biseps=models.CharField(max_length=100)
    Cuff=models.CharField(max_length=100)
    Callor=models.CharField(max_length=100)
    Message=models.CharField(max_length=100)
    Imageicon=models.CharField(max_length=200)
    
    
    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}".format(self.Custumerid,self. Catid,self.Item,self.Quantity,self.Frontlength,self.Shoulder,self.Chest,self.Wrist,self.Hips,self.Sleeves,self.Biseps,self.Cuff,self.Callor,self.Message,self.Imageicon)
    
class Lowerdetsils(models.Model):
    Custumerid=models.ForeignKey(Addcustumer,on_delete=models.CASCADE)
    Catid=models.AutoField(primary_key=True)    
    Item=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Fulllength=models.CharField(max_length=100)
    Waist=models.CharField(max_length=100)
    Hips=models.CharField(max_length=100)
    Thigh=models.CharField(max_length=100)
    Rise=models.CharField(max_length=100)
    Knee=models.CharField(max_length=100)
    Uplegoppening=models.CharField(max_length=100)
    Legoppening=models.CharField(max_length=100)
    Others=models.CharField(max_length=100)
    Message=models.CharField(max_length=100)
    Imageicon=models.CharField(max_length=200)
    
    
    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}".format(self.Custumerid,self.Catid,self.Item,self.Quantity,self.Fulllength,self.Waist,self.Hips,self.Thigh,self.Rise,self.Knee,self.Uplegoppening,self.Legoppening,self.Others,self.Message,self.Imageicon)
    
class Paymentdetails(models.Model):
    Custumerid=models.ForeignKey(Addcustumer,on_delete=models.CASCADE)
    Recipt=models.AutoField(primary_key=True)    
    Totalamount=models.IntegerField()   
    Advanceamount=models.IntegerField() 
    Dueamount=models.IntegerField()
    
    def __str__(self):
        return "{0},{1},{2},{3},{4}".format(self.Custumerid,self.Recipt,self.Totalamount,self.Advanceamount,self.Dueamount)
    
    
class Dueset(models.Model):
    Custumerid=models.IntegerField()
    Due_no=models.AutoField(primary_key=True)    
    date = models.DateTimeField('date published', default=timezone.now)
    Due_amount=models.IntegerField()   
    dob = models.DateField()
    
    def __str__(self):
        return "{0},{1},{2},{3},{4}".format(self.Custumerid,self.Due_no,self.date,self.Due_amount,self.dob)
    
    
    
from django.db import models
from django.utils import timezone

class EmailStatus(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachment_path = models.CharField(max_length=500, null=True, blank=True)
    attachment_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, default='Pending')  # Status can be 'Pending', 'Sent', 'Failed'
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Email to {self.recipient} - {self.status}"



class clothbooking(models.Model):
    Booking_Id = models.AutoField(primary_key=True)
    Mail_Id = models.CharField(max_length=100)
    Mobile_No = models.BigIntegerField()  # Updated field to BigIntegerField
    Upper_Wear = models.TextField()
    Lower_Wear = models.TextField()
    Description = models.TextField()
    quantity = models.IntegerField()
    date = models.DateTimeField('date published', default=timezone.localtime)
    Status = models.CharField(default='Pending', max_length=50)

    def __str__(self):
        return f"Email to {self.Booking_Id} - {self.Mail_Id}"
