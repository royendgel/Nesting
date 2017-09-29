from django.shortcuts import render
from Identities.forms import CreateAccountForm

# Create your views here.

def nest(request):
	
	return render(request, 'Identities/nest.html')



def register(request):
	
	if request.method == 'POST':
		
		form = CreateAccountForm(request.POST)
		
		if form.is_valid():
			form.save()
			
		else:
			return redirect(reverse('Identities:logout'))
		
	else:
		
		form = CreateAccountForm()
		var = {'form' : form}
		return render(request, 'Identities/create_account.html', var)
		