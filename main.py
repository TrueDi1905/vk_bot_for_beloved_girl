import datetime
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

token_base = os.environ.get('TOKEN')
token_error = os.environ.get('TOKEN_ERROR')
user_id_base = '325154031'
user_id_error = '336159482'
url = 'https://api.vk.com/method/'


def get_statuses_online():
    response = requests.get(f'{url}users.get?user_ids=id{user_id_base}&'
                            f'fields=online&access_token={token_base}&v=5.131')
    online_status = response.json()['response'][0]['online']
    return online_status


def message(what):
    if what == 'error':
        text = 'Бот сломался('
        user_id = user_id_error
        token = token_error
    else:
        text = os.environ.get('TEXT_ONE')
        user_id = user_id_base
        token = token_base
    requests.get(f'{url}messages.send?user_id={user_id}&'
                 f'random_id=0&message={text}&'
                 f'access_token={token}&v=5.131')


def main():
    while True:
        current_date_time = datetime.datetime.now().time()
        time_start = datetime.time(1, 30, 00)
        time_finish = datetime.time(5, 30, 00)
        if time_start < current_date_time < time_finish:
            try:
                online = get_statuses_online()
                if int(online) == 1:
                    message('good')
                    time.sleep(1380)
                time.sleep(120)
            except:
                message('error')
                time.sleep(300)
        else:
            time.sleep(1200)


if __name__ == '__main__':
    main()
