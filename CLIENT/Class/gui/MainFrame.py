# -------------------------------------
#
# client-side class
#
# group: GUI
# class: MainFrame
#
# written and developed by Anton Pernisch & Ernest Haban (on behalf of esec team)
# (c) Anton Pernisch & Ernest Haban (on behalf of esec team) 2021
#
# -------------------------------------

import wx
from Class.gui.LoginPanel import LoginPanel
from Class.gui.ChatboxPanel import ChatboxPanel
from Handler.communication.DisconnectHandler import DisconnectHandler as Disconnect
import time

class MainFrame:
    def __init__(self):
        MainFrame.frame = wx.Frame(parent=None, title="esec chat - v1.0 patch 00010", size=(750, 750), style=wx.DEFAULT_FRAME_STYLE)
        panels_sizer = wx.BoxSizer()
        MainFrame.frame.SetSizer(panels_sizer)
        MainFrame.login_panel = LoginPanel(MainFrame.frame)
        MainFrame.chatbox_panel = ChatboxPanel(MainFrame.frame)

        panels_sizer.Add(MainFrame.login_panel, 1, wx.ALL | wx.EXPAND, 0)
        panels_sizer.Add(MainFrame.chatbox_panel, 1, wx.ALL | wx.EXPAND, 0)
        MainFrame.chatbox_panel.Hide()
        MainFrame.login_panel.Show()
        MainFrame.frame.Centre()
        MainFrame.frame.Show()
        MainFrame.frame.Bind(wx.EVT_CLOSE, Disconnect)

    def show_chatbox(self):
        MainFrame.chatbox_panel.Show()
        MainFrame.login_panel.Hide()
        MainFrame.frame.Layout()

    def show_login(self):
        MainFrame.chatbox_panel.Hide()
        MainFrame.login_panel.Show()
        MainFrame.frame.Layout()