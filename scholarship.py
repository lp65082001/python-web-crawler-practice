#!/usr/bin/python
# -*- coding: UTF-8 -*-

# In[1]:


from pyquery import PyQuery as pq
import re
import tkinter as tk


window = tk.Tk()
window.title('scholarship')
window.geometry('600x200')

#result = 'http://www.ce.ntu.edu.tw/最新消息/獎學金/'
result = 'http://www.ce.ntu.edu.tw/%E6%9C%80%E6%96%B0%E6%B6%88%E6%81%AF/%E7%8D%8E%E5%AD%B8%E9%87%91/'
doc = pq(url=result,encoding='utf-8')



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

