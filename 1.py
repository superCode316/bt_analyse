import window
import wx
import analyse
import os
import paint


def time_ave(time_arr):
    if len(time_arr) is not 0:
        t_sum = time_arr[0]
        for i in range(1, len(time_arr)):
            t_sum += time_arr[i]
        return t_sum / len(time_arr)
    return None


class Frame(window.MyFrame1):
    def __init__(self, parent):
        window.MyFrame1.__init__(self, parent)
        self.m_textCtrl11.Hide()
        self.m_textCtrl12.Hide()
        self.m_textCtrl13.Hide()
        self.ready = False
        self.mine = None
        self.mines = None
        self.max_mine = None
        self.mid_mine = None
        self.min_mine = None
        self.max_t = None
        self.mid_t = None
        self.min_t = None
        self.transaction = None
        self.transactions = None
        self.dc = None
        self.log = analyse.Log()
        self.type = 0
        # self.Bind(wx.EVT_PAINT, self.onPaint)
        self.data = {}

    def onPaint(self, e):
        if self.type:
            subs = self.transaction.get_all()
        else:
            subs = self.mine.get_all()
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(wx.Colour(0, 0, 0)))
        self.dc = dc
        length = len(subs.keys())
        key = list(subs.keys())
        self.data = {}.fromkeys(tuple(range(0, length)))
        for i in range(0, length):
            height = subs[key[i]]
            data = {'key': key[i], 'x1': i, 'y1': 1500, 'x2': i, 'y2': 200 - height / 10000000 * 200}
            dc.DrawLine(i + 200, 1500, i + 200, 200 - height / 10000000 * 200)
            self.data[i] = data

    def f(self, event):
        return
        # if self.type:
        #     # _hash = self.m_listBox3.GetItemText(self.m_listBox3.GetFirstSelected())
        #     # _time = self.m_listBox3.GetItemText(self.m_listBox3.GetFirstSelected(), 1)
        #     # peer = self.m_listBox3.GetItemText(self.m_listBox3.GetFirstSelected(), 2)
        #     time = self.transaction.get_time(self.m_listBox4.GetSelection())
        #     self.set_text(time, _hash)
        # else:
        #     # height = self.m_listBox3.GetItemText(self.m_listBox3.GetFirstSelected())
        #     # _time = self.m_listBox3.GetItemText(self.m_listBox3.GetFirstSelected(), 1)
        #     # peer = self.m_listBox3.GetItemText(self.m_listBox3.GetFirstSelected(), 2)
        #     time = self.mine.get_time(height)
        #     self.set_text(time, height)

    def list_click(self, event, **__id):
        self.m_listBox3.DeleteAllItems()
        if len(__id.keys()) is 0:
            _id = self.m_listBox4.GetString(self.m_listBox4.GetSelection())
        else:
            _id = __id['__id']

        if self.type:
            time = self.transaction.get_time(_id)
            type = ['交易', 'hash值']
        else:
            time = self.mine.get_time(_id)
            type = ['区块', '高度']
        if not timedelta_to_int(time['gap']) == 0:
            self.set_text(time['gap'], type)
        else:
            self.text3.SetLabel('该交易只收到一条消息')
        self.listctrl_set(_id)

    def add(self, event):
        dlg = wx.DirDialog(self, u'选择文件夹')
        filenames = []
        filepaths = []
        if dlg.ShowModal() == wx.ID_OK:
            for root, dirs, files in os.walk(dlg.GetPath()):
                for file in files:
                    if '.log' in str(file):
                        filepaths.append(os.path.join(root, file))
                        filenames.append(file)
        if len(filenames) is 0:
            return self.show_info('没有文件')
        self.ready = True
        self.infoBar.ShowMessage('加载中', wx.ICON_INFORMATION)
        self.log.add_by_filepath(filepaths)
        filepath_str = '、'.join(filenames)
        self.m_staticText26.SetLabel(filepath_str)
        self.mine = analyse.File(self.log.get_mines())
        self.transaction = analyse.File(self.log.get_transactions())
        self.transactions = self.transaction.records
        self.mines = self.mine.records
        self.max_time()
        self.set_list()
        self.set_sum()
        self.infoBar.Dismiss()

    def max_time(self):
        mine_gaps = self.mine.get_all_subs()
        mine_gap_arr = mine_gaps['arr']
        mine_max_gap = max(mine_gap_arr)
        mine_min_gap = min(mine_gap_arr)
        mine_mid_gap = sorted(mine_gap_arr)[len(mine_gap_arr)//2]
        for i in mine_gaps['dict']:
            if mine_gaps['dict'][i] == mine_max_gap:
                self.max_mine = i
            if mine_gaps['dict'][i] == mine_mid_gap:
                self.mid_mine = i
            if mine_gaps['dict'][i] == mine_min_gap:
                self.min_mine = i
        t_gaps = self.transaction.get_all_subs()
        t_gap_arr = t_gaps['arr']
        t_max_gap = max(t_gap_arr)
        t_min_gap = min(t_gap_arr)
        t_mid_gap = sorted(t_gap_arr)[len(t_gap_arr) // 2]
        for i in t_gaps['dict']:
            if t_gaps['dict'][i] == t_max_gap:
                self.max_t = i
            if t_gaps['dict'][i] == t_mid_gap:
                self.mid_t = i
            if t_gaps['dict'][i] == t_min_gap:
                self.min_t = i

    def set_list(self):
        # wx.EVT_PAINT()
        l = self.m_listBox4
        if self.type:
            l.Set(list(self.transaction.records.keys()))
            paint.Frame(self, '', self.transaction.get_all(), self.CallBack)
        else:
            l.Set(list(self.mine.records.keys()))
            paint.Frame(self, '', self.mine.get_all(), self.CallBack)

    def CallBack(self, value):
        self.list_click(None, __id=value['id'])
        print(value)

    def set_sum(self):
        if self.type:
            self.text14.SetLabel('平均时间间隔为' + str(time_ave(self.transaction.get_all_subs()['arr'])))
            self.text11.SetLabel('最大时间间隔为' + str(self.transaction.get_all_subs()['dict'][self.max_t]))
            self.m_textCtrl11.Show()
            self.m_textCtrl11.SetLabel(self.max_t)
            self.text12.SetLabel('时间的中间值为' + str(self.transaction.get_all_subs()['dict'][self.mid_t]))
            self.m_textCtrl12.Show()
            self.m_textCtrl12.SetLabel(self.mid_t)
            self.text13.SetLabel('最短时间间隔为' + str(self.transaction.get_all_subs()['dict'][self.min_t]))
            self.m_textCtrl13.Show()
            self.m_textCtrl13.SetLabel(self.min_t)
        else:
            self.text14.SetLabel('平均时间间隔为' + str(time_ave(self.mine.get_all_subs()['arr'])))
            self.text11.SetLabel('最大时间间隔为' + str(self.mine.get_all_subs()['dict'][self.max_mine]))
            self.m_textCtrl11.Show()
            self.m_textCtrl11.SetLabel(self.max_mine)
            self.text12.SetLabel('时间的中间值为' + str(self.mine.get_all_subs()['dict'][self.mid_mine]))
            self.m_textCtrl12.Show()
            self.m_textCtrl12.SetLabel(self.mid_mine)
            self.text13.SetLabel('最短时间间隔为' + str(self.mine.get_all_subs()['dict'][self.min_mine]))
            self.m_textCtrl13.Show()
            self.m_textCtrl13.SetLabel(self.min_mine)
            
    def listctrl_set(self, _id):
        l = self.m_listBox3
        if self.type:
            # l.Set(self.transaction_list)
            for i in self.transactions[_id]:
                index = l.InsertItem(0, _id)
                l.SetItem(index, 1, i['time'])
                l.SetItem(index, 2, i['peer'])
        else:
            # l.Set(self.mine_list)
            for i in self.mines[_id]:
                index = l.InsertItem(0, _id)
                l.SetItem(index, 1, i['time'])
                l.SetItem(index, 2, i['peer'])

    def set_text(self, st, type):
        # et, lt, st = time['start'], time['end'], time['gap']
        # self.text0.SetLabel('该%s所在%s是%s，来自于%s' % (type[0], type[1], id, peer))
        # self.text1.SetLabel('该%s最早收到时间：%s' % (type[0], et))
        # self.text2.SetLabel('该%s最晚收到时间：%s' % (type[0], lt))
        self.text3.SetLabel('该%s完成交易时间：%s' % (type[0], st))

    def clear_text(self):
        self.text0.SetLabel('')
        self.text1.SetLabel('')
        self.text2.SetLabel('')
        self.text3.SetLabel('')

    def refresh_list(self, *l):
        # list_box = self.m_listBox3
        self.type = self.rb.GetSelection()
        # if self.type:
        #     if l:
        #         # list_box.Set(l)
        #     else:
        #         # list_box.Set(self.transaction_list)
        # else:
        #     # if l:
        #         list_box.Set(l)
        #     else:
        #         list_box.Set(self.mine_list)

    def show_info(self, message):
        self.infoBar.Hide()
        self.infoBar.ShowMessage(message)

    def change_type(self, event):
        self.type = not self.type
        self.clear_text()
        self.set_list()
        # self.m_listBox3.DeleteAllItems()
        self.set_sum()


def main():
    app = wx.App(False)
    frame = Frame(None)
    frame.Show(True)
    # start the applications
    app.MainLoop()


def timedelta_to_int(timedelta):
    microseconds = timedelta.microseconds
    seconds = timedelta.seconds
    return seconds+microseconds


if __name__ == '__main__':
    main()
