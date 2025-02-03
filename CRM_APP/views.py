from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CRM_APP.models import Customer
from CRM_APP.forms import CustomerForm,SignupForm,SignInForm
from django.views.generic import View,CreateView,FormView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


class SignupView(CreateView):
    form_class=SignupForm
    template_name="signup.html"
      
    def get(self,request,*args,**kwargs):

            form_instance=self.form_class()

            return render(request,self.template_name,{"form":form_instance})
        
    def post(self,request,*args,**kwargs):

            form_instance=self.form_class(request.POST)

            if form_instance.is_valid():

                form_instance.save()

                print("Account created Succesfully")

                return redirect("signin")
            
            else:

                print("failed to create account")

                return render(request,self.template_name,{"form":form_instance})

     
class SigninView(FormView):

    template_name='SigninForm.html'
    
    form_class=SignInForm

    def post(self,request,*args,**kwargs):

        form_instance=self.form_class(request.POST)

        if form_instance.is_valid():

            username=form_instance.cleaned_data.get('username')
            password=form_instance.cleaned_data.get('password')

            user_obj=authenticate(username=username,password=password)

            if user_obj:

                login(request,user_obj)

                return redirect('dashboard')
            return render(request,self.template_name,{"form":form_instance})



@login_required
def dashboard(request):
    user = request.user  # Get the logged-in user
    total_customers = Customer.objects.filter(user=user).count()  # Count only user's customers
    recent_customer = Customer.objects.filter(user=user).last()  # Get the most recent customer for this user
    
    return render(request, 'dashboard.html', {
        'total_customers': total_customers,
        'recent_customers': recent_customer
    })

@login_required
def customer_list(request):
    customers = Customer.objects.filter(user=request.user)  # Only show customers of logged-in user
    return render(request, 'customer_list.html', {'customers': customers})

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.user = request.user  # Assign the logged-in user
            customer.save()
            return redirect('dashboard')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})

@login_required
def customer_update(request, id):
    customer = Customer.objects.get(id=id, user=request.user)  # Ensure user can only edit their customers
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer_form.html', {'form': form})

@login_required
def customer_delete(request, id):
    customer = Customer.objects.get(id=id, user=request.user)
    customer.delete()
    return redirect('dashboard')

def Logout_View(request):
    logout(request)
    return redirect("signin")
