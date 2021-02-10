# while True:
#     print('Nyora makore ako: ')
#     makore = input()
#     try:
#         makore = int(makore)
#     except:
#         print('Nyora nhamba kwete zvaukunyora zvekupenga izvo.')
#         continue
#     if makore < 1:
#         print('Ndapota nyora number iripamusoro peimwechete.')
#         continue
#     elif makore > 100:
#         print("Kwanai ")
#         continue
#     break
# print(f'Unemakore {makore}.')


# import requests
# res = requests.get("https://google.com/files/")
# type(res)
# res.status_code == requests.codes.ok
# len(res.text)
# print(res.text[:600])

# from selenium import webdriver
# browser = webdriver.Firefox()
# type(browser)
# browser.get("https://inventwithpython.com")
# try:
#     elem = browser.find_element_by_class_name("cover-thumb")
#     print("Found <%s> element with that class name! " % (elem.tag_name))
# except:
#     print("Was not able to find an element with that name.")
# linkElem = browser.find_element_by_link_text("Read Online for Free")
# type(linkElem)
# linkElem.click()
# linkElem = browser.find_element_by_link_text("Buy on Amazon")
# type(linkElem)
# linkElem.click()

from selenium import webdriver
browser = webdriver.Firefox()
type(browser)
browser.get("https://www.whatsapp.com")

Elem = browser.find_element_by_link_text("DOWNLOAD")
type(Elem)
Elem.click()


Elem = browser.find_element_by_link_text("Android")
type(Elem)
Elem.click()

Elem = browser.find_element_by_link_text("DOWNLOAD NOW")
type(Elem)
Elem.click()
#browser.back()
#browser.forward()









































