from abc import ABC, abstractmethod
import textwrap
from LoginScreen import tkWindow, data
import requests
import sys
from time import sleep

# --------------
FIRST_TIME = True # !!! Important what happens when user first time launch program ----------
# --------------

class Dwar(object):

    def __init__(self):
        self.connection = False  # Dwar server connection
        self.game_url = 'dwar.ru'

    @staticmethod
    def login_screen():
        tkWindow.mainloop()
        username = data['username']
        password = data['password']
        return (username, password)

    def authentication(self, username, password, dwar_server='w1'):
        """
        Description:
            Authentication to dwar Account
        Arguments:
            username {[string]} -- [Dwar Username]
            password {[string]} -- [Dwar password]
            dwar_server {[string]} -- Which dwar server to run w1-Prime or w2-Minor
        """
        dwar_user = username
        dwar_passwd = password
        full_dwar_url = f"https://{dwar_server}.{self.game_url}"
        try:
            serverTest_request = requests.get(full_dwar_url)
            if serverTest_request.status_code == 200:
                self.connection = True
                print("Ehlo Packet Recived Succesfully")
        except requests.exceptions.ConnectionError:
            print(
                "Cant establish connection to Dwar server, Please Check Internet Connection\n or Restart software")
            sys.exit()
        if self.connection:
            self.driver.get(full_dwar_url)
            usr_tag = self.driver.find_element_by_name("email")
            usr.send_keys(dwar_user)  # User
            passwd_tag = self.driver.find_element_by_name("passwd")
            passwd_tag.send_keys(dwar_passwd)
            sleep(2)
            self.driver.find_element_by_id('form_btn_go').click()
            sleep(10)

    def execute_xmlhttpRequest(self, url, method='POST', _async='true'):
        """Create Ajax Xmlhttprequest, and send.
         initializes a newly-created request,
        Arguments:
            url {[str]} -- [description]
        Keyword Arguments:
            method {str} -- http Method (default: {'POST'})
            _async {str} -- indicating whether or not to perform the operation asynchronously (default: {'true'})
        Retrun:
            type: str
            return Javascrip xmlhttprequest
        """
        ajax_request = f'''
        var i = new XMLHttpRequest(); 
        i.open("{method}", "{url}", {_async});
        i.send();
        '''
        return textwrap.dedent(ajax_request)  # Use texwrap.dedent for indentation purposes

    def respawn(self, payment=True):
        """[summary]
        Keyword Arguments:
            payment {bool} -- Dwarshi aris 2 tipis gacocxleba Fasiani romelic imave Lokaciashi gacocxlebs
            da girs 15 centi an ufaso da gacocxldebi Odelvais-shi, Tu payment=True shesruldebA fasiani gacocxleba,
            xolo tu payment=False mashin ufaso
        """
        if payment:
            # Tu vasrulebt fasian gacocxlebas
            self.execute_xmlhttpRequest(url="https/test.url")

    def parse_xml(self, game_mode, instance):
        """[summary]
        Arguments:
            game_mode {[type]} -- [description]
        Returns:
            type: list
            description: return list contain id-s of bots or farming resources depend on game mode 
        """


class Fight(Dwar):
    pass


class Farm(Dwar):
    pass

    def heal_zanoz(self):
        pass


class OpenSuperHit(Dwar):
    pass


class ServiceCraft(Dwar):
    pass


class PurpleConlegret(object):
    pass