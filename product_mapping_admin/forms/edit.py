from django import forms


class EditForm(forms.Form):

    DELIVERY_METHODS = (
        ('code', 'Code'),
        ('url', 'URL')

    )

    product_id = forms.CharField(widget=forms.HiddenInput())
    brand = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Brand Slug'}))
    delivery_method = forms.ChoiceField(choices=DELIVERY_METHODS)
