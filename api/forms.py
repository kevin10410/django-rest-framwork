from django import forms

from .models import Status

class StatusForm(forms.ModelForm):
    
    class Meta:
      model = Status
      fields = [
        'user',
        'content',
        'image',
      ]

    def clean(self):
        data = self.cleaned_data
        content = data.get('content', None)

        content = None if content == "" else content
        image = data.get('image', None)

        if content == None and image == None:
          raise forms.ValidationError('Content or image is required')

        return super().clean()