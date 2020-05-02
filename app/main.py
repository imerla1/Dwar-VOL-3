from abc import ABC, abstractmethod


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
            False if Authentication doesn't finish Succesfully
        """        



class Fight(Dwar):
    def do_somthing(self):
        return 'Hello World'

class Farm(Dwar):
    pass

class OpenSuperHit(Dwar):
    pass

class ServiceCraft(Dwar):
    pass
