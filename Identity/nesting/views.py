from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from nesting.forms import Identity_Form, Symptom_Form
from nesting.models import Identity_unique, Symptoms

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

    model = Symptoms

    template_name = 'nesting/Symptoms_list.html'

    def get(self, request):

        form = Symptom_Form()


        Symptoms_desc = Symptoms.objects.all()


        var = {'form':form, 'Symptoms_desc':Symptoms_desc}


        return render(request, self.template_name, var)



    def post(self, request):

        form = Symptom_Form(request.POST or None)

        Symptom_content = None

        if form.is_valid():

            Symptoms_description = form.save(commit = False)
            Symptoms_description.user = request.user
            Symptoms_description.save()

            Symptom_content = form.cleaned_data['Symptoms_description']

            form = Symptom_Form()


            redirect('nesting:nesting')

        var = {'form': form, 'Symptom_content': Symptom_content}

        return render(request, self.template_name, var)




class Symptom_nest_list_view(TemplateView):

    pass
