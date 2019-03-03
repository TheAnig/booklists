# Pagination - <shelves, end == total>
# 


import requests as req

dev_key = 'AIxEUzTE6D5n7piTn8wFAQ'

url = 'https://www.goodreads.com/shelf/list.xml'

user_id = '45618'

print(req.get(url+f'?key={dev_key}'+f'&user_id={user_id}'+f'&page={2}').text)