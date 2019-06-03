# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version May  6 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sys
###########################################################################
## Class MyFrame1
###########################################################################

packages = [('jessica alba', 'pomona', '1981'), ('sigourney weaver', 'new york', '1949'),
            ('angelina jolie', 'los angeles', '1975'), ('natalie portman', 'jerusalem', '1981'),
            ('rachel weiss', 'london', '1971'), ('scarlett johansson', 'new york', '1984')]


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1100, 550), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        box = wx.BoxSizer(wx.VERTICAL)

        self.infoBar = wx.InfoBar(self)
        box.Add(self.infoBar,wx.SizerFlags().Expand())

        box1 = wx.BoxSizer(wx.HORIZONTAL)

        box1.SetMinSize(wx.Size(100, 30))
        self.m_staticText26 = wx.StaticText(self, wx.ID_ANY, u"选择文件…", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)

        self.m_staticText26.SetMinSize(wx.Size(600, -1))
        self.m_staticText26.SetMaxSize(wx.Size(600, -1))

        box1.Add(self.m_staticText26, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_BUTTON, self.add, self.m_button3)

        box.Add(box1, 1, 0, 5)
        box.Add(self.m_button3, 0, wx.ALL, 5)

        self.rb = wx.RadioBox(self, choices=['区块', '交易'])
        box.Add(self.rb)
        self.Bind(wx.EVT_RADIOBOX, self.change_type, self.rb)
        
        box2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_listBox4 = wx.ListBox(self, -1, size=wx.Size(200, 350))
        box2.Add(self.m_listBox4, 0, wx.ALL, 5)
        # self.Bind(wx.EVT_LISTBOX, self.list_click, self.m_listBox4)

        self.m_listBox3 = wx.ListCtrl(self, -1, size=wx.Size(450, 350), style=wx.LC_REPORT)
        self.m_listBox3.InsertColumn(0, 'id', width=100)
        self.m_listBox3.InsertColumn(1, '收到消息时间', width=200)
        self.m_listBox3.InsertColumn(3, 'peer', wx.LIST_FORMAT_LEFT, width=150)
        box2.Add(self.m_listBox3, 0, wx.ALL, 5)
        # self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.f, self.m_listBox3)

        box21 = wx.BoxSizer(wx.VERTICAL)

        self.text0 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text0.Wrap(-1)

        box21.Add(self.text0, 0, wx.ALL, 5)

        self.text1 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text1.Wrap(-1)

        box21.Add(self.text1, 0, wx.ALL, 5)

        self.text2 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text2.Wrap(-1)

        box21.Add(self.text2, 0, wx.ALL, 5)

        self.text3 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text3.Wrap(-1)

        box21.Add(self.text3, 0, wx.ALL, 5)

        self.text11 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text11.Wrap(-1)

        box21.Add(self.text11, 0, wx.ALL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.TE_READONLY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0)
        box21.Add(self.m_textCtrl11, 0, wx.ALL, 5)

        self.text12 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text12.Wrap(-1)

        box21.Add(self.text12, 0, wx.ALL, 5)

        self.m_textCtrl12 = wx.TextCtrl(self, wx.TE_READONLY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), )
        box21.Add(self.m_textCtrl12, 0, wx.ALL, 5)

        self.text13 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text13.Wrap(-1)

        box21.Add(self.text13, 0, wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(self, wx.TE_READONLY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0)
        box21.Add(self.m_textCtrl13, 0, wx.ALL, 5)

        self.text14 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text14.Wrap(-1)

        box21.Add(self.text14, 0, wx.ALL, 5)

        self.text5 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.text5.Wrap(-1)

        box21.Add(self.text5, 0, wx.ALL, 5)

        box2.Add(box21, 1, wx.EXPAND, 5)

        box.Add(box2, 1, wx.EXPAND, 5)
        #
        # box3 = wx.BoxSizer(wx.HORIZONTAL)
        #
        # self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(300, -1), 0)
        # box3.Add(self.m_textCtrl3, 0, wx.ALL, 5)
        #
        # self.m_button4 = wx.Button(self, wx.ID_ANY, u"搜索", wx.DefaultPosition, wx.DefaultSize, 0)
        # box3.Add(self.m_button4, 0, wx.ALL, 5)
        # self.Bind(wx.EVT_BUTTON, self.search, self.m_button4)
        # box.Add(box3, 1, wx.EXPAND, 5)

        self.SetSizer(box)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def f(self, event):
        pass

    def add(self, event):
        pass

    def change_type(self, event):
        pass

    def list_click(self, event):
        pass
