import requests
import datetime

class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update


token = '5904369130:AAG1c4fxJ7VfoahubnbwZy-Spge-sw7WFtc' #Your bot's token
UtopianSpectraBot = BotHandler(token) #Your bot's name


def main():
    new_offset = 1
    print('Now Launching...')

    while True:
        all_updates=UtopianSpectraBot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == 'Monday':
                    UtopianSpectraBot.send_message(first_chat_id,
                                                  '''
                                                  1. Mathematics (7.00 am - 9.00 am)\n2. Basic of Pysic (9.00 am - 12.00 am)
                                                  ''')
                    new_offset = first_update_id + 1
                if first_chat_text == 'Tuesday':
                    UtopianSpectraBot.send_message(first_chat_id,
                                                  '''
                                                  1. Biology (8.30 am - 10.00 am)\n2. Chemistry ( 01.00 pm - 03.00 pm)
                                                  ''')
                    new_offset = first_update_id + 1
                if first_chat_text == 'Wednesday':
                    UtopianSpectraBot.send_message(first_chat_id,
                                                  '''
                                                  1. Sport (07.00 am - 10.00 am)\n2. English Language (02.00 pm - 04.00 pm)
                                                  ''')
                    new_offset = first_update_id + 1
                if first_chat_text == 'Thursday':
                    UtopianSpectraBot.send_message(first_chat_id,
                                                  '''
                                                  1. Culture (09.00 am - 10.30 am)\n2. Tecnology (01.00 pm - 03.00 pm)
                                                  ''' )
                    new_offset = first_update_id + 1
                if first_chat_text == 'Friday':
                    UtopianSpectraBot.send_message(first_chat_id,
                                                  '''
                                                  1. Dance (07.00 am - 09.30 am)
                                                  ''' )
                    new_offset = first_update_id + 1
                if first_chat_text == 'Saturday':
                    UtopianSpectraBot.send_message(first_chat_id,
                                                  '''
                                                  1. Learning Python ( 10.00am - 12.00 am)
                                                  ''' )
                    new_offset = first_update_id + 1
                if first_chat_text == 'Sunday':
                    UtopianSpectraBot.send_message(first_chat_id,
                                                  '''
                                                  Refreshing. Don't forget to  :)
                                                  ''' )
                    new_offset = first_update_id + 1
            else:
                UtopianSpectraBot.send_message(first_chat_id, 'Hi,This Bot is your schedule. Please type a day name you want to see your schedule ')
                new_offset = first_update_id +1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()