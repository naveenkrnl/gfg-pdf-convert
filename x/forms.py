from django import forms  
    
# creating a form   
class InputForm(forms.Form):  
    URL = forms.URLField()

    def clean_URL(self):
        value=self.cleaned_data.get("URL")
        if "geeksforgeeks.org" not in value:
            raise forms.ValidationError("Only Geeksforgeeks articles can be downloaded")
        return value