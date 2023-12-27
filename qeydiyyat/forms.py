from django.forms import ModelForm
from . models import AdminQeydiyyatForm, AdminSinaqQeydiyyatForm, AdminElaqeForm

class QeydiyyatForm(ModelForm):
    class Meta:
        model = AdminQeydiyyatForm
        fields = '__all__'

class SinaqQeydiyyatForm(ModelForm):
    class Meta:
        model = AdminSinaqQeydiyyatForm
        fields = '__all__'

class ElaqeForm(ModelForm):
    class Meta:
        model = AdminElaqeForm
        fields = '__all__'