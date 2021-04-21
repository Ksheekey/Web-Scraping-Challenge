#--------------------------------#
# LATEST NEWS TITLE & PARAGRAPH #
#--------------------------------#

from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://redplanetscience.com/'
browser.visit(url)
for x in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.find_all('div', class_='content_title')

for title in titles:
        news_title = title.text
        break

for y in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    paras = soup.find_all('div', class_='article_teaser_body')

for para in paras:
        news_p = para.text
        break

browser.quit()
print(news_title)
print(news_p)

#------------------------#
# FEATURED SPACE IMAGE #
#------------------------#

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url_2 = 'https://spaceimages-mars.com/'
browser.visit(url_2)

for z in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images = soup.find('div', class_='floating_text_area')

image_url = images.find('a')['href']

featured_image_url = [url_2 + image_url]

browser.quit()
print(featured_image_url)

#------------------------#
# HEMISPEHRE INFO #
#------------------------#

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

hemisphere_image_urls = []

url = 'https://marshemispheres.com/'
browser.visit(url)
for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    cerberus = soup.find_all('div', class_='collapsible results')
    
    for x in cerberus:
        cerberus__1 = x('a')[0]['href']

url__2 = 'https://marshemispheres.com/' + cerberus__1
browser.visit(url__2)
for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    cerberus__1_title = soup.find('h2', class_='title').text

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    cerberus__1 = soup.find_all('img', class_='wide-image')
    
    for x in cerberus__1:
        cerberus__1_url = x['src']

cerberus_info = {"title": cerberus__1_title, "img_url": url + cerberus__1_url}
hemisphere_image_urls.append(cerberus_info)

browser.back()

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    schiaparelli = soup.find_all('div', class_='collapsible results')
    
    for x in schiaparelli:
        schiaparelli__1 = x('a')[2]['href']

url__3 = 'https://marshemispheres.com/' + schiaparelli__1
browser.visit(url__3)

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    schiaparelli__1_title = soup.find('h2', class_='title').text

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    schiaparelli__1 = soup.find_all('img', class_='wide-image')
    
    for x in schiaparelli__1:
        schiaparelli__1_url = x['src']

schiaparelli_info = {"title": schiaparelli__1_title, "img_url": url + schiaparelli__1_url}
hemisphere_image_urls.append(schiaparelli_info)

browser.back()

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    syrtis = soup.find_all('div', class_='collapsible results')
    
    for x in syrtis:
        syrtis__1 = x('a')[4]['href']
        
url__4 = 'https://marshemispheres.com/' + syrtis__1
browser.visit(url__4)

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    syrtis__1_title = soup.find('h2', class_='title').text

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    syrtis__1 = soup.find_all('img', class_='wide-image')
    
    for x in syrtis__1:
        syrtis__1_url = x['src']
        
syrtis_info = {"title": syrtis__1_title, "img_url": url + syrtis__1_url}
hemisphere_image_urls.append(syrtis_info)

browser.back()

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    valles = soup.find_all('div', class_='collapsible results')
    
    for x in valles:
        valles__1 = x('a')[6]['href']
        
url__5 = 'https://marshemispheres.com/' + valles__1
browser.visit(url__5)

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    valles__1_title = soup.find('h2', class_='title').text

for k in range(1):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    valles__1 = soup.find_all('img', class_='wide-image')
    
    for x in valles__1:
        valles__1_url = x['src']
        
valles_info = {"title": valles__1_title, "img_url": url + valles__1_url}
hemisphere_image_urls.append(valles_info)

browser.quit()

print(hemisphere_image_urls)