import openpyxl
import openpyxl.styles as sty
import os
import time
import datetime


class Excel:
    def __init__(self, path='', today=''):
        if today == '':
            os.environ['TZ'] = 'Asia/Shanghai'
            time.tzset()
            self.sheet_date = time.strftime('%m.%d')
        else:
            self.sheet_date = today
        self.sheet_yesterday = self.cal_yesterday(self.sheet_date)
        print("Sheet名字: 今天是{0}, 昨天是{1}".format(self.sheet_date, self.sheet_yesterday))

        self.path = path
        f_order = openpyxl.load_workbook(path + '/order.xlsx')
        self.f_order = f_order
        self.sheet_order = f_order[self.sheet_date] if self.sheet_date in f_order.sheetnames \
            else f_order.create_sheet(self.sheet_date)
        f_shipping = openpyxl.load_workbook(path + '/shipping.xlsx')
        self.f_shipping = f_shipping
        self.sheet_shipping = f_shipping[self.sheet_date] if self.sheet_date in f_shipping.sheetnames \
            else f_shipping.create_sheet(self.sheet_date)
        f_product = openpyxl.load_workbook(path + '/product.xlsx')
        self.f_product = f_product
        self.sheet_product = f_product[self.sheet_date] if self.sheet_date in f_product.sheetnames \
            else f_product.create_sheet(self.sheet_date)
        self.sheet_storage = f_product['产品总表']
        f_backup = openpyxl.load_workbook(path + '/backup.xlsx')
        self.f_backup = f_backup
        self.sheet_backup = f_backup[self.sheet_yesterday]
        self.sheet_backup_today = f_backup[self.sheet_date] if self.sheet_date in f_backup.sheetnames \
            else f_backup.create_sheet(self.sheet_date)

    @staticmethod
    def cal_yesterday(today):
        year = int(time.strftime('%Y'))
        month = int(today.split('.')[0])
        day = int(today.split('.')[1])
        previous = datetime.datetime(year, month, day) + datetime.timedelta(days=-1)
        return previous.strftime('%m.%d')

    def cal_today_storage(self):
        self.copy_from_sheet_to_new(self.sheet_backup, self.sheet_storage, self.f_product, '/product.xlsx')
        print("已拉取昨日{0}的备份库存作为今日的计算原数据".format(self.sheet_yesterday))
        table = self.sheet_product
        col_sell, col_id = self.get_col_sell()
        if col_sell == -1 or col_id == -1:
            return {'success': False, 'msg': "Doesn't contain column '售出件数' or '产品编号' in sheet {0}".format(table.title)}
        col_storage = self.get_col_storage()
        if col_storage == -1:
            return {'success': False, 'msg': "Doesn't contain column '库存' in sheet #1"}
        data_storage = [[int(self.sheet_backup.cell(i, 1).value),
                         int(self.sheet_backup.cell(i, col_storage).value) if self.sheet_backup.cell(i, col_storage).value else 0]
                        for i in range(2, self.sheet_backup.max_row + 1)]
        data_sell = list()
        # Prepare selling information: [id starts from 1, sum of sell]
        [data_sell.append([int(table.cell(i, col_id).value) - 1, int(table.cell(i, col_sell).value)]) for i in range(2, table.max_row + 1)]
        # Calculate today's storage
        for entry in data_sell:
            data_storage[entry[0]][1] -= entry[1]
        # Write back to xlsx
        for each in data_storage:
            self.sheet_storage.cell(each[0] + 1, col_storage).value = each[1]
        for row in range(2, self.sheet_storage.max_row + 1):
            for col in range(1, self.sheet_storage.max_column + 1):
                num_storage = self.sheet_storage.cell(row, col_storage).value
                num_storage = 0 if not num_storage else int(num_storage)
                self.sheet_storage.cell(row, col).fill = sty.PatternFill(patternType='solid', fgColor="fa8072") \
                    if num_storage <= 0 else sty.PatternFill(fgColor="ffffff")
        self.f_product.save(self.path + '/product.xlsx')
        print("已更新今日最新库存")
        self.copy_from_sheet_to_new(self.sheet_storage, self.f_backup[self.sheet_date], self.f_backup, '/backup.xlsx')
        print("已备份今日最新库存")
        return {'success': True}

    def cal_today_selling(self):
        table = self.sheet_product
        indices = self.get_indices(table)
        for i in range(2, table.max_row + 1):
            num = int(table.cell(i, indices['售出件数']).value)
            value = float(table.cell(i, indices['单价']).value)
            bonus = float(table.cell(i, indices['优惠']).value)
            total = num * value
            total_cost = num * float(table.cell(i, indices['成本']).value)
            original_profit = total - total_cost
            total_final = total * bonus
            total_profit = total_final - total_cost
            table.cell(i, indices['总金额']).value = total
            table.cell(i, indices['总利润']).value = original_profit
            table.cell(i, indices['折后金额']).value = total_final
            table.cell(i, indices['折后利润']).value = total_profit
        self.f_product.save(self.path + '/product.xlsx')

    def cal_order_group_by_buyer(self):
        table = self.sheet_product
        indices = self.get_indices(table)
        data = dict()
        for i in range(2, table.max_row + 1):
            entry = list()
            for j in range(1, table.max_column + 1):
                entry.append(table.cell(i, j).value)
            id = table.cell(i, indices['微信id']).value
            total = table.cell(i, indices['折后金额']).value
            if id in data:
                data[id]['sum'] += total
                data[id]['entry'].append(entry)
            else:
                data[id] = dict()
                data[id]['sum'] = total
                data[id]['entry'] = [entry]
        i = 2
        for id, value in data.items():
            for each_row in value['entry']:
                for j in range(len(each_row)):
                    table.cell(i, j + 1).value = each_row[j]
                table.cell(i, j + 2).value = value['sum']
                i += 1
        table.cell(1, j + 2).value = '该用户今日总购买金额（若一日多单请老婆大人自行计算~）'
        self.f_product.save(self.path + '/product.xlsx')
        print("已初步整理今日每个微信买家的产品信息及总购买金额。若一日多单请老婆大人自行计算该单需要额外支付多少钱~")

    def get_col_sell(self):
        table = self.sheet_product
        col_sell = -1
        col_id = -1
        for i in range(1, table.max_column + 1):
            if table.cell(1, i).value == '售出件数':
                col_sell = i
            if table.cell(1, i).value == '产品编号':
                col_id = i
        return col_sell, col_id

    def get_col_storage(self):
        table = self.sheet_backup
        col_storage = -1
        for i in range(1, table.max_column + 1):
            if table.cell(1, i).value == '库存':
                col_storage = i
                break
        return col_storage

    def copy_from_sheet_to_new(self, sheet_ori, sheet_des, file, filename):
        for i in range(1, sheet_des.max_row + 1):
            for j in range(1, sheet_des.max_column + 1):
                sheet_des.cell(i, j).value = ''
        for i in range(1, sheet_ori.max_row + 1):
            for j in range(1, sheet_ori.max_column + 1):
                sheet_des.cell(i, j).value = sheet_ori.cell(i, j).value
        file.save(self.path + filename)

    @staticmethod
    def get_indices(table):
        indices = dict()
        for i in range(1, table.max_column + 1):
            indices[table.cell(1, i).value] = i
        return indices


path = '/Users/charlesge/Downloads/AliciaEarings'

e = Excel(path=path)
response = e.cal_today_storage()
if not response['success']:
    print(response['msg'])
e.cal_today_selling()
e.cal_order_group_by_buyer()
