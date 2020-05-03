from abc import ABC, abstractmethod
import textwrap

class Dwar(object):
    
    def __init__(self):
        pass
    
    def authentication(self, username, password):
        """
        Description:
            Authentication to dwar Account

        Arguments:
            username {[string]} -- [Dwar Username]
            password {[string]} -- [Dwar password]

        Returns:
            [type] -- [boolean]
            True if Authentiaction finish Succesfully 
            False if Authentication Failed
        """
                
    def execute_xmlhttpRequest(self, url, method='POST', _async='true'):
        """Create Ajax Xmlhttprequest, and send.
         initializes a newly-created request,

        Arguments:
            url {[str]} -- [description]

        Keyword Arguments:
            method {str} -- http Method (default: {'POST'})
            method {str} -- indicating whether or not to perform the operation asynchronously (default: {'true'})

        Retrun:
            type: str
            return Javascrip xmlhttprequest
        """        
        ajax_request = f'''
        var i = new XMLHttpRequest(); 
        i.open("{method}", "{url}", {_async});
        i.send();
        '''
        return textwrap.dedent(ajax_request) # Use texwrap.dedent for indentation purposes
    
    def respawn(self, payment=True):
        """[summary]

        Keyword Arguments:
            payment {bool} -- Dwarshi aris 2 tipis gacocxleba Fasiani romelic imave Lokaciashi gacocxlebs
            da girs 15 centi an ufaso da gacocxldebi Odelvais-shi, Tu payment=True shesruldebA fasiani gacocxleba,
            xolo tu payment=False mashin ufaso
              
        """ 
        pass       

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

class OpenSuperHit(Dwar):
    pass

class ServiceCraft(Dwar):
    pass
