from django import forms

class AssessmentForm(forms.Form):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('professional', 'Professional'),
    ]

    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)
    
    INTEREST_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('web', 'Web Development'),
        ('data', 'Data Science'),
        ('cyber', 'Cybersecurity'),
        ('design', 'UI/UX Design'),
    ]
    interests = forms.MultipleChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
