# -------------------------------------
#
# client-side class
#
# group: communication
# class: SendMessage (aka Send)
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

# TODO: check current_message for ; (injection etc)

import wx
import socket
import time
from threading import Timer
from Translation.English import English as Locale
from Modules.dialogs.ErrorDialog import ErrorDialog as Error
from Modules.dialogs.WarningDialog import WarningDialog as Warning
from Class.communication.ReciveMessage import ReciveMessage

class SendMessage:
    def __init__(self):
        SendMessage.reserved = False
        from Class.gui.ChatboxPanel import ChatboxPanel
        from Class.gui.LoginPanel import LoginPanel
        from Handler.button.ConnectHandler import ConnectHandler
        from Class.gui.MainFrame import MainFrame

        current_message = ChatboxPanel.messagebox.GetValue()
        username = LoginPanel.username_textctrl.GetValue()

        username_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, False, u"Ebrima")
        message_font = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL, False, u"Ebrima")

        if current_message != "":
            SendMessage.reserved = True
            username = LoginPanel.username_textctrl.GetValue()
            host = LoginPanel.ip_textctrl.GetValue()
            port = 826

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect_ex((host, port))
                body = b'MES;' + bytes(username, 'utf-8') + b";" + bytes(current_message, 'utf-8')
                try:
                    s.sendall(body)
                    data = s.recv(1024)
                except OSError:
                    Error(Locale.dialog__error__connLost_title, Locale.dialog__error__connLost)
                    ConnectHandler.connected = False
                    MainFrame.show_login(MainFrame)
                    SendMessage.reserved = False
                    return
            if data.decode("utf-8") == "ERR;SPAM":
                ChatboxPanel.messagebox.SetFocus()
                ChatboxPanel.banned = True
                ReciveMessage.redText("Heads up", "You have been banned for 5 seconds because of spam")
                t = Timer(5, SendMessage.unban)
                t.start()
            elif data.decode("utf-8") == "ACK-MES":
                ChatboxPanel.messagebox.SetValue("")
                ChatboxPanel.messagebox.SetHint(Locale.send_message)
                ChatboxPanel.messagebox.SetFocus()
            elif data.decode("utf-8") == "ERR;UNAUTH":
                Warning(Locale.dialog__error__unauth_title, Locale.dialog__error__unauth)
                ChatboxPanel.messagebox.SetFocus()
            else:
                # message was not ack'd by server
                ChatboxPanel.messagebox.SetFocus()
            SendMessage.reserved = False
        else:
            ChatboxPanel.messagebox.SetFocus()
            return
    
    def unban():
        from Class.gui.ChatboxPanel import ChatboxPanel

        ChatboxPanel.banned = False
        return