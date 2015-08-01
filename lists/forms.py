from django import forms

from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"

class ItemForm(forms.models.ModelForm): #Note ModelForm
    item_text = forms.CharField(
        widget=forms.fields.TextInput(attrs={  #change the form.as_p
            'placeholder': 'Enter a to-do item',
            'class': 'form-control input-lg',
        }),
    )
    
    class Meta:   #Which Model the Form is for and which fields to use
        model = Item
        fields = ('text',)  
        widgets = {'text': forms.fields.TextInput(attrs={
                    'placeholder': 'Enter a to-do item',
                    'class': 'form-control input-lg',
                  }),
        }
        error_messages = {'text': {'required': EMPTY_ITEM_ERROR}
        }