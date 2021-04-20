#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


url = 'https://redplanetscience.com/'
browser.visit(url)


# In[4]:


for x in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_='content_title')

titles


# In[5]:


for title in titles:
        news_title = title.text
        break


# In[6]:


news_title


# In[7]:


for y in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    paras = soup.find_all('div', class_='article_teaser_body')

paras


# In[8]:


for para in paras:
        news_p = para.text
        break


# In[9]:


news_p


# In[10]:


browser.quit()


# In[11]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[12]:


url_2 = 'https://spaceimages-mars.com/'
browser.visit(url_2)


# In[13]:


#('img', class_='headerimage fade-in')
for z in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images = soup.find('div', class_='floating_text_area')

image_url = images.find('a')['href']


# In[14]:


featured_image_url = [url_2 + image_url]
featured_image_url


# In[15]:


browser.quit()


# In[16]:


import pandas as pd


# In[17]:


url = 'https://galaxyfacts-mars.com/'


# In[18]:


tables = pd.read_html(url)
tables


# In[19]:


type(tables)


# In[20]:


mars_df = mars_df = tables[0]
mars_df.head(15)


# In[21]:


new_header = mars_df.iloc[0] #grab the first row for the header
mars_df = mars_df[1:] #take the data less the header row
mars_df.columns = new_header #set the header row as the df header
mars_df


# In[22]:


mars_df.set_index(['Mars - Earth Comparison'], inplace=True)
mars_df


# In[ ]:


mars_df.to_html('mars_df.html')


# In[ ]:


mars_df


# In[23]:


#################
# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[24]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[25]:


hemisphere_image_urls = []


# In[26]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    cerberus = soup.find_all('div', class_='collapsible results')
    
    for x in cerberus:
        cerberus__1 = x('a')[0]['href']
        
cerberus__1


# In[27]:


url__2 = 'https://marshemispheres.com/' + cerberus__1
browser.visit(url__2)


# In[28]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    cerberus__1_title = soup.find('h2', class_='title').text

cerberus__1_title


# In[29]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    cerberus__1 = soup.find_all('img', class_='wide-image')
    
    for x in cerberus__1:
        cerberus__1_url = x['src']
        
cerberus__1_url


# In[30]:


cerberus_info = {"title": cerberus__1_title, "img_url": url + cerberus__1_url}
cerberus_info


# In[31]:


hemisphere_image_urls.append(cerberus_info)


# In[32]:


hemisphere_image_urls


# In[33]:


#-----#


# In[34]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[35]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    schiaparelli = soup.find_all('div', class_='collapsible results')
    
    for x in schiaparelli:
        schiaparelli__1 = x('a')[2]['href']
        
schiaparelli__1


# In[36]:


url__3 = 'https://marshemispheres.com/' + schiaparelli__1
browser.visit(url__3)


# In[37]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    schiaparelli__1_title = soup.find('h2', class_='title').text

schiaparelli__1_title


# In[38]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    schiaparelli__1 = soup.find_all('img', class_='wide-image')
    
    for x in schiaparelli__1:
        schiaparelli__1_url = x['src']
        
schiaparelli__1_url


# In[39]:


schiaparelli_info = {"title": schiaparelli__1_title, "img_url": url + schiaparelli__1_url}
schiaparelli_info


# In[40]:


hemisphere_image_urls.append(schiaparelli_info)


# In[41]:


hemisphere_image_urls


# In[42]:


#---#


# In[43]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[44]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    syrtis = soup.find_all('div', class_='collapsible results')
    
    for x in syrtis:
        syrtis__1 = x('a')[4]['href']
        
syrtis__1


# In[45]:


url__4 = 'https://marshemispheres.com/' + syrtis__1
browser.visit(url__4)


# In[46]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    syrtis__1_title = soup.find('h2', class_='title').text

syrtis__1_title


# In[47]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    syrtis__1 = soup.find_all('img', class_='wide-image')
    
    for x in syrtis__1:
        syrtis__1_url = x['src']
        
syrtis__1_url


# In[48]:


syrtis_info = {"title": syrtis__1_title, "img_url": url + syrtis__1_url}
syrtis_info


# In[49]:


hemisphere_image_urls.append(syrtis_info)
hemisphere_image_urls


# In[50]:


#---#


# In[51]:


url = 'https://marshemispheres.com/'
browser.visit(url)


# In[52]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    valles = soup.find_all('div', class_='collapsible results')
    
    for x in valles:
        valles__1 = x('a')[6]['href']
        
valles__1


# In[53]:


url__5 = 'https://marshemispheres.com/' + valles__1
browser.visit(url__5)


# In[54]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    valles__1_title = soup.find('h2', class_='title').text

valles__1_title


# In[55]:


for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    valles__1 = soup.find_all('img', class_='wide-image')
    
    for x in valles__1:
        valles__1_url = x['src']
        
valles__1_url


# In[56]:


valles_info = {"title": valles__1_title, "img_url": url + valles__1_url}
valles_info


# In[57]:


hemisphere_image_urls.append(valles_info)
hemisphere_image_urls


# In[58]:


browser.quit()


# In[ ]:

print (hemisphere_image_urls)


