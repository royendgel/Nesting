from django import forms
from nesting.models import Identity_unique
from nesting.models import Symptom_relation


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

    date_of_birth = forms.DateField(

            required = False,
                widget=forms.TextInput(
                            attrs= {

                            'placeholder' : 'Enter birth day',
                            'class':'form-control'

                            }
                ),
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




class Symptom_Form(forms.ModelForm):


                Symptom_description = forms.CharField(

                widget=forms.Textarea(
                            attrs= {

                            'placeholder':'Symptom description',
                            'class':'form-control'

                            }
                )
    )

                Symptom_name = forms.CharField(


                    widget=forms.TextInput(
                                attrs= {

                                'placeholder':'Symptom Name',
                                'class':'form-control'

                                }
                    )

                )

                class Meta:

                    model = Symptom_relation

                    fields = ('Symptom_name', 'Symptom_description',)
