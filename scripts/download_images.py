# Needed modules
import os, pickle, requests, bs4
from selenium import webdriver

# Setting the needed values for the operations below
base_dir = 'C:\\base'
image_dir = 'C:\\images'
html_file = 'images.txt'                    # File that contains the HTML structure of the website
static_dir = ''                             # Site to make requests to
css_selector = '.o_attachment_download'     # Selector for beautifulsoup4
cookies_file = 'cookies.pkl'
image_source = 'href'                       # Images sometimes are under src, href, etc.
counter = 0

# Calling the browser with the static URL
driver = webdriver.Chrome()
driver.get(static_dir + '/web/login')

# Adding the cookies in the cookies.pkl file to this current session
for cookie in pickle.load(open(os.path.join(image_dir,cookies_file), "rb")):
    if 'expiry' in cookie:
        del cookie['expiry']
    driver.add_cookie(cookie)

# Refreshing the browser so the loaded cookies are reflected
driver.refresh()
# Creating a session with the requests module
res = requests.Session()
# Loading the selenium webdriver cookies to the requests module
res.cookies.update( {c['name']:c['value'] for c in driver.get_cookies()} )
# Closing the browser
driver.quit()

# Opening the HTML file with the special encoding 
with open(os.path.join(base_dir,html_file),encoding="utf8") as img_text:
    data_web = ''.join(img_text.readlines()) # Joining all the lines into one
    content = bs4.BeautifulSoup(data_web, "html.parser") # Parsing the data into HTML
    images = content.select(css_selector) # Selecting the classes that contains the images
    total_images = len(images) # Total images
    # Looping over the selected classes
    for image in images:
        img_to_download = str(static_dir + image.get(image_source)).replace('?download=true','') # Getting the image URL
        image_req = res.get(img_to_download) # Requesting the image
        if image_req.status_code == 200:
            counter += 1 # Counter for all the images
            downloaded_image = os.path.join(image_dir,'Image #%s.jpg' %(counter)) # Setting the filename of the image
            # Saving the image to disk
            with open(downloaded_image,'wb') as down_img:
                for chunk in image_req.iter_content(100000):
                    down_img.write(chunk)
            # Log
            print('Image %s of %s downloaded.' %(counter, total_images))