from django.http import HttpResponse
from django.shortcuts import render,redirect
from tailorrecipt import models
from tailorrecipt.models import User,Addcustumer,Lowerdetsils,Upperdetsils,Paymentdetails,Dueset
from tailorrecipt import settings
from .form import AddCustumer,due
from django.template.loader import render_to_string

from reportlab.lib import colors
from django.db.models.expressions import RawSQL
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import pdfkit
import http.client
import http
import json
from . import sendMail
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black, HexColor
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from io import BytesIO
from django.http import HttpResponse
from django.utils import timezone
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black, HexColor
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from io import BytesIO
from django.http import HttpResponse
from django.utils import timezone
from .import views
from datetime import datetime   
import os,requests
curl = settings.CURRENT_URL
media_url=settings.MEDIA_URL



from PIL import Image
import io
from django.core.files.storage import FileSystemStorage
import os

def resize_and_compress_image(image_file, target_size_kb=50, resize_factor=0.9, quality=75):
    """
    Resize and compress the image to ensure it is under the target size in kilobytes.
    
    :param image_file: Uploaded image file
    :param target_size_kb: Target size in kilobytes
    :param resize_factor: Factor by which to reduce the image dimensions
    :param quality: JPEG quality parameter
    :return: Path of the saved image
    """
    # Open the uploaded image
    img = Image.open(image_file)

    # Convert RGBA to RGB if necessary
    if img.mode == 'RGBA':
        # Create a new image with a white background
        img = img.convert('RGB')

    # Resize the image to reduce dimensions
    img = img.resize((800, 600), Image.LANCZOS)  # Initial resize, adjust dimensions as needed
    
    # Save to a BytesIO object with JPEG compression
    image_io = io.BytesIO()
    img.save(image_io, format='JPEG', quality=quality)
    
    # Ensure the image is compressed enough
    while len(image_io.getvalue()) / 1024 > target_size_kb:  # Target size in KB
        img = img.resize((int(img.width * resize_factor), int(img.height * resize_factor)), Image.LANCZOS)
        image_io = io.BytesIO()
        img.save(image_io, format='JPEG', quality=quality)
    
    image_io.seek(0)
    
    # Save the image to the filesystem
    fs = FileSystemStorage()
    filename = fs.save(image_file.name, image_io)
    image_path = fs.url(filename)
    relative_image_path = os.path.basename(image_path)
    return relative_image_path


from django.urls import reverse

def tailorhome(request):
    msg=""
    fm = AddCustumer()
    if request.method=="POST":
        fm=AddCustumer(request.POST)
        if fm.is_valid():
            print("Form validated")
            print("Custumer Name:",fm.cleaned_data['custumername'])
            print("custumer Mobile :",fm.cleaned_data['custumermobile'])
            print("deliverdate:",fm.cleaned_data['deliverdate'])
            print("Serial_no:",fm.cleaned_data['Serial_no'])
            print("emailid",fm.cleaned_data['Emailid'])
            Custumername=fm.cleaned_data['custumername']
            Custumermobile=fm.cleaned_data['custumermobile']
            Deliverydate=fm.cleaned_data['deliverdate']
            Serial_no=fm.cleaned_data['Serial_no']
            Emailid=fm.cleaned_data['Emailid']
            
            
            print(Custumername,Deliverydate,Custumermobile,Serial_no,Emailid)
            data=Addcustumer(Custumer_name=Custumername,Emailid=Emailid,Custumer_mobile=Custumermobile,Delivery_date=Deliverydate,Serial_no=Serial_no)
            try:
                data.save()
                msg="custumer register succesfully"
            except Exception as e:
                msg = f"Customer not registered. Error: {str(e)}"
            print(msg)
            return redirect(curl+'TailorApp/tailorhome',{"form":fm,'msg':msg})
    return render(request,'Tailorhome.html',{'curl':curl ,'form':fm,'msg':msg,'logout_url': reverse('logout')})
    # elif request.method == "GET":
    #     return render(request,'Tailorhome.html',{'curl':curl ,'msg':msg,'form':fm})
    
    
def addclothes(request):
    
    obj=Addcustumer.objects.raw('SELECT * FROM tailorrecipt_addcustumer ORDER BY Custumerid DESC LIMIT 1')
        
    
    return render(request,'AddClothes.html',{'curl':curl,'context':obj})
     

def coupleclothes(request):
    obj=Addcustumer.objects.raw('SELECT * FROM tailorrecipt_addcustumer ORDER BY Custumerid DESC LIMIT 1')
    msg=""
    msg1=""
    msg2=""
    if request.method=="POST":
        custumerid=request.POST.get('custumerid')
        firstitem=request.POST.get('firstitem') 
        firstquantity=request.POST.get('firstquantity')
        frontlength=request.POST.get('frontlength')
        shoulder=request.POST.get('shoulder')
        chest=request.POST.get('chest')
        wrist=request.POST.get('wrist')
        hips=request.POST.get('hips')
        sleeves=request.POST.get('sleeves')
        biseps=request.POST.get('biseps')
        cuff=request.POST.get('cuff')
        callor=request.POST.get('callor')
        firstmessage=request.POST.get('firstmessage')

        firstimageicon=request.FILES['firstimageicon']
        
        if firstimageicon:
            # Resize and compress the image
            firstimageicon = resize_and_compress_image(firstimageicon)
        
    
        seconditem=request.POST.get('seconditem') 
        secondquantity=request.POST.get('secondquantity')
        fulllength=request.POST.get('fulllength')
        waist=request.POST.get('waist')
        hipss=request.POST.get('hipss')
        thigh=request.POST.get('thigh')
        rise=request.POST.get('rise')
        knee=request.POST.get('knee')
        uplegoppening=request.POST.get('uplegoppening')
        legoppening=request.POST.get('legoppening')
        other=request.POST.get('other')
        secondmessage=request.POST.get('secondmessage')
        secondimageicon=request.FILES['secondimageicon']
        
       
        if secondimageicon:
            # Resize and compress the image
            secondimageicon = resize_and_compress_image(secondimageicon)
            
        totalamount=request.POST.get('totalAmount')
        advanceamount=request.POST.get('advancedAmount')
        dueamount=request.POST.get('dueAmount')
            
        print("uppercloth",firstitem,firstquantity,frontlength,shoulder,chest,wrist,hips,sleeves,biseps,cuff,callor,firstmessage,firstimageicon,custumerid)
            
        data=Upperdetsils(Item=firstitem,Quantity=firstquantity,Frontlength=frontlength,Shoulder=shoulder,Chest=chest,Wrist=wrist,Hips=hips,Sleeves=sleeves,Biseps=biseps,Cuff=cuff,Callor=callor,Message=firstmessage,Imageicon=firstimageicon,Custumerid_id=custumerid)
        try:   
            data.save()
            msg=" Uper cloth details register succesfully"
        except:
            msg=" Uper cloth details not register"        
        
       
        print(custumerid,seconditem,secondquantity,fulllength,waist,hipss,thigh,rise,knee,uplegoppening,legoppening,other,secondmessage,secondimageicon)
        data=Lowerdetsils(Custumerid_id=custumerid,Item=seconditem,Quantity=secondquantity,Fulllength=fulllength,Waist=waist,Hips=hipss,Thigh=thigh,Rise=rise,Knee=knee,Uplegoppening=uplegoppening,Legoppening=legoppening,Others=other,Message=secondmessage,Imageicon=secondimageicon)
        try:   
            data.save()
            msg1=" Lower cloth details register succesfully"
        except:
            msg1=" Lower cloth details not register"
            
        
        payment=Paymentdetails(Totalamount=totalamount,Advanceamount=advanceamount,Dueamount=dueamount,Custumerid_id=custumerid)
        print("paymentdetails",totalamount,advanceamount,dueamount,custumerid)
        try:
            payment.save()
            msg2="payementdetails register successfully"
        except:
            msg2="payment details not register "
            
        return redirect(curl+'TailorApp/coupleclothes/'+ f'?msg={msg}&msg1={msg1}&msg2={msg2}')

    return render(request,'Coupleclothes.html',{'curl':curl,'context':obj})    


import qrcode
from django.http import HttpResponse
from django.shortcuts import render
from io import BytesIO
import qrcode
from django.http import HttpResponse

from io import BytesIO



def QRCODE(request):
    if request.method == "GET":
        # Fetch the latest customer
        latest_customer = Addcustumer.objects.latest('Custumerid')
        # Customer data to include in the QR code
        data = {
            "Customer Name": latest_customer.Custumer_name,
            "Mobile": latest_customer.Custumer_mobile,
            "Delivery Date": latest_customer.Delivery_date.strftime('%Y-%m-%d'),
            "Customer ID": latest_customer.Custumerid,
            "Last Updated":latest_customer.Update
        }

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")

        # Save QR code to a BytesIO object for response
        buffer = BytesIO()
        qr_image.save(buffer, format="PNG")
        buffer.seek(0)
        
        # Return the QR code as a downloadable file
        response = HttpResponse(buffer, content_type="image/png")
        response['Content-Disposition'] = 'attachment; filename="customer_qr_code.png"'
        return response


def invoice(request):
    if request.method == "GET":
        # Fetch the latest customer
        
        latest_customer =Addcustumer.objects.latest('Custumerid')
        
        # Get related data
        upper_details = Upperdetsils.objects.filter(Custumerid=latest_customer)
        lower_details = Lowerdetsils.objects.filter(Custumerid=latest_customer)
        
        # Get the first payment detail
        payment_details = Paymentdetails.objects.filter(Custumerid=latest_customer)
        
        # Create a byte buffer for the PDF
        buffer = BytesIO()

        # Create a document template
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=inch, leftMargin=inch, topMargin=inch, bottomMargin=inch)
        elements = []

        # Define styles
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Company', fontSize=16, leading=20, alignment=1, textColor=colors.darkblue))
        styles.add(ParagraphStyle(name='CustomTitle', fontSize=14, leading=18, textColor=colors.black))
        styles.add(ParagraphStyle(name='CustomNormal', fontSize=12, leading=14, textColor=colors.black))
        styles.add(ParagraphStyle(name='Terms', fontSize=10, leading=12, textColor=colors.grey))

        # Add company details
        elements.append(Paragraph("Murlitailor", styles['Company']))
        elements.append(Paragraph("Email: Artfullstiches@gmail.com", styles['CustomNormal']))
        elements.append(Paragraph("Mobile Number: 9171809182", styles['CustomNormal']))
        elements.append(Paragraph("Address: Vijay Nagar, Indore", styles['CustomNormal']))
        elements.append(Spacer(1, 12))

        # Add invoice title and customer details
        elements.append(Paragraph(f"Invoice for: {latest_customer.Custumer_name} (Serial Number: {latest_customer.Custumerid})", styles['Company']))
        elements.append(Spacer(1, 8))
        current_date_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        elements.append(Paragraph(f"Mobile Number: {latest_customer.Custumer_mobile}", styles['CustomNormal']))
        elements.append(Paragraph(f"Current Date: {current_date_time}", styles['CustomNormal']))
        elements.append(Paragraph(f"Delivery Date: {latest_customer.Delivery_date}", styles['CustomNormal']))
        elements.append(Spacer(1, 12))

        # Add upper clothes information
        elements.append(Paragraph("Upper Clothes Information", styles['CustomTitle']))
        upper_data = [["#", "DESCRIPTION", "QUANTITY"]]
        for i, item in enumerate(upper_details, start=1):
            upper_data.append([str(i), f"{item.Item} (Category ID: {item.Catid})", str(item.Quantity)])
        upper_table = Table(upper_data, colWidths=[30, 400, 70])
        upper_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(upper_table)
        elements.append(Spacer(1, 12))

        # Add lower clothes information
        elements.append(Paragraph("Lower Clothes Information", styles['CustomTitle']))
        lower_data = [["#", "DESCRIPTION", "QUANTITY"]]
        for i, item in enumerate(lower_details, start=1):
            lower_data.append([str(i), f"{item.Item} (Category ID: {item.Catid})", str(item.Quantity)])
        lower_table = Table(lower_data, colWidths=[30, 400, 70])
        lower_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        elements.append(lower_table)
        elements.append(Spacer(1, 12))

        # Add payment details
        # Add payment details
        if payment_details.exists():
            total_amount = payment_details.aggregate(Sum('Totalamount'))['Totalamount__sum'] or 0
            advance_amount = payment_details.aggregate(Sum('Advanceamount'))['Advanceamount__sum'] or 0
            due_amount = payment_details.aggregate(Sum('Dueamount'))['Dueamount__sum'] or 0
            elements.append(Paragraph("Payment Details", styles['CustomTitle']))
            payment_data = [
                ["Total Amount", f"${total_amount}"],
                ["Advance Amount", f"${advance_amount}"],
                ["Due Amount", f"${due_amount}"]
            ]
            payment_table = Table(payment_data, colWidths=[150, 150])
            payment_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(payment_table)
            elements.append(Spacer(1, 12))

        # Add terms and conditions
        elements.append(Paragraph("Terms & Conditions", styles['CustomTitle']))
        terms = ("Customers must pick up their clothes within one month. We are not responsible for clothes left beyond this period. "
                 "Please present this receipt when collecting your clothes. Please deposit full payment when taking your clothes, as we do not accept due amounts.")
        elements.append(Paragraph(terms, styles['Terms']))
        elements.append(Spacer(1, 48))

        # Add signature
        elements.append(Paragraph("Murli Tailor", ParagraphStyle(name='Signature', fontSize=14, fontName='Helvetica-Oblique', textColor=colors.black)))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph("Owner of Murli Tailor", styles['Normal']))

        # Build the PDF
        doc.build(elements)

        # Get the PDF value
        buffer.seek(0)
        pdf = buffer.getvalue()
        buffer.close()

        pdf_path = f"media/invoice_{latest_customer.Custumerid}.pdf"
        with open(pdf_path, 'wb') as f:
            f.write(pdf)

        # Send the PDF via email
        email_subject = "Your Invoice from Murliailor"
        email_body = f"Dear {latest_customer.Custumer_name},\n\nThis is invoice of your clothes from murlitalor.shop.\n\n You can track you cloth updated in murli tailor  website\n\nBest regards,\nArtfullstiches"
        sendMail.sendMail(latest_customer.Emailid, subject=email_subject, html=email_body, attachment_path=pdf_path, attachment_name=f"invoice_{latest_customer.Custumerid}.pdf")

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{latest_customer.Custumerid}.pdf"'
        
        return response
        
    return render(request, 'invoice.html')

# def send_text_via_whatsapp(whatsapp_number, message):



def doublecoupleclothes(request):
    obj=Addcustumer.objects.raw('SELECT * FROM tailorrecipt_addcustumer ORDER BY Custumerid DESC LIMIT 1')
    msg=""
    msg1=""
    msg2=""
    msg3=""
    msg4=""
    if request.method=="POST":
        custumerid=request.POST.get('custumerid')
        firstitem=request.POST.get('firstitem') 
        firstquantity=request.POST.get('firstquantity')
        frontlength=request.POST.get('frontlength')
        shoulder=request.POST.get('shoulder')
        chest=request.POST.get('chest')
        wrist=request.POST.get('wrist')
        hips=request.POST.get('hips')
        sleeves=request.POST.get('sleeves')
        biseps=request.POST.get('biseps')
        cuff=request.POST.get('cuff')
        callor=request.POST.get('callor')
        firstmessage=request.POST.get('firstmessage')

        firstimageicon=request.FILES['firstimageicon']
        if firstimageicon:
            # Resize and compress the image
            firstimageicon = resize_and_compress_image(firstimageicon)
        
        
        
    
        seconditem=request.POST.get('seconditem') 
        secondquantity=request.POST.get('secondquantity')
        fulllength=request.POST.get('fulllength')
        waist=request.POST.get('waist')
        hipss=request.POST.get('hipss')
        thigh=request.POST.get('thigh')
        rise=request.POST.get('rise')
        knee=request.POST.get('knee')
        uplegoppening=request.POST.get('uplegoppening')
        legoppening=request.POST.get('legoppening')
        other=request.POST.get('other')
        secondmessage=request.POST.get('secondmessage')
        secondimageicon=request.FILES['secondimageicon']
        if secondimageicon:
            # Resize and compress the image
            secondimageicon = resize_and_compress_image(secondimageicon)
    
        totalamount=request.POST.get('totalAmount')
        advanceamount=request.POST.get('advancedAmount')
        dueamount=request.POST.get('dueAmount')
            
        print("uppercloth",firstitem,firstquantity,frontlength,shoulder,chest,wrist,hips,sleeves,biseps,cuff,callor,firstmessage,firstimageicon,custumerid)
            
        data=Upperdetsils(Item=firstitem,Quantity=firstquantity,Frontlength=frontlength,Shoulder=shoulder,Chest=chest,Wrist=wrist,Hips=hips,Sleeves=sleeves,Biseps=biseps,Cuff=cuff,Callor=callor,Message=firstmessage,Imageicon=firstimageicon,Custumerid_id=custumerid)
        try:   
            data.save()
            msg=" Uper cloth details register succesfully"
        except:
            msg=" Uper cloth details not register"        
        
       
        print(custumerid,seconditem,secondquantity,fulllength,waist,hipss,thigh,rise,knee,uplegoppening,legoppening,other,secondmessage,secondimageicon)
        data=Lowerdetsils(Custumerid_id=custumerid,Item=seconditem,Quantity=secondquantity,Fulllength=fulllength,Waist=waist,Hips=hipss,Thigh=thigh,Rise=rise,Knee=knee,Uplegoppening=uplegoppening,Legoppening=legoppening,Others=other,Message=secondmessage,Imageicon=secondimageicon)
        try:   
            data.save()
            msg1=" Lower cloth details register succesfully"
        except:
            msg1=" Lower cloth details not register"
            
        
    
        firstitemtwo=request.POST.get('firstitemtwo') 
        firstquantitytwo=request.POST.get('firstquantitytwo')
        frontlengthtwo=request.POST.get('frontlengthtwo')
        shouldertwo=request.POST.get('shouldertwo')
        chesttwo=request.POST.get('chesttwo')
        wristtwo=request.POST.get('wristtwo')
        hipstwo=request.POST.get('hipstwo')
        sleevestwo=request.POST.get('sleevestwo')
        bisepstwo=request.POST.get('bisepstwo')
        cufftwo=request.POST.get('cufftwo')
        callortwo=request.POST.get('callortwo')
        firstmessagetwo=request.POST.get('firstmessagetwo')

        firstimageicontwo=request.FILES['firstimageicontwo']
        if firstimageicontwo:
            # Resize and compress the image
            firstimageicontwo = resize_and_compress_image(firstimageicontwo)
        
        
        
    
        seconditemthree=request.POST.get('seconditemthree') 
        secondquantitythree=request.POST.get('secondquantitythree')
        fulllengththree=request.POST.get('fulllengththree')
        waistthree=request.POST.get('waistthree')
        hipsthree=request.POST.get('hipsthree')
        thighthree=request.POST.get('thighthree')
        risethree=request.POST.get('risethree')
        kneethree=request.POST.get('kneethree')
        uplegoppeningthree=request.POST.get('uplegoppeningthree')
        legoppeningthree=request.POST.get('legoppeningthree')
        otherthree=request.POST.get('otherthree')
        secondmessagethree=request.POST.get('secondmessagethree')
        secondimageiconthree=request.FILES['secondimageiconthree']
        if secondimageiconthree:
            # Resize and compress the image
            secondimageiconthree = resize_and_compress_image(secondimageiconthree)
    
        totalamount=request.POST.get('totalAmount')
        advanceamount=request.POST.get('advancedAmount')
        dueamount=request.POST.get('dueAmount')
            
        print("uppercloth",firstitemtwo,firstquantitytwo,frontlengthtwo,shouldertwo,chesttwo,wristtwo,hipstwo,sleevestwo,bisepstwo,cufftwo,callortwo,firstmessagetwo,firstimageicontwo,custumerid)
            
        datatwo=Upperdetsils(Item=firstitemtwo,Quantity=firstquantitytwo,Frontlength=frontlengthtwo,Shoulder=shouldertwo,Chest=chesttwo,Wrist=wristtwo,Hips=hipstwo,Sleeves=sleevestwo,Biseps=bisepstwo,Cuff=cufftwo,Callor=callortwo,Message=firstmessagetwo,Imageicon=firstimageicontwo,Custumerid_id=custumerid)
        try:   
            datatwo.save()
            msg3=" Uper cloth 2nd details register succesfully"
        except:
            msg3=" Uper cloth 2nd details not register"        
        
       
        print(custumerid,seconditemthree,secondquantitythree,fulllengththree,waistthree,hipsthree,thighthree,risethree,kneethree,uplegoppeningthree,legoppeningthree,otherthree,secondmessagethree,secondimageiconthree)
        datathree=Lowerdetsils(Custumerid_id=custumerid,Item=seconditemthree,Quantity=secondquantitythree,Fulllength=fulllengththree,Waist=waistthree,Hips=hipsthree,Thigh=thighthree,Rise=risethree,Knee=kneethree,Uplegoppening=uplegoppeningthree,Legoppening=legoppeningthree,Others=otherthree,Message=secondmessagethree,Imageicon=secondimageiconthree)
        try:   
            datathree.save()
            msg4=" Lower cloth 2nd details register succesfully"
        except:
            msg4=" Lower cloth 2nd details not register"
            
            
        payment=Paymentdetails(Totalamount=totalamount,Advanceamount=advanceamount,Dueamount=dueamount,Custumerid_id=custumerid)
        print("paymentdetails",totalamount,advanceamount,dueamount,custumerid)
        try:
            payment.save()
            msg2="payementdetails register successfully"
        except:
            msg2="payment details not register "
            
        return redirect(curl+'TailorApp/doublecoupleclothes/'+ f'?msg={msg}&msg1={msg1}&msg2={msg2}&msg3={msg3}&msg4={msg4}')

    return render(request,'Doublecoupleclothes.html',{'curl':curl,'context':obj})    
        






def uppersinglecloth(request):
    obj = Addcustumer.objects.raw('SELECT * FROM tailorrecipt_addcustumer ORDER BY Custumerid DESC LIMIT 1')
    msg = ""
    
    if request.method == "POST":
        custumerid = request.POST.get('custumerid')
        custumer_mobile = request.POST.get('custumermobile')
        item = request.POST.get('item')
        quantity = request.POST.get('quantity')
        frontlength = request.POST.get('frontlength')
        shoulder = request.POST.get('shoulder')
        chest = request.POST.get('chest')
        wrist = request.POST.get('wrist')
        hips = request.POST.get('hips')
        sleeves = request.POST.get('sleeves')
        biseps = request.POST.get('biseps')
        cuff = request.POST.get('cuff')
        callor = request.POST.get('callor')
        message = request.POST.get('message')
        totalamount = request.POST.get('totalAmount')
        advanceamount = request.POST.get('advancedAmount')
        dueamount = request.POST.get('dueAmount')
        imageicon = request.FILES.get('imageicon')
        
        if imageicon:
            # Resize and compress the image
            relative_image_path = resize_and_compress_image(imageicon)
            
            print("uppercloth", custumer_mobile, item, quantity, frontlength, shoulder, chest, wrist, hips, sleeves, biseps, cuff, callor, message, relative_image_path, custumerid)
           
            data = Upperdetsils(Item=item, Quantity=quantity, Frontlength=frontlength, Shoulder=shoulder, Chest=chest, Wrist=wrist, Hips=hips, Sleeves=sleeves, Biseps=biseps, Cuff=cuff, Callor=callor, Message=message, Imageicon=relative_image_path, Custumerid_id=custumerid)
            payment = Paymentdetails(Totalamount=totalamount, Advanceamount=advanceamount, Dueamount=dueamount, Custumerid_id=custumerid)
            print("paymentdetails", totalamount, advanceamount, dueamount, custumerid)
            
            try:
                data.save()
                payment.save()
                msg = "cloth details registered successfully"
            except Exception as e:
                print("Error saving details:", e)
                msg = "cloth details not registered"
            
            return redirect(curl + 'TailorApp/uppersinglecloth/' + f'?msg={msg}')
    return render(request, 'Uppersinglecloth.html', {'curl': curl, 'context': obj})



# def uppersinglecloth(request):
#     obj=Addcustumer.objects.raw('SELECT * FROM tailorrecipt_addcustumer ORDER BY Custumerid DESC LIMIT 1')
        
#     msg=""
    
#     if request.method=="POST":  
#         custumerid=request.POST.get('custumerid')
#         custumer_mobile=request.POST.get('custumermobile')
#         item=request.POST.get('item') 
#         quantity=request.POST.get('quantity')
#         frontlength=request.POST.get('frontlength')
#         shoulder=request.POST.get('shoulder')
#         chest=request.POST.get('chest')
#         wrist=request.POST.get('wrist')
#         hips=request.POST.get('hips')
#         sleeves=request.POST.get('sleeves')
#         biseps=request.POST.get('biseps')
#         cuff=request.POST.get('cuff')
#         callor=request.POST.get('callor')
#         message=request.POST.get('message')
#         totalamount=request.POST.get('totalAmount')
#         advanceamount=request.POST.get('advancedAmount')
#         dueamount=request.POST.get('dueAmount')
#         imageicon=request.FILES['imageicon']
#         fs=FileSystemStorage()
#         fs.save(imageicon.name,imageicon)  
        
#         print("uppercloth",custumer_mobile,item,quantity,frontlength,shoulder,chest,wrist,hips,sleeves,biseps,cuff,callor,message,imageicon,custumerid)
#         data=Upperdetsils(Item=item,Quantity=quantity,Frontlength=frontlength,Shoulder=shoulder,Chest=chest,Wrist=wrist,Hips=hips,Sleeves=sleeves,Biseps=biseps,Cuff=cuff,Callor=callor,Message=message,Imageicon=imageicon,Custumerid_id=custumerid)
#         payment=Paymentdetails(Totalamount=totalamount,Advanceamount=advanceamount,Dueamount=dueamount,Custumerid_id=custumerid)
#         print("paymentdetails",totalamount,advanceamount,dueamount,custumerid)
#         try:   
#             data.save()
#             payment.save()
#             msg="cloth details register succesfully"
#         except:
#             msg="cloth details not register"
                
#         # custumermobile= "+91" + custumer_mobile
#         # print(custumermobile) 
         
        
#         return redirect(curl+'TailorApp/uppersinglecloth/'+ f'?msg={msg}')
#     return render(request,'Uppersinglecloth.html',{'curl':curl,'context':obj}) 

# send_whatsapp_message(custumerid,custumermobile,item,totalamount,advanceamount,dueamount)  

def lowersinglecloth(request):
    
        obj=Addcustumer.objects.raw('SELECT * FROM tailorrecipt_addcustumer ORDER BY Custumerid DESC LIMIT 1')
        msg=""
        msg1=""
        if request.method=="POST":  
            custumerid=request.POST.get('custumerid')
            item=request.POST.get('item') 
            quantity=request.POST.get('quantity')
            fulllength=request.POST.get('fulllength')
            waist=request.POST.get('waist')
            hips=request.POST.get('hips')
            thigh=request.POST.get('thigh')
            rise=request.POST.get('rise')
            knee=request.POST.get('knee')
            uplegoppening=request.POST.get('uplegoppening')
            legoppening=request.POST.get('legoppening')
            other=request.POST.get('other')
            message=request.POST.get('message')
            totalamount=request.POST.get('totalAmount')
            advanceamount=request.POST.get('advancedAmount')
            dueamount=request.POST.get('dueAmount')
            
            imageicon=request.FILES['imageicon']
            if imageicon:
            
                imageicon= resize_and_compress_image(imageicon)
            
            
            print(custumerid,item,quantity,fulllength,waist,hips,thigh,rise,knee,uplegoppening,legoppening,other,message,imageicon)
            data=Lowerdetsils(Custumerid_id=custumerid,Item=item,Quantity=quantity,Fulllength=fulllength,Waist=waist,Hips=hips,Thigh=thigh,Rise=rise,Knee=knee,Uplegoppening=uplegoppening,Legoppening=legoppening,Others=other,Message=message,Imageicon=imageicon)
            try:   
                data.save()
                msg="cloth details register succesfully"
            except:
                msg="cloth details not register"
                
                
            payment=Paymentdetails(Totalamount=totalamount,Advanceamount=advanceamount,Dueamount=dueamount,Custumerid_id=custumerid)
            print("paymentdetails",totalamount,advanceamount,dueamount,custumerid)
            try:
                payment.save()
                msg1="payementdetails register successfully"
            except:
                msg1="payment details not register "
            
    
            return redirect(curl+'TailorApp/lowersinglecloth/'+ f'?msg={msg}&msg1={msg1}')
        return render(request,'Lowersinglecloth.html',{'curl':curl,'context':obj}) 
        
    
    
def tripleclothes(request):
    obj=Addcustumer.objects.raw('SELECT * FROM tailorrecipt_addcustumer ORDER BY Custumerid DESC LIMIT 1')
    msg=""
    msg1=""
    msg2=""
    msg3=""
    msg4=""
    msg5=""
    msg6=""
    if request.method=="POST":
        custumerid=request.POST.get('custumerid')
        firstitem=request.POST.get('firstitem') 
        firstquantity=request.POST.get('firstquantity')
        frontlength=request.POST.get('frontlength')
        shoulder=request.POST.get('shoulder')
        chest=request.POST.get('chest')
        wrist=request.POST.get('wrist')
        hips=request.POST.get('hips')
        sleeves=request.POST.get('sleeves')
        biseps=request.POST.get('biseps')
        cuff=request.POST.get('cuff')
        callor=request.POST.get('callor')
        firstmessage=request.POST.get('firstmessage')

        firstimageicon=request.FILES['firstimageicon']
        if firstimageicon:
            firstimageicon= resize_and_compress_image(firstimageicon)
        
        
    
        seconditem=request.POST.get('seconditem') 
        secondquantity=request.POST.get('secondquantity')
        fulllength=request.POST.get('fulllength')
        waist=request.POST.get('waist')
        hipss=request.POST.get('hipss')
        thigh=request.POST.get('thigh')
        rise=request.POST.get('rise')
        knee=request.POST.get('knee')
        uplegoppening=request.POST.get('uplegoppening')
        legoppening=request.POST.get('legoppening')
        other=request.POST.get('other')
        secondmessage=request.POST.get('secondmessage')
        secondimageicon=request.FILES['secondimageicon']
        if secondimageicon:
            secondimageicon= resize_and_compress_image(secondimageicon)
    
        
            
        print("uppercloth",firstitem,firstquantity,frontlength,shoulder,chest,wrist,hips,sleeves,biseps,cuff,callor,firstmessage,firstimageicon,custumerid)
            
        data=Upperdetsils(Item=firstitem,Quantity=firstquantity,Frontlength=frontlength,Shoulder=shoulder,Chest=chest,Wrist=wrist,Hips=hips,Sleeves=sleeves,Biseps=biseps,Cuff=cuff,Callor=callor,Message=firstmessage,Imageicon=firstimageicon,Custumerid_id=custumerid)
        try:   
            data.save()
            msg=" Uper cloth details register succesfully"
        except:
            msg=" Uper cloth details not register"        
        
       
        print(custumerid,seconditem,secondquantity,fulllength,waist,hipss,thigh,rise,knee,uplegoppening,legoppening,other,secondmessage,secondimageicon)
        data=Lowerdetsils(Custumerid_id=custumerid,Item=seconditem,Quantity=secondquantity,Fulllength=fulllength,Waist=waist,Hips=hipss,Thigh=thigh,Rise=rise,Knee=knee,Uplegoppening=uplegoppening,Legoppening=legoppening,Others=other,Message=secondmessage,Imageicon=secondimageicon)
        try:   
            data.save()
            msg1=" Lower cloth details register succesfully"
        except:
            msg1=" Lower cloth details not register"
            
        
    
        firstitemtwo=request.POST.get('firstitemtwo') 
        firstquantitytwo=request.POST.get('firstquantitytwo')
        frontlengthtwo=request.POST.get('frontlengthtwo')
        shouldertwo=request.POST.get('shouldertwo')
        chesttwo=request.POST.get('chesttwo')
        wristtwo=request.POST.get('wristtwo')
        hipstwo=request.POST.get('hipstwo')
        sleevestwo=request.POST.get('sleevestwo')
        bisepstwo=request.POST.get('bisepstwo')
        cufftwo=request.POST.get('cufftwo')
        callortwo=request.POST.get('callortwo')
        firstmessagetwo=request.POST.get('firstmessagetwo')

        firstimageicontwo=request.FILES['firstimageicontwo']
        if firstimageicontwo:
            firstimageicontwo= resize_and_compress_image(firstimageicontwo)
        
        
        
    
        seconditemthree=request.POST.get('seconditemthree') 
        secondquantitythree=request.POST.get('secondquantitythree')
        fulllengththree=request.POST.get('fulllengththree')
        waistthree=request.POST.get('waistthree')
        hipsthree=request.POST.get('hipsthree')
        thighthree=request.POST.get('thighthree')
        risethree=request.POST.get('risethree')
        kneethree=request.POST.get('kneethree')
        uplegoppeningthree=request.POST.get('uplegoppeningthree')
        legoppeningthree=request.POST.get('legoppeningthree')
        otherthree=request.POST.get('otherthree')
        secondmessagethree=request.POST.get('secondmessagethree')
        secondimageiconthree=request.FILES['secondimageiconthree']
        if secondimageiconthree:
            secondimageiconthree= resize_and_compress_image(secondimageiconthree)
        
    
            
        print("uppercloth",firstitemtwo,firstquantitytwo,frontlengthtwo,shouldertwo,chesttwo,wristtwo,hipstwo,sleevestwo,bisepstwo,cufftwo,callortwo,firstmessagetwo,firstimageicontwo,custumerid)
            
        datatwo=Upperdetsils(Item=firstitemtwo,Quantity=firstquantitytwo,Frontlength=frontlengthtwo,Shoulder=shouldertwo,Chest=chesttwo,Wrist=wristtwo,Hips=hipstwo,Sleeves=sleevestwo,Biseps=bisepstwo,Cuff=cufftwo,Callor=callortwo,Message=firstmessagetwo,Imageicon=firstimageicontwo,Custumerid_id=custumerid)
        try:   
            datatwo.save()
            msg3=" Uper cloth 2nd details register succesfully"
        except:
            msg3=" Uper cloth 2nd details not register"        
        
       
        print(custumerid,seconditemthree,secondquantitythree,fulllengththree,waistthree,hipsthree,thighthree,risethree,kneethree,uplegoppeningthree,legoppeningthree,otherthree,secondmessagethree,secondimageiconthree)
        datathree=Lowerdetsils(Custumerid_id=custumerid,Item=seconditemthree,Quantity=secondquantitythree,Fulllength=fulllengththree,Waist=waistthree,Hips=hipsthree,Thigh=thighthree,Rise=risethree,Knee=kneethree,Uplegoppening=uplegoppeningthree,Legoppening=legoppeningthree,Others=otherthree,Message=secondmessagethree,Imageicon=secondimageiconthree)
        try:   
            datathree.save()
            msg4=" Lower cloth 2nd details register succesfully"
        except:
            msg4=" Lower cloth 2nd details not register"
        
        custumeridfour=request.POST.get('custumeridfour')
        firstitemfour=request.POST.get('firstitemfour') 
        firstquantityfour=request.POST.get('firstquantityfour')
        frontlengthfour=request.POST.get('frontlengthfour')
        shoulderfour=request.POST.get('shoulderfour')
        chestfour=request.POST.get('chestfour')
        wristfour=request.POST.get('wristfour')
        hipsfour=request.POST.get('hipsfour')
        sleevesfour=request.POST.get('sleevesfour')
        bisepsfour=request.POST.get('bisepsfour')
        cufffour=request.POST.get('cufffour')
        callorfour=request.POST.get('callorfour')
        firstmessagefour=request.POST.get('firstmessagefour')

        firstimageiconfour=request.FILES['firstimageiconfour']
        if firstimageiconfour:
            firstimageiconfour= resize_and_compress_image(firstimageiconfour)
        
        
        
    
        seconditemfive=request.POST.get('seconditemfive') 
        secondquantityfive=request.POST.get('secondquantityfive')
        fulllengthfive=request.POST.get('fulllengthfive')
        waistfive=request.POST.get('waistfive')
        hipsfive=request.POST.get('hipsfive')
        thighfive=request.POST.get('thighfive')
        risefive=request.POST.get('risefive')
        kneefive=request.POST.get('kneefive')
        uplegoppeningfive=request.POST.get('uplegoppeningfive')
        legoppeningfive=request.POST.get('legoppeningfive')
        otherfive=request.POST.get('otherfive')
        secondmessagefive=request.POST.get('secondmessagefive')
        secondimageiconfive=request.FILES['secondimageiconfive']
        if secondimageiconfive:
            secondimageiconfive= resize_and_compress_image(secondimageiconfive)
    
        totalamount=request.POST.get('totalAmount')
        advanceamount=request.POST.get('advancedAmount')
        dueamount=request.POST.get('dueAmount')
            
        print("uppercloth",firstitemfour,firstquantityfour,frontlengthfour,shoulderfour,chestfour,wristfour,hipsfour,sleevesfour,bisepsfour,cufffour,callorfour,firstmessagefour,firstimageiconfour,custumerid)
            
        datafour=Upperdetsils(Item=firstitemfour,Quantity=firstquantityfour,Frontlength=frontlengthfour,Shoulder=shoulderfour,Chest=chestfour,Wrist=wristfour,Hips=hipsfour,Sleeves=sleevesfour,Biseps=bisepsfour,Cuff=cufffour,Callor=callorfour,Message=firstmessagefour,Imageicon=firstimageiconfour,Custumerid_id=custumerid)
        try:   
            datafour.save()
            msg5=" Uper cloth details register succesfully"
        except:
            msg5=" Uper cloth details not register"        
        
       
        print(custumerid,seconditemfive,secondquantityfive,fulllengthfive,waistfive,hipsfive,thighfive,risefive,kneefive,uplegoppeningfive,legoppeningfive,otherfive,secondmessagefive,secondimageiconfive)
        datafive=Lowerdetsils(Custumerid_id=custumerid,Item=seconditemfive,Quantity=secondquantityfive,Fulllength=fulllengthfive,Waist=waistfive,Hips=hipsfive,Thigh=thighfive,Rise=risefive,Knee=kneefive,Uplegoppening=uplegoppeningfive,Legoppening=legoppeningfive,Others=otherfive,Message=secondmessagefive,Imageicon=secondimageiconfive)
        try:   
            datafive.save()
            msg6=" Lower cloth details register succesfully"
        except:
            msg6=" Lower cloth details not register"
            
        payment=Paymentdetails(Totalamount=totalamount,Advanceamount=advanceamount,Dueamount=dueamount,Custumerid_id=custumerid)
        print("paymentdetails",totalamount,advanceamount,dueamount,custumerid)
        try:
            payment.save()
            msg2="payementdetails register successfully"
        except:
            msg2="payment details not register "
            
        return redirect(curl+'TailorApp/tripleclothes/'+ f'?msg={msg}&msg1={msg1}&msg2={msg2}&msg3={msg3}&msg4={msg4}&msg5={msg5}&msg6={msg6}')

    return render(request,'Tripleclothes.html',{'curl':curl,'context':obj})    
        
def editsdeatils(request):
    fam = due()  # Form initialization
    msg = ''
    data = None 
    due_data = None
    if request.method=="POST":
        if 'search' in request.POST:
            searchid=request.POST.get('searchid')
            print(searchid)
            data=Addcustumer.objects.filter(Custumerid=searchid).values('Custumer_name','Custumer_mobile','Custumerid')
            due_data=Dueset.objects.filter(Custumerid=searchid).values()
            print(data)
 
        elif 'save' in request.POST:
            fm=due(request.POST)
            if fm.is_valid():
                print("Form validated")
                print("Custumer id:",fm.cleaned_data['custumer_id'])
                print("due amount :",fm.cleaned_data['due_amount'])
                print("date:",fm.cleaned_data['date'])
                
                Custumer_id=fm.cleaned_data['custumer_id']
                Due_amount=fm.cleaned_data['due_amount']
                Date=fm.cleaned_data['date']
                data=Dueset(Custumerid=Custumer_id,Due_amount=Due_amount,dob=Date)
                try:
                    data.save()
                    msg="custumer due amount set"
                except:
                    msg="custumer due amount not set"
                print(msg)
                return redirect(curl+'TailorApp/editsdeatils',{"form1":fam,'msg':msg})
    return render(request,'EditsDetails.html',{'curl':curl ,'form1':fam,'msg':msg,'context':data,'context2':due_data})
 

def upgradeprogress(request):
    msg=""
    if request.method=="POST":
        searchid=request.POST.get('searchid')
        print(searchid)
        update123=request.POST.get('update')
        print(update123)
        try:
            Addcustumer.objects.filter(Custumerid=searchid).update(Update=update123)
            msg="updated"
        except:
            msg="not updateed"
    return render(request,'UpgradeProgress.html',{'curl':curl,'msg':msg})
def searching(request):
    if request.method=="POST":
        searchid=request.POST.get('searchid')
        print(searchid)
        
        data=Addcustumer.objects.filter(Custumerid=searchid).values('Custumer_name','Custumer_mobile','Delivery_date','Custumerid','Update')
        print(data)
        data1=Upperdetsils.objects.filter(Custumerid_id=searchid).values()
        print(data1)
        data2=Lowerdetsils.objects.filter(Custumerid_id=searchid).values()
        print(data2)
        data3=Paymentdetails.objects.filter(Custumerid_id=searchid).values()
        print(data3)
        return render(request,'Searching.html',{'curl':curl,'context':data,'context1':data1,'context2':data2,'context3':data3,'media_url':media_url})
    return render(request,'Searching.html',{'curl':curl})
    
def Settingshome(request):

    return render(request,'Settingshome.html',{'curl':curl})



def user(request):
    msg=""
    if request.method=="POST":
        searchid=request.POST.get('searchid')
        print(searchid)
        update123='Cancelled'
        try:
            Addcustumer.objects.filter(Custumerid=searchid).update(Update=update123)
            msg="Custumer deleted"
        except:
            msg="Custumer not deleted"
    return render(request,'User.html',{'curl':curl,'msg': msg })
 


from tailorrecipt.models import User






def approved(request):
    # Get the UserID from the GET request if provided
    userid = request.GET.get('userid', '')

    # Filter users based on UserID if it's provided
    if userid:
        users = User.objects.filter(userid__icontains=userid)  # Use icontains for case-insensitive search
    else:
        users = User.objects.all()  # If no UserID is entered, show all users

    return render(request, 'Approved.html', {'curl': curl, 'users': users, 'userid': userid})


def password(request):
    msg=""
    if request.method=="POST":
        searchid=request.POST.get('searchid')
        print(searchid)
        update123=request.POST.get('password')
        print(update123)
        try:
            User.objects.filter(userid=searchid).update(password=update123)
            msg="Password updated"
        except:
            msg="Password not updates"
        print(msg)
    return render(request,'Password.html',{'curl':curl,'msg':msg})

def dueview(request):
    dues = Dueset.objects.all()  # Fetch all Dueset objects
    print(dues)
    for due in dues:
        try:
            # Try to fetch Addcustumer object based on Custumerid
            add_custumer = Addcustumer.objects.get(Custumerid=due.Custumerid)
            # Add custumer name and mobile to dues object
            due.custumer_name = add_custumer.Custumer_name
            due.custumer_mobile = add_custumer.Custumer_mobile
        except Addcustumer.DoesNotExist:
            # Handle case where no Addcustumer object found for Custumerid
            due.custumer_name = "Not Found"
            due.custumer_mobile = "Not Found"
    return render(request, 'Dueview.html', {'curl':curl,'dues': dues})



def idinvoice(request):
    msg = ''
    if request.method == "POST":
        searchid = request.POST.get('searchid')
        print(searchid)

        # Check if the customer exists
        item_exists = Addcustumer.objects.filter(Custumerid=searchid).exists()
        
        if item_exists:
            latest_customer = Addcustumer.objects.get(Custumerid=searchid)

            # Get related data
            upper_details = Upperdetsils.objects.filter(Custumerid=latest_customer)
            lower_details = Lowerdetsils.objects.filter(Custumerid=latest_customer)
            payment_details = Paymentdetails.objects.filter(Custumerid=latest_customer)

            # Create a byte buffer for the PDF
            buffer = BytesIO()

            # Create a document template
            doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=inch, leftMargin=inch, topMargin=inch, bottomMargin=inch)
            elements = []

            # Define styles
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='Company', fontSize=16, leading=20, alignment=1, textColor=colors.darkblue))
            styles.add(ParagraphStyle(name='CustomTitle', fontSize=14, leading=18, textColor=colors.black))
            styles.add(ParagraphStyle(name='CustomNormal', fontSize=12, leading=14, textColor=colors.black))
            styles.add(ParagraphStyle(name='Terms', fontSize=10, leading=12, textColor=colors.grey))

            # Add company details
            elements.append(Paragraph("Murli tailor", styles['Company']))
            elements.append(Paragraph("Email: Murlitailor@gmail.com", styles['CustomNormal']))
            elements.append(Paragraph("Mobile Number: 9171809182", styles['CustomNormal']))
            elements.append(Paragraph("Address: khardon kalan shajapur, M.P", styles['CustomNormal']))
            elements.append(Spacer(1, 12))

            # Add invoice title and customer details
            elements.append(Paragraph(f"Invoice for: {latest_customer.Custumer_name} (Serial Number: {latest_customer.Custumerid})", styles['Company']))
            elements.append(Spacer(1, 5))
            current_date_time = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
            elements.append(Paragraph(f"Mobile Number: {latest_customer.Custumer_mobile}", styles['CustomNormal']))
            elements.append(Paragraph(f"Current Date: {current_date_time}", styles['CustomNormal']))
            elements.append(Paragraph(f"Delivery Date: {latest_customer.Delivery_date}", styles['CustomNormal']))
            elements.append(Spacer(1, 12))

            # Add upper clothes information
            elements.append(Paragraph("Upper Clothes Information", styles['CustomTitle']))
            upper_data = [["#", "DESCRIPTION", "QUANTITY"]]
            for i, item in enumerate(upper_details, start=1):
                upper_data.append([str(i), f"{item.Item} (Category ID: {item.Catid})", str(item.Quantity)])
            upper_table = Table(upper_data, colWidths=[30, 400, 70])
            upper_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(upper_table)
            elements.append(Spacer(1, 12))

            # Add lower clothes information
            elements.append(Paragraph("Lower Clothes Information", styles['CustomTitle']))
            lower_data = [["#", "DESCRIPTION", "QUANTITY"]]
            for i, item in enumerate(lower_details, start=1):
                lower_data.append([str(i), f"{item.Item} (Category ID: {item.Catid})", str(item.Quantity)])
            lower_table = Table(lower_data, colWidths=[30, 400, 70])
            lower_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))
            elements.append(lower_table)
            elements.append(Spacer(1, 12))

            # Add payment details
            if payment_details.exists():
                total_amount = payment_details.aggregate(Sum('Totalamount'))['Totalamount__sum'] or 0
                advance_amount = payment_details.aggregate(Sum('Advanceamount'))['Advanceamount__sum'] or 0
                due_amount = payment_details.aggregate(Sum('Dueamount'))['Dueamount__sum'] or 0
                elements.append(Paragraph("Payment Details", styles['CustomTitle']))
                payment_data = [
                    ["Total Amount", f"${total_amount}"],
                    ["Advance Amount", f"${advance_amount}"],
                    ["Due Amount", f"${due_amount}"]
                ]
                payment_table = Table(payment_data, colWidths=[150, 150])
                payment_table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ]))
                elements.append(payment_table)
                elements.append(Spacer(1, 12))

            # Add terms and conditions
            elements.append(Paragraph("Terms & Conditions", styles['CustomTitle']))
            terms = ("Customers must pick up their clothes within one month. We are not responsible for clothes left beyond this period. "
                     "Please present this receipt when collecting your clothes. Please deposit full payment when taking your clothes, as we do not accept due amounts.")
            elements.append(Paragraph(terms, styles['Terms']))
            elements.append(Spacer(1, 48))

            # Add signature
            elements.append(Paragraph("Artfullstiches", ParagraphStyle(name='Signature', fontSize=14, fontName='Helvetica-Oblique', textColor=colors.black)))
            elements.append(Spacer(1, 12))
            elements.append(Paragraph("Owner of Artfullstiches", styles['CustomNormal']))

            # Build the PDF
            doc.build(elements)

            # Get the PDF value
            buffer.seek(0)
            pdf = buffer.getvalue()
            buffer.close()

            # Save the PDF to a file
            pdf_path = f"media/invoice_{latest_customer.Custumerid}.pdf"
            with open(pdf_path, 'wb') as f:
                f.write(pdf)

            # Send the PDF via email
            email_subject = "Your Invoice from Murlitailor"
            email_body = f"Dear {latest_customer.Custumer_name},\n\n This is the invoice for your clothes from murlitalor.shop.\n\nBest regards,\nArtfullstiches"
            sendMail.sendMail(latest_customer.Emailid, subject=email_subject, html=email_body, attachment_path=pdf_path, attachment_name=f"invoice_{latest_customer.Custumerid}.pdf")

            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="invoice_{latest_customer.Custumerid}.pdf"'
            return response
        else:
            msg = f"Item with Id {searchid} does not exist."
            
    return render(request, 'Idinvoice.html', {'curl':curl,'msg': msg})




def custumerlist(request):
    msg=''
    customers =Addcustumer.objects.all()
    print(customers)
    return render(request,'Custumerlist.html',{'curl':curl,'msg':msg,'customers':customers})

def deletedue(request):
    msg = ''
    if request.method == "POST":
        searchid = request.POST.get('searchid')
        print(searchid)
        try:
            # Check if the due record exists
            due_exists = Dueset.objects.filter(Custumerid=searchid).exists()
            if due_exists:
                # Delete the due record
                Dueset.objects.filter(Custumerid=searchid).delete()
                msg = f"Due record for Customer Id {searchid} deleted successfully."
            else:
                msg = f"No due record found for Customer Id {searchid}."
        except Exception as e:
            msg = f"An error occurred while deleting the due record: {str(e)}"
        print(msg)

    return render(request, 'Deletedue.html', {'curl': curl, 'msg': msg})

    
def deleteitemu(request):
    msg = ''
    if request.method == "POST":
        searchid = request.POST.get('searchid')
        print(searchid)
        try:
            # Check if the item exists
            item_exists = Upperdetsils.objects.filter(Catid=searchid).exists()
            if item_exists:
                # Delete the item
                Upperdetsils.objects.filter(Catid=searchid).delete()
                msg = f"Item with Id {searchid} deleted successfully from Upper details."
            else:
                msg = f"No item found with Id {searchid} in Upper details."
        except Exception as e:
            msg = f"An error occurred while deleting the item: {str(e)}"
        print(msg)

    return render(request, 'Deleteupper.html', {'curl': curl, 'msg': msg})

def deleteiteml(request):
    msg = ''
    if request.method == "POST":
        searchid = request.POST.get('searchid')
        print(searchid)
        try:
            # Check if the item exists
            item_exists = Lowerdetsils.objects.filter(Catid=searchid).exists()
            if item_exists:
                # Delete the item
                Lowerdetsils.objects.filter(Catid=searchid).delete()
                msg = f"Item with Id {searchid} deleted successfully from Lower details."
            else:
                msg = f"No item found with Id {searchid} in Lower details."
        except Exception as e:
            msg = f"An error occurred while deleting the item: {str(e)}"
        print(msg)

    return render(request, 'Deletelower.html', {'curl': curl, 'msg': msg})


def deletecustumer(request):
    msg = ''
    if request.method == "POST":
        Custumerid = request.POST.get('searchid')
        print(Custumerid)
        try:
            # Check if the customer exists
            customer_exists = Addcustumer.objects.filter(Custumerid=Custumerid).exists()
            if customer_exists:
                # Delete the customer
                Addcustumer.objects.filter(Custumerid=Custumerid).delete()
                msg = "Customer deleted successfully."
            else:
                msg = f"Customer with Id {Custumerid} does not exist."
        except Exception as e:
            msg = f"An error occurred: {str(e)}"
        print(msg)
    
    return render(request, 'Deleteuser.html', {'curl': curl, 'msg': msg})



# def filter(request):
#     msg=''
#     customers =models.Addcustumer.objects.all()
#     for custumer in customers:
#         try:
#             addcustumer=models.Paymentdetails.objects.get(Custumerid=custumer.Custumerid)
#             customers.Totalamount=addcustumer.Totalamount
#             customers.Advanceamount=addcustumer.Advanceamount
#             customers.Dueamount=addcustumer.Dueamount
#         except models.Paymentdetails.DoesNotExist:
#             customers.Totalamount="Not Found"
#             customers.Advanceamount="Not Found"
#             customers.Dueamount="Not Found"
#     return render(request,'Filter.html',{'curl':curl,'msg':msg,'customers':customers})

from django.shortcuts import render
from django.db.models import Sum
from . import models
from tailorrecipt.models import User,Addcustumer,Lowerdetsils,Upperdetsils,Paymentdetails,Dueset,clothbooking
def filter(request):
    msg = ''
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Filter customers within the date range if provided
    if start_date and end_date:
        customers = Addcustumer.objects.filter(Delivery_date__range=[start_date, end_date])
    else:
        customers = Addcustumer.objects.all()

    for customer in customers:
        payment_details = Paymentdetails.objects.filter(Custumerid=customer.Custumerid)

        if payment_details.exists():
            total_amount = payment_details.aggregate(Sum('Totalamount'))['Totalamount__sum'] or 0
            advance_amount = payment_details.aggregate(Sum('Advanceamount'))['Advanceamount__sum'] or 0
            due_amount = payment_details.aggregate(Sum('Dueamount'))['Dueamount__sum'] or 0

            customer.Totalamount = total_amount
            customer.Advanceamount = advance_amount
            customer.Dueamount = due_amount
        else:
            customer.Totalamount = "Not Found"
            customer.Advanceamount = "Not Found"
            customer.Dueamount = "Not Found"

    return render(request, 'Filter.html', {'curl':curl,'msg': msg, 'customers': customers, 'start_date': start_date, 'end_date': end_date})



def some_protected_view(request):
    if 'email' not in request.session:
        return redirect('login')
    # ... rest of your view code ...
    
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect('index')


def bookings(request):
    msg = ''
    
    # Get the Booking_Id filter value from the request (if any)
    booking_id = request.GET.get('booking_id', None)
    
    # Fetch all cloth bookings, filtered by Booking_Id if provided
    if booking_id:
        customers = clothbooking.objects.filter(Booking_Id=booking_id)
    else:
        customers = clothbooking.objects.all()
    
    # Iterate over each booking and add extra fields from the User model
    for customer in customers:
        try:
            # Fetch the user based on the email field
            user = User.objects.get(email=customer.Mail_Id)
            # Dynamically add 'userid' and 'name' attributes to the customer object
            customer.userid = user.userid
            customer.name = user.name
        except User.DoesNotExist:
            # If no user is found, set default values
            customer.userid = None
            customer.name = "Unknown"
    
    # Render the template with the updated customers list and filter value
    return render(request, 'bookings_list.html', {
        'curl': curl,
        'msg': msg,
        'customers': customers,
        'booking_id': booking_id
    })


