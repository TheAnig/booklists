# Shelf ID = shelf name + user id

import requests as req

dev_key = 'AIxEUzTE6D5n7piTn8wFAQ'

user_id = '45618'

shelf_id = 'books-about-greg-s-mom'

url = f'https://www.goodreads.com/review/list/{user_id}.xml?key={dev_key}&v=2'

print(req.get(url+f'&shelf={shelf_id}').text)