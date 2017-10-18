from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from nesting.forms import Identity_Form, Symptom_Form
from nesting.models import Identity_unique, Symptom_relation

# Create your views here.

class Identity_view(TemplateView):

    template_name = 'nesting/nesting.html'

    def get(self, request):
        # Create view logic

        # Instantiate Identity Form

        form = Identity_Form()

        Identities = Identity_unique.objects.filter(user = request.user)

        var = {'form': form, 'Identities': Identities}

        return render(request, self.template_name, var)

    def post(self, request):

        # Create a form instance and populate it with data from the request

        form  = Identity_Form(request.POST or None)

        content = None

        # Assess whether the data is valid

        if form.is_valid():

            NIS = form.save(commit = False)
            NIS.user = request.user
            NIS.save()

            # process the data in form.cleaned_data as required
            content = form.cleaned_data['NIS']

            form = Identity_Form()

# redirect to nesting url
            return redirect('nesting:nesting')

        var = {'form': form, 'content': content}

        return render(request,self.template_name, var)



# Sript code to ensure that if the user reloads it returns a fresh from for the user to fill.

class Identity_nest_list_view(TemplateView):

    # Create Identity_nest_list_view logic

    model = Identity_unique

    template_name = 'nesting/Identity_nest.html'


    def get(self, request):

        form = Identity_Form()

        Identities = Identity_unique.objects.filter(user = request.user).order_by('-Timestamp')
        var = {'form':form, 'Identities': Identities}
        return render(request, self.template_name, var)





class Symptoms_document_view(TemplateView):

    model = Symptom_relation

    template_name = 'nesting/Symptoms_list.html'

    def get(self, request, pk):

        form = Symptom_Form()


        Symptoms_desc = Symptom_relation.objects.all()[:1]
        # Symptoms_desc = Identity_unique.objects.get(pk=pk).Symptom_relation_set


        var = {'form':form, 'Symptoms_desc':Symptoms_desc}


        return render(request, self.template_name, var)



    def post(self, request, pk):

        form = Symptom_Form(request.POST )

        Symptom_content = None

        if form.is_valid():

            Symptom_description = form.save(commit = False)
            Symptom_description.user = request.user
            Symptom_content = form.cleaned_data['Symptom_description']

            Symptom_description.save()
            ident = Identity_unique.objects.get(pk=pk)

            Symptom_description.Unique_Identity.add(ident)
            Symptom_description.save()

            form = Symptom_Form()


            redirect('nesting:nesting')

        var = {'form': form, 'Symptom_content': Symptom_content}

        return render(request, self.template_name, var)




class Medical_History_nest_view(TemplateView):


    model = Symptom_relation

    template_name = 'nesting/Medical_History_nest.html'

    def get(self, request, pk):

        form = Symptom_Form()

        Symptoms_desc = Symptom_relation.objects.all()
        Symptoms_desc = Identity_unique.objects.get(pk=pk).symptoms.all()

        var = {'form':form, 'Symptoms_desc':Symptoms_desc}

        return render(request, self.template_name, var)
