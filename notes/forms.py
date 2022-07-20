
class MainForm(forms.Form):
    name = forms.CharField(initial='Name')
    comment = forms.CharField(initial='Comment')