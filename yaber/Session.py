import yaber.Worker
import protocol.Account
import protocol.Message
import protocol.Session
from protocol.Action import Action

class Session(protocol.Session):
    '''a specialization of protocol.Session'''

    def __init__(self, id_=None, account=None):
        '''constructor'''
        protocol.Session.__init__(self, id_, account)

    def login(self, account, password, status):
        '''start the login process'''
        self.account = protocol.Account(account, password, status)
        worker = yaber.Worker('emesene2', self)
        worker.start()

        self.add_action(Action.ACTION_LOGIN, (account, password, status))

    def send_message(self, cid, text, style=None):
        '''send a common message'''
        account = self.account.account
        message = protocol.Message(protocol.Message.TYPE_MESSAGE, text, account,
            style)
        self.add_action(Action.ACTION_SEND_MESSAGE, (cid, message))
