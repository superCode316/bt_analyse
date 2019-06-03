import re, datetime


# 因为日志中message是唯一一个包含在内的dict对象，所以单独处理
def message(datas):
    data = datas.replace('{', '').replace('}', '').split(',')
    result = {}
    if len(data) < 2:
        return result
    for i in data:
        ii = i.split(':')
        result[ii[0].replace(' ', '')] = ii[1]
    return result


def printProgress(iteration, total, barLength=50):
    import sys
    formatStr = '{0:.1f}'
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '#' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s %s' % ('Progress:', bar, percent, '%', 'Complete')),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def time_parse(time_str):
    return datetime.datetime.strptime(time_str, '%b %d %H:%M:%S.%f')


def time_sub(s, e):
    s_time = time_parse(s)
    e_time = time_parse(e)
    return e_time - s_time


def timedelta_to_int(t):
    return t.seconds*1000000 + t.microseconds


# 处理单条记录
# 输入单条记录的字符串
# 返回处理后的单条记录的dict对象
def single(line):
    w_key = ('level', 'module')
    s_key = ('time', 'msg', 'message', 'peer', 'type')
    s = {}.fromkeys(w_key, s_key)
    string = '%s="([^"]+)'
    word = '%s=([^ ]+)'
    for i in s_key:
        s[i] = re.findall(string % i, line)[0]
    for i in w_key:
        s[i] = re.findall(word % i, line)[0]
    s['message'] = message(s['message'])
    return s


class Log(object):

    def __init__(self):
        self.all = []

    # 向对象中添加记录
    # 输入为文件的路径
    # 没有返回值，但会将文件的处理结果放进对象的all中
    def add_by_filepath(self, paths):
        for path in paths:
            print(path)
            fs = open(path)
            all_data = fs.readlines()
            b = 0
            length = len(all_data)
            printProgress(0, length)
            for i in all_data:
                s = single(i)
                self.all.append(s)
                b += 1
                printProgress(b, length)
            return True

    # 取得所有有关于区块的消息数组
    def get_mines(self):
        data = []
        for i in self.all:
            if 'MineBlockMessage' in i['type']:
                data.append(i)
        return data

    # 取得所有有关于交易的消息数组
    def get_transactions(self):
        data = []
        for i in self.all:
            if 'Transaction' in i['type']:
                data.append(i)
        return data


class File(object):

    def __init__(self, data):
        self.records = {}
        self.add_data(data)

    def add_data(self, data):
        records = {}
        for i in data:
            if i['message'] is {}:
                continue
            if 'height' in i['message'] or 'block_height' in i['message']:
                h = i['message']['block_height'].replace(' ', '')
                if not h in records:
                    records[h] = []
                records[h].append(i)
            elif 'tx_hash' in i['message']:
                h = i['message']['tx_hash'].replace(' ', '')
                if not h in records:
                    records[h] = []
                records[h].append(i)
        self.records = records

    def get_time(self, height):
        records = self.records
        time = []
        for i in records[height]:
            time.append(i['time'])
        times = {}.fromkeys(('all', 'start', 'end', 'gap'))
        times['all'] = time
        times['start'] = time[0]
        times['end'] = time[len(time) - 1]
        times['gap'] = time_sub(time[0], time[len(time) - 1])
        return times

    def get_all_subs(self):
        codes = self.records.keys()
        all_times = {}.fromkeys(codes)
        for i in codes:
            all_times[i] = self.get_time(i)
        subs_dict = {}.fromkeys(all_times.keys())
        subs_arr = []
        for i in all_times:
            s = all_times[i]
            start = s['start']
            end = s['end']
            sub = time_sub(start, end)
            if sub.microseconds + sub.seconds is not 0:
                subs_dict[i] = sub
                subs_arr.append(sub)
        print(self.get_time(list(all_times.keys())[len(list(all_times.keys()))-1]))
        return {'dict': subs_dict, 'arr': subs_arr, 'start&end': []}

    def get_all(self):
        codes = self.records.keys()
        all_times = {}.fromkeys(codes)
        for i in codes:
            all_times[i] = self.get_time(i)
        subs_dict = {}
        for i in all_times:
            s = all_times[i]
            start = s['start']
            end = s['end']
            sub = timedelta_to_int(time_sub(start, end))
            if sub is not 0:
                subs_dict[i] = sub
        return subs_dict

