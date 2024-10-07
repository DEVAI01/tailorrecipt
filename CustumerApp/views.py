# views.py
from django.shortcuts import render,redirect
from django.conf import settings
from tailorrecipt import models
from tailorrecipt.models import clothbooking
curl = settings.CURRENT_URL
media_url = settings.MEDIA_URL

from django.shortcuts import render
 # Assuming the User model is in the same app

def custumer(request):
    # Get email from session or default to 'Guest'
    email = request.session.get('email', 'Guest')

    # Initialize a message
    msg = 'Thanks for choosing us'

    # Initialize user_details as None
    user_details = None

    # If the email is not 'Guest', try to fetch the user from the User model
    if email != 'Guest':
        try:
            user_details = models.User.objects.get(email=email)
        except user_details.DoesNotExist:
            msg = 'User not found'

    # Print the email for debugging purposes
    print(user_details)

    # Render the page with the necessary context
    return render(request, 'CustumerHome.html', {'curl': curl,'msg': msg,'email': email,'user_details': user_details})



def bookings(request):
   # Base URL or modify as per your setup
    msg = ''
    email = request.session.get('email', 'Guest')
    booking_id = None
    mobile = None  # Initialize mobile as None

    try:
        # Fetch the user details based on the email
        user_details = models.User.objects.get(email=email)
        mobile = user_details.mobile  # Assuming 'mobile' is a field in the User model
        print(f"Phone number: {mobile}")
    except models.User.DoesNotExist:
        msg1 = 'User not found'
        print(msg1)

    if request.method == 'POST':
        # Extract form data from POST request
        upper_wear = request.POST.getlist('upper_wear')
        lower_wear = request.POST.getlist('lower_wear')
        description = request.POST.get('description')
        quantity = request.POST.get('quantity')
        
        print("Upper Wear: ", upper_wear)
        print("Lower Wear: ", lower_wear)
        print("Description: ", description)
        print("Quantity: ", quantity)

        # Save form data in the clothbooking model
        data = clothbooking(
            Mail_Id=email,
            Mobile_No=mobile,
            Upper_Wear=upper_wear,
            Lower_Wear=lower_wear,
            Description=description,
            quantity=quantity
        )

        try:
            data.save()  # Save the booking
            booking_id = data.Booking_Id  # Retrieve the Booking_Id after saving
            msg = f"Booking confirmed! Your Booking ID is {booking_id}"
        except Exception as e:
            print("Error saving details:", e)
            msg = "Booking not confirmed"
        
        # Render template with message and booking ID after POST request
        return render(request, 'Bookings.html', {
            'curl': curl,
            'msg': msg,
            'email': email,
            'booking_id': booking_id
        })
    all_bookings = clothbooking.objects.filter(Mail_Id=email)
    # If it's a GET request, render the page without processing the form
    return render(request, 'Bookings.html', {
        'curl': curl,
        'msg': msg,
        'email': email,
        'booking_id': booking_id,
        'all_bookings':all_bookings
    })


def chatus(request):
    email = request.session.get('email', 'Guest')
    msg = ''
    print(email)
    return render(request, 'Chatus.html', {'curl': curl, 'msg': msg, 'email': email})
    
def custumersettings(request):
    msg = ''
    email = request.session.get('email', 'Guest')
    print(email)
    return render(request, 'Settings.html', {'curl': curl, 'msg': msg, 'email': email})

    
def services(request):
    msg = ''
    email = request.session.get('email', 'Guest')
    print(email)
    return render(request, 'Services.html', {'curl': curl, 'msg': msg, 'email': email})



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



from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.units import inch
from io import BytesIO

def download_receipt(request, booking_id):
    try:
        booking = clothbooking.objects.get(Booking_Id=booking_id)
    except clothbooking.DoesNotExist:
        return HttpResponse("Booking not found", status=404)

    email = booking.Mail_Id
    try:
        user_details = models.User.objects.get(email=email)
    except models.User.DoesNotExist:
        return HttpResponse("User not found", status=404)

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Watermark
    p.setFillColorRGB(0.9, 0.9, 0.9)  # Light color for watermark
    p.setFont("Helvetica-Bold", 60)
    p.saveState()
    p.translate(width / 2, height / 2)  # Move to the center of the page
    p.rotate(45)  # Rotate the watermark
    p.drawCentredString(0, 0, "Murli Tailor")  # Draw the watermark
    p.restoreState()

    # Header
    p.setFillColorRGB(0.2, 0.2, 0.6)  # Dark blue color
    p.rect(0, height - inch, width, inch, fill=1)
    p.setFillColorRGB(1, 1, 1)  # White color for text
    p.setFont("Helvetica-Bold", 24)
    p.drawCentredString(width / 2, height - 0.65 * inch, "Murli Tailor")
    p.setFont("Helvetica", 14)
    p.drawCentredString(width / 2, height - 0.85 * inch, "Receipt")

    # Booking Details Table
    data = [
        ['Booking ID:', booking.Booking_Id],
        ['Name:', user_details.name],
        ['Email:', booking.Mail_Id],
        ['Mobile:', user_details.mobile],
        ['Date:', booking.date],
        ['Upper Wear:', booking.Upper_Wear],
        ['Lower Wear:', booking.Lower_Wear],
        ['Quantity:', booking.quantity]
    ]

    table = Table(data, colWidths=[1.5 * inch, 4 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (0, 1), (1, 1), colors.lightyellow),  # Highlight customer name row
        ('FONTNAME', (0, 1), (1, 1), 'Helvetica-Bold'),  # Make customer name bold
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    table.wrapOn(p, width, height)
    table.drawOn(p, inch, height - 4.5 * inch)

    styles = getSampleStyleSheet()
    note_style = ParagraphStyle('Note', parent=styles['Normal'], fontSize=10, textColor=colors.grey, alignment=1)
    condition_style = ParagraphStyle('Condition', parent=styles['Normal'], fontSize=8, textColor=colors.grey, alignment=1)

    note = Paragraph("Note: This booking will be processed after 5 days from the booking date.", note_style)
    condition = Paragraph("This receipt is for booking purposes only. Purchase conditions will be applied on demand.", condition_style)

    # Adjust the Y-coordinates to reduce the gap
    note.wrapOn(p, 6 * inch, inch)
    condition.wrapOn(p, 6 * inch, inch)

    note.drawOn(p, inch, height - 5.5 * inch)  # Adjust this value for positioning
    condition.drawOn(p, inch, height - 5.8 * inch)  # Adjust this value for positioning

    # Signature at the bottom left
    p.setFont("Helvetica-Bold", 12)
    p.drawString(inch, inch, "Murli Tailor")  # Draw signature text at the bottom left

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{booking_id}.pdf"'
    response.write(pdf)

    return response



