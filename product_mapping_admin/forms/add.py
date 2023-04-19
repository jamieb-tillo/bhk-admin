from django import forms



class AddForm(forms.Form):

    DELIVERY_METHODS = (
        ('', ' - Select -'),
        ('code', 'Code'),
        ('url', 'URL')

    )

    product_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Product ID'}))
    brand = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Brand Slug'}))
    delivery_method = forms.ChoiceField(choices=DELIVERY_METHODS)