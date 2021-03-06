# -------------------------------------
#
# client-side handler
#
# group: Button
# class: SendMessageBtn
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

from Class.communication.SendMessage import SendMessage
from Modules.dialogs.WarningDialog import WarningDialog as Warning
from Modules.dialogs.ErrorDialog import ErrorDialog as Error
from Translation.English import English as Locale
from Class.communication.ReciveMessage import ReciveMessage

class SendMessageBtn:
    def __init__(self, event):
        from Class.gui.ChatboxPanel import ChatboxPanel
        
        if not SendMessage.reserved and not ChatboxPanel.banned:
            SendMessage()
        elif ChatboxPanel.banned:
            ReciveMessage.redText("SELF", "You can't send messages right now...")
        else:
            Warning(Locale.dialog__error__tooFast_title, Locale.dialog__error__tooFast)