# piza-project
# Models.py ---we will be creating database tables for our application using Django models.in this we are creating Piza object with fields piza_shape,piza_size,piza_toping,it contains behaviour or properties of object we are storing
#from django.db import models

# Create your models here.
Piza_Shape=[('Regular','Regular'),('Square','Square')]
Piza_Size=[('small','small'),('medium','medium'),('large','large')]
Piza_topping=[('Cheese','Cheese'),('Tomato','Tomato'),('Onion','Onion'),('Corn','Corn'),('Capicum','Capcicum')]
class Piza(models.Model):
    piza_topping=models.CharField(max_length=10,choices=Piza_topping)
    piza_shape=models.CharField(max_length=10,choices=Piza_Shape)
    piza_size=models.CharField(max_length=10,choices=Piza_Size)


    def __str__(self):
        return f'{self.piza_shape,self.piza_size,self.piza_topping} piza ordered'
        
  # order.py----in this we have created form using Modelform which basically forms 'form' using model properties in this piza_shape,piza_size,piza_toping are properties
  in order to display them to user so that he can select properties of his choice and order piza
  
  #views.py---in this we have created function 'Order' which check if the user has made request to order pizza,if he has made we are storing that form containing post request in our database and sending him to items page where message order placed successfully gets displayed,function stored items displays the stored objects of model Piza
