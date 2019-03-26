from django import forms
from .models import PatientDetails

class PatientDetailsForm(forms.ModelForm):


    gender = forms.ChoiceField(choices=PatientDetails.GENDER_CHOICES, required=True, widget=forms.Select(attrs={'class': "form-dropdown", 'id': "gender"}))
    date = forms.ChoiceField(choices=PatientDetails.DATE_CHOICES, required=True, widget=forms.Select(attrs={'class': "form-dropdown"}))
    month = forms.ChoiceField(choices=PatientDetails.MONTH_CHOICES, required=True, widget=forms.Select(attrs={'class': "form-dropdown"}))
    year = forms.ChoiceField(choices=PatientDetails.YEAR_CHOICES, required=True, widget=forms.Select(attrs={'class': "form-dropdown"}))
    #illnesses = forms.ModelMultipleChoiceField(choices=PatientDetails.ILLNESS_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': "form-checkbox"}), queryset=None)

    class Meta:
        model = PatientDetails
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "form-textbox",
                                                 'id': "first_name"}),
            'last_name': forms.TextInput(attrs={'class': "form-textbox",
                                                'id': "last_name"}),
            'email': forms.TextInput(attrs={'class': "form-textbox",
                                            'style': "width:400px",
                                            'id': "email-id",
                                            'readonly': "True"}),
            'height': forms.TextInput(attrs={'class': "form-textbox",
                                             'style': "width:60px",
                                             'placeholder': "ex: 176",
                                             'id': "height"}),
            'weight': forms.TextInput(attrs={'class': "form-textbox",
                                             'style': "width:60px",
                                             'placeholder': "ex: 70",
                                             'id': "weight"}),
            'reason': forms.TextInput(attrs={'class': "form-textbox",
                                            'style': "width:400px"}),
            'prescribed_tablets': forms.TextInput(attrs={'class': "form-textbox",
                                                        'style': "width:400px"}),
            'drug_allergies': forms.Textarea(attrs={'class': "form-textbox"}),
            'other_illnesses': forms.TextInput(attrs={'class': "form-textbox"}),
            'operations': forms.Textarea(attrs={'class': "form-textbox"}),
            'current_medications': forms.Textarea(attrs={'class': "form-textbox"}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['email'] = '123@qwe.com'
