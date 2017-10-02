from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from nesting.forms import Identity_form
from nesting.models import Identity_unique

# Create your views here.

class Identity_view(TemplateView):

    template_name = 'nesting/nesting.html'

    def get(self, request):

        form = Identity_form()

        Identities = Identity_unique.objects.filter(user = request.user)
        var = {'form': form, 'Identities': Identities}
        return render(request, self.template_name, var)

    def post(self, request):

        form  = Identity_form(request.POST)

        if form.is_valid():

            NIS = form.save(commit = False)
            NIS.user = request.user
            NIS.save()

            content = form.cleaned_data['NIS']

            form = Identity_form()

            return redirect('nesting:nesting')

        var = {'form': form, 'content': content}

        return render(request,self.template_name, var)
