from django.shortcuts import render
from django.core.mail import EmailMessage  # Import EmailMessage for sending emails
from django.http import JsonResponse  # Import JsonResponse for AJAX responses
from .forms import ContactForm

def index(request):
    form = ContactForm()
    message_name = ''

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            try:
                # Prepare the email content
                full_message = (
                    f"New message from contact form:\n\n"
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Subject: {subject}\n\n"
                    f"Message:\n{message}"
                )
                
                # Create the email
                email_message = EmailMessage(
                    subject=f"Website Inquiry: {subject}",
                    body=full_message,
                    from_email='no-reply@olivia_le.com',  # Your email as the sender
                    to=['hello@olivia-le.com'],  # Your email as the recipient
                    reply_to=[email]  # User's email for the reply-to field
                )

                # Send the email
                email_message.send(fail_silently=False)

                # Response for AJAX request
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': 'Your message has been sent!'})
                else:
                    message_name = 'Your message has been sent'
            except Exception as e:
                # Handle any errors that occur
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': f'Failed to send email: {str(e)}'}, status=500)
                else:
                    message_name = f'Error sending email: {str(e)}'

    return render(request, 'index.html', {'form': form, 'message_name': message_name})
