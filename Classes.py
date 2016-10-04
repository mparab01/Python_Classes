
# coding: utf-8

# Q. Create a methode to find an area of a circle using OOP.

# In[15]:

class area:
    pi = 3.14
    def __init__ (self, radius=1):
        self.radius = radius
        
    def area(self):
        return circle.pi * self.radius**2
       
    def perimeter(self):
        return 2*circle.pi*self.radius
    


# In[16]:

d = circle(radius=2)


# In[17]:

d.area()


# In[19]:

d.radius


# In[20]:

d.pi


# In[ ]:



