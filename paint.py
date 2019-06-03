import wx
import analyse



class Frame(wx.Frame):

    def __init__(self, parent, title, subs, CallBack):
        self.subs = subs
        super(Frame, self).__init__(parent, title=title, size=(len(list(subs.keys()))*2, 300))
        self.InitUI()
        self.data = {}
        self.dc = None
        self.Bind(wx.EVT_LEFT_DOWN, self.choose)
        self.CallBack = CallBack

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        self.label1 = wx.StaticText(self, wx.ID_ANY, 'Mar 17 00:00:31.772', wx.DefaultPosition, wx.DefaultSize, 0)
        self.label2 = wx.StaticText(self, wx.ID_ANY, 'Mar 17 23:58:29.872', wx.Point(len(list(subs.keys()))*2-150, -1), wx.DefaultSize, 0)
        bSizer6.Add(self.label1, 0, wx.ALL, 5)
        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

    def InitUI(self):
        self.Bind(wx.EVT_PAINT, self.onPaint)
        self.Centre()
        self.Show(True)

    def onPaint(self, e):
        subs = self.subs
        dc = wx.PaintDC(self)
        self.dc = dc
        pen = wx.Pen(wx.Colour(36, 100, 204))
        pen.SetWidth(1)
        dc.SetPen(pen)
        dc.Clear()
        length = len(subs.keys())
        key = list(subs.keys())
        self.data = {}.fromkeys(tuple(range(0, length)))
        for i in range(0, length):
            height = subs[key[i]]
            data = {'id': key[i], 'x1': i, 'y1': 1500, 'x2': i, 'y2': 200 - height / 10000000 * 200}
            dc.DrawLine(i*2, 1500, i*2, 200 - height / 10000000 * 200)
            self.data[i] = data

    def choose(self, evt):
        x = evt.GetLogicalPosition(self.dc)[0]
        if x % 2 == 0:
            x /= 2
        else:
            x = (x + 1) / 2

        self.CallBack(self.data[x])
        dc = self.dc
        pos = self.data[x]
        dc.SetPen(wx.Pen(colour=wx.Colour(0, 0, 0), width=100))
        dc.DrawLine(1,1,10,10)


ex = wx.App()
ex.MainLoop()
