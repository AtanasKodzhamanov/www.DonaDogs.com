from django import forms 
from django.forms import CharField, Select
from django.utils.translation import gettext_lazy as _


from DogShelter.web.models import AdoptionForm, NewsletterSubscriber

# Subscribe for the newsletter form
class SubscribeForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = "__all__"

# Contact form
class ContactForm(forms.Form):
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    subject = forms.CharField(required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')

# Adopt form
class AdoptForm(forms.Form):
    name = forms.CharField(required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    phone = forms.CharField(required=True, label='Phone')   
    city = forms.CharField(required=True, label='City')
    country = forms.CharField(required=True, label='Country')
    dog = forms.CharField(required=True, label='Dog Name')

    class Meta:
        model = AdoptionForm

# Dog filter form

class DogFilterForm(forms.Form):
    dog_name = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            'name': 'dogName',
            'id': 'dogName',
            'placeholder': _('Input name'),
        }),
    )

class vaStatusForm(forms.Form):
    # Define the form fields
    adoption_status = forms.CharField(
        label=_("Virtual Adoption Status"),
        widget=Select(choices=(
            ("all", _("All dogs")),
            ("va", _("Virtually Adopted")),
            ("no", _("No Adoptors")),
        ))
    )
    adoption_status.widget.attrs.update({
        'name': 'adoptionStatus',
        'id': 'adoptionStatus',
    })

class genderFilterForm(forms.Form):
    gender = forms.CharField(
        label=_("Gender"),
        widget=Select(choices=(
            ("all", _("All genders")),
            ("male", _("M")),
            ("female", _("F")),
        ))
    )
    gender.widget.attrs.update({
        'name': 'genderFilter',
        'id': 'genderFilter',
    })