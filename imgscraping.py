import mechanicalsoup
import os
import wget

browser = mechanicalsoup.StatefulBrowser()
url = "https://www.google.com.eg/imghp?hl=en&ogbl"
browser.open(url)

browser.get_current_page()
browser.select_form()
browser.get_current_form().print_summary()

search_term = "lion"
browser["q"] = search_term
browser.launch_browser()
response = browser.submit_selected()
#print("new url :  ",browser.get_url())
#print("response :  ",response.text[:50])
new_url = browser.get_url()
browser.open(new_url)
page = browser.get_current_page()
all_img = page.find_all("img")
print(all_img)

img_source = []
for img in all_img :
    img = img.get("src")
    img_source.append(img)
img_source = [img for img in img_source if img.startswith("https")]
print(img_source)



path = os.getcwd()

path = os.path.join(path,search_term+"s")
try:
    os.mkdir(path)
except :
    pass

counter = 0
for img in img_source :
    save_as = os.path.join(path, search_term+str(counter)+".jpg")
    wget.download(img,save_as)
    counter += 1