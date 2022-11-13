#!/usr/bin/env python
# coding: utf-8

# # 7PAM2000 Applied Data Science 1 Assignment 1: Visualisation

# In[508]:


#header files to access the dataframe and graphs.
import pandas as pan
import matplotlib.pyplot as mat


# In[509]:


#Store the dataset into the data_f that is alias of the dataFrame. 
data_f = pan.read_csv("API_SE.PRM.CMPT.FE.ZS_DS2_en_csv_v2_4682189.csv")
data_f


# In[510]:


data_f = data_f.drop(columns = ["1960","1961","1962","1963","1964",'1965',"1966","1967","1968",'1969',"1970",'1971',"1972","1973","1974","1975","1976","1977","1978","1979","1980","1981","1982","1983","1984","1985","1986","1987","1988","1989","1990","1991","1992","1993",'1994',"1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"])


# In[511]:


data_f


# In[512]:


data_f.isnull().sum()


# In[513]:


dafr=data_f.fillna(0)


# In[514]:


dafr.isnull().sum()


# In[ ]:





# In[515]:


dafr


# In[516]:


dafr.columns


# In[517]:


dafr1 = dafr.head(40)


# In[518]:


'''Line Graph was used to plot line chart using matplotlib library. xlabels defind the x-axis value.ylabels defined 
the y-axis. Rotation function use for graph the y-ticks and x-ticks'''
def linegraph():
    dafr1.plot(x= "Country Name", y=['2019','2020','2021'],figsize = (15,5))
    mat.suptitle("Primary completion rate, female (% of relevant age group)")
    mat.xlabel("Country Name")    #xlabels asign the value year
    mat.ylabel("2019 , 2020 , 2021")   #ylabels asign the value Sales
    mat.xticks(rotation=90) 
    mat.yticks(rotation=90)
    mat.legend()


# In[519]:


linegraph()


# In[547]:


dafr1.columns


# In[548]:


'''Pie Graph used to plot the year based on the country name, here i use the figsize to shape the graph and also use the
suptitle to write the title of the graph. label was used to labeling the x-axis and y-axis.legend use to defind the main 
part of the graph and also decide the place of legend name in the corner for using loc attribute.'''

def pieGraph():
    #ploting the bar graph
    dafr1.plot(x="Country Name", y= "2020", kind='pie',figsize = (15,5) ) 
    #title of the graph
    mat.suptitle("Primary completion rate, female (% of relevant age group)") 
    #xlabels asign the value year
    mat.xlabel("Country")
    #ylabels asign the value Sales
    mat.ylabel("Year") 
    #rotate the asix label using xticks
    mat.xticks(rotation=90)
    #rotate the axis label using yticks
    mat.yticks(rotation=90)     
    mat.legend(["2020"],loc = 1) 


# In[549]:


pieGraph()


# In[553]:


'''Kde graph used to plot the graph using matplotlib library.'''

def kdeGraph():
    #ploting the kde graph with years
    axes = dafr1.plot( y= ['2018','2019', '2020', '2021'],kind='kde',figsize =(15,7))    
    #the graph title using suptitle
    mat.suptitle("Primary completion rate, female (% of relevant age group)")              
    #xlabels asign the value year
    mat.xlabel("Year") 
    #ylabels asign the value 2019
    mat.ylabel("2018,2019, 2020, 2021")  
    #rotate the x-asix label using function-xticks
    mat.xticks(rotation=90)
    #rotate the y-axix label using function-yticks
    mat.yticks(rotation=90)    
    mat.legend(loc = 1)  


# In[554]:


kdeGraph()


# In[ ]:





# In[ ]:




