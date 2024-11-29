

from django.forms import ModelForm
from hospital.models import Hospital
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout,Row, Column, HTML, Fieldset
from crispy_forms.bootstrap import InlineRadios, FormActions 


class HospitalCreate(ModelForm):
    class Meta:
        model=Hospital
        fields=[
            'name',  
    'address' ,
    'phone_number',
    'email' ,
    'website' ,
    'established_date' ,
    'about' ,
    'capacity',
            
        ]
    
    def __init__(self, *args, **kwargs):
        super(HospitalCreate, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(

            HTML("""<b class="text-dark"> Child's full names</b> <hr>"""),

            Row(
                Column( 'name'),
                Column('address'),
                Column('phone_number'),
            ),
            HTML(""" <hr>"""),
            Row(
                Column('capacity'),
                Column('email'),
                 Column('website'),
                Column('established_date')
            ),
            HTML("""<b class="text-dark"> Child's Gender and Talent </b> <hr>"""),
            Row(
           
                Column('about'),
            ),
           

             HTML("""<hr> """),
            FormActions(
                Submit('save', 'Save',css_class='mx-4 px-4 btn btn-success'),
                Submit('save_and_add_another', 'Save and Add Another',css_class=' mx-2 px-4 btn btn-warning text-end'),   
                HTML(""" {% if request.GET.next %} <input type="hidden" name="next" value="{{ request.GET.next }}"/> {% endif %}"""),
            )
        )

        