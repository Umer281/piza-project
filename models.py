from django.db import models

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
    
        
    

    