from bs4 import BeautifulSoup

# HTML content
html = '''
<div class="example-class">Element 1</div>
<div class="example-class">Element 2</div>
<div class="other-class">Element 3</div>
'''

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find elements with a specific class
elements_with_class = soup.select('.example-class')

# Iterate through the found elements
for element in elements_with_class:
    print(element)



# 👇 HTML Source
html_source = '''
<p class="p">Hello Python</p>
<p class="p" id="bs">Hello BeautifulSoup</p>
'''
soup = BeautifulSoup(html_source, 'html.parser') # 👉️ Parsing

p = soup.find(id="bs", class_="p") # 👉️ Find By ID and Class -- This method also works with the find_all() function.
print(p) # 👉️ Print Result

p = soup.find(attrs={"id":"bs", "class":"p"}) # 👉️ Find By ID and Class -- This method also works with the find_all() function.
print(p) # 👉️ Print Result

p = soup.select_one("#bs.p") # 👉️ Select By ID and Class -- This method also works with the select() function.
print(p) # 👉️ Print Result


