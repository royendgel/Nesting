from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from nesting.forms import Identity_Form
from nesting.models import Identity_unique

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
