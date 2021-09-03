from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=5, error_messages={
        "required": "Please enter your name!",
        "max_length": "Please enter a shorter name!"
    })
