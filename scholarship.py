
# coding: utf-8

# In[1]:


from pyquery import PyQuery as pq
import re
import tkinter as tk
window = tk.Tk()
window.title('scholarship')
window.geometry('600x125')
doc = pq(url="http://www.ce.ntu.edu.tw/最新消息/獎學金/",encoding='utf-8')


# In[2]:


doc1=pq(doc)


# In[ ]:


fp = open("pathway.txt", "w")
for i in range(0,5):
    a = str(doc1("#w4pl-inner-519 > ul > li:nth-child("+str(i+1)+")").text())
    b=doc1("#w4pl-inner-519 > ul > li:nth-child("+str(i+1)+")"+" > a ")
    path = b.attr('href')
    #print(a)
    #print(path)
    tk.Label(window, text=str(i+1)+'.  '+a, bg='#eeeeee').pack()
    fp.write(path+'\n')
fp.close()
window.mainloop()   

