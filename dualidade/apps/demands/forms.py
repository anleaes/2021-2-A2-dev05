
from django import forms


class demandsForm(forms.ModelForm):
    
    class Meta:
      
        exclude = ('demands', 'created_on' , 'updated_on')

class demandsItemForm(forms.ModelForm):
    
    class Meta:
       
        exclude = ('demands', 'created_on' , 'updated_on')

