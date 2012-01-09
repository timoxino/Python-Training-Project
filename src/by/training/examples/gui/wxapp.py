#!/usr/bin/python2.7
# Author: Tsimafei Shchytkavets <timoxino@gmail.com>
'''
This module includes simple implementation of wxPython application.
'''

import wx

#frame = wx.Frame(parent=None, id=-1, title='wxApp', style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION, size=(500, 400))
class wxApp(wx.Frame):

    def __init__(self, *args, **kwargs):

        super(wxApp, self).__init__(style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION, *args, **kwargs)
        self.Init()

    def Init(self):

        self.SetMenuBar(self.InitMenu())
        self.InitFrame()

    def InitMenu(self):

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileMenuItem = fileMenu.Append(id=wx.ID_EXIT, text='Quit', help='Quit wxApp')
        self.Bind(event=wx.EVT_MENU, handler=self.OnQuit, source=fileMenuItem)
        menuBar.Append(fileMenu, '&File')
        return menuBar

    def OnQuit(self, e):

        self.Close()

    def InitFrame(self):

        self.SetSize((500, 400))
        self.SetTitle('wxApp')
        #frame.Move((500, 250))
        self.Center()
        self.Show(True)

def main():

    app = wx.App()
    wxApp(None)
    app.MainLoop()

if __name__=='__main__':
    main()