
# import requests
# from bs4 import BeautifulSoup
# url = 'https://archive.ics.uci.edu/ml/datasets.php'

# # Lets use the requests get method to fetch the data from url

# response = requests.get(url)
# # lets check the status
# status = response.status_code
# print(status) # 200 means the fetching was successful

###############

# import requests
# from bs4 import BeautifulSoup
# url = 'https://archive.ics.uci.edu/ml/datasets.php'

# response = requests.get(url)
# content = response.content # we get all the content from the website
# soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
# print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
# print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
# print(soup.body) # gives the whole page on the website
# print(response.status_code)

# tables = soup.find_all('table', {'cellpadding':'3'})
# # We are targeting the table with cellpadding attribute with the value of 3
# # We can select using id, class or HTML tag , for more information check the beautifulsoup doc
# table = tables[0] # the result is a list, we are taking out data from it
# for td in table.find('tr').find_all('td'):
#     print(td.text)

# with open('./home/faizan/30_days_python/day_22/file_example.txt','a') as f:
# f.write(td.text)




print("ha")

co = 519
z = 0
j = 0
for i in range(co):
    j += i

print(j)