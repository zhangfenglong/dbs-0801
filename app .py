#!/usr/bin/env python
# coding: utf-8

# In[211]:


from flask import Flask, request,render_template 


# In[212]:


import joblib


# In[213]:


app = Flask(__name__)


# In[214]:


@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1 = r1, result2 = r2))
    else:
        return(render_template("index.html", result1 = "WATING", result2 = "WAITING"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




