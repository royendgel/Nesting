from django import forms
from nesting.models import Identity_unique
from nesting.models import Symptoms

class Identity_Form(forms.ModelForm):

    NIS = forms.CharField(
                    widget=forms.TextInput(
                            attrs={

                                'placeholder': 'Enter NIS',
                                'class' : 'form-control'
                            }
                )
    )

    First_Name = forms.CharField(
                widget=forms.TextInput(
                        attrs={

                            'placeholder': 'Enter First Name',
                            'class' : 'form-control'
                        }
            )
    )
    Last_Name = forms.CharField(

       widget=forms.TextInput(
               attrs={

                   'placeholder': 'Enter Last Name',
                   'class' : 'form-control'
               }
        )
    )

    location = forms.CharField(

            widget=forms.TextInput(
                        attrs= {

                        'placeholder':'Enter Address',
                        'class':'form-control'

                        }
            )
    )

    date_of_birth = forms.CharField(

                widget=forms.TextInput(
                            attrs= {

                            'placeholder':'Enter Date of Birth',
                            'class':'form-control'

                            }
                )
        )

    Contact = forms.CharField(

                    widget=forms.TextInput(
                                attrs= {

                                'placeholder':'Enter Contact',
                                'class':'form-control'

                                }
                    )
            )


    class Meta:

        model = Identity_unique

        fields = ('NIS', 'First_Name', 'Last_Name', 'location', 'date_of_birth', 'Contact',)



class Symptoms_Form(forms.ModelForm):


    Symptoms_description = forms.CharField()


    class Meta:

        model = Symptoms

        fields = ('Symptoms_description',)
