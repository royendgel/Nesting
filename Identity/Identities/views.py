from django.shortcuts import render, redirect
from django.urls import reverse


from Identities.forms import CreateAccountForm, UpdateAccountForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def nest(request):

	return render(request, 'Identities/nest.html')



def register(request):

	# If   the method is a POST request

	if request.method == 'POST':

# Create the form object containing the type of request
		form = CreateAccountForm(request.POST)

# If the data populating the fields are valid then save the form and redirect
# to home page
		if form.is_valid():
			form.save()
			return redirect('/Identity')

		else:
			return redirect(reverse('Identities:logout'))

	else:

		form = CreateAccountForm()
		var = {'form' : form}
		return render(request, 'Identities/create_account.html', var)



def view_profile(request):

	var = {'user': request.user}

	return render(request, 'Identities/profile.html', var)


def edit_profile(request):

	if request.method == 'POST':

		form = UpdateAccountForm(request.POST, instance = request.user)


		if form.is_valid():
			form.save()

			return redirect(reverse('Identities:view_profile'))

		else:
			return redirect('Identities/profile/edit')


	else:

		form = UpdateAccountForm(instance = request.user)

		var = {'form' : form }

		return render(request, 'Identities/edit_profile.html', var)


def change_password(request):

	if request.method == 'POST':

		form = PasswordChangeForm(data = request.POST, user = request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('Identities:login'))

		else:

			return redirect('/Identity/change-password')
	else:

		form = PasswordChangeForm(user = request.user)

		var = {'form': form}

		# Create change_password instance a place in the the template context
		return render(request, 'Identities/change_password.html', var)
