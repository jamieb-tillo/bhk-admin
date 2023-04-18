from django import forms



class AddForm(forms.Form):

    DELIVERY_METHODS = (
        ('code', 'Code'),
        ('url', 'URL')

    )

    product_id = forms.CharField()
    brand = forms.CharField()
    delivery_method = forms.ChoiceField(choices=DELIVERY_METHODS)