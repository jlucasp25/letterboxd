from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=255, required=True)
    age = forms.IntegerField(label='Age', required=True)
    phone = forms.CharField(label='Phone', max_length=20, required=False)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Message',widget=forms.Textarea, required=True)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.endswith("outlook.com"):
            raise forms.ValidationError('Please enter a non-spam email address!')
        return email

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise forms.ValidationError('You must be 18 years or older to submit this form!')
        return age

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if not phone:
            return ""
        return "+351" + phone

    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get("age")
        phone = cleaned_data.get("phone")
        if age > 18 and not phone:
            raise forms.ValidationError("Phone is required if age is provided!")
        return cleaned_data

    def send_email(self):
        message = f"""
        You got a message on the website:
        Name: {self.cleaned_data["name"]}
        Age: {self.cleaned_data["age"]}
        Phone: {self.cleaned_data["phone"]}
        Email: {self.cleaned_data["email"]}
        Message: {self.cleaned_data["message"]}
        """
        send_mail(
            subject='Contact Form Submission',
            message=message,
            from_email="formacao@fc.up.pt",
            recipient_list=["admin@admin.com"],
            fail_silently=True,
        )