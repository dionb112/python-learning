
# coding: utf-8
bottles = 99

for bottles > 0:
    print bottles
# In[1]:


# My First Python Project
bottle_message = "bottles of beer."
for bottles in range(99, 0, -1):
    print(bottles, bottle_message, 'on the wall.')
    print(bottles, bottle_message)
    print('Take one down.')
    print("Pass it around.")
    bottles = bottles - 1
    if bottles == 1:
        bottle_message = "bottle of beer"
    if bottles == 0:
        print("No more bottles of beer on the wall.")
    else:
        print(bottles, bottle_message, ' on the wall.')
    print()

        

