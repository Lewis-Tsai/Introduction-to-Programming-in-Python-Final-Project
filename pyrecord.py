import sys, os, datetime
import tkinter
class Record:
    """Represent a record."""
    def __init__(self, date, category, item, amount):
        self._date = date
        self._category = category
        self._item = item
        self._amount = amount

    date = property(lambda self: self._date)
    category = property(lambda self: self._category)
    item = property(lambda self: self._item)
    amount = property(lambda self: self._amount)

class Records:
    money_init = False
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        # 1. Read from 'records.txt' or prompt for initial amount of money.
        # 2. Initialize the attributes (self._records and self._initial_money)
        #    from the file or user input.
        money = ''
        self._record = []
        try:
            fh = open('records.txt', 'r')
            assert os.path.getsize(fh.name)>0
            print("Welcome back!")
            money = fh.readline()
            if int(money):
                self._money = int(money)
                self._init_money = int(money)
                Records.money_init = True
            else:
                raise ValueError
            for line in fh.readlines():
                line = line.rstrip('\n')
                tmp_record_split = line.split()
                if len(tmp_record_split) != 4:
                    sys.stderr.write(f'{line} is not a valid record and has been skipped\n')
                else:
                    if tmp_record_split[3].isdigit() or tmp_record_split[3].startswith('-') and tmp_record_split[3][1:].isdigit():
                        self._record.append(Record(*tmp_record_split))
                        #money += int(tmp_record_split[2])
                        self._init_money -= int(tmp_record_split[3])
                    else:
                        sys.stderr.write(f'{tmp_record_split[3]} is not a valid amount and has been skipped\n')
            fh.close()
        except:
            self._money = 0
            self._init_money = 0

    def get_value(self, opr):
        if opr == 'money':
            return self._money
        elif opr == 'init_money':
            return self._init_money

    def update_value(self, opr, value):
        if opr == 'money':
            self._money = value
        elif opr == 'init_money':
            self._init_money = value

    def add(self, str_record, categories):
        '''Add a record to Records.'''
        str_record_split = str_record.split()
        if len(str_record_split) == 4:
            if categories.is_category_valid(str_record_split[1]) == False:
                tkinter.messagebox.showwarning('pymoney', 'No such category.')
            else:
                if str_record_split[3].isdigit() or str_record_split[3].startswith('-') and str_record_split[3][1:].isdigit():
                    self._record.append(Record(*str_record_split))
                    self._money += int(str_record_split[3])
                else:
                    tkinter.messagebox.showwarning('pymoney', 'Please enter a valid amount.')
        else:
            tkinter.messagebox.showwarning('pymoney', 'Please enter a valid record.')
 
    def view(self):
        '''View the records.'''
        records_pack = [[]*4 for i in range(len(self._record))]
        for i in range(len(self._record)):
            records_pack[i].append(self._record[i].date)
            records_pack[i].append(self._record[i].category)
            records_pack[i].append(self._record[i].item)
            records_pack[i].append(self._record[i].amount)

        return records_pack

    def delete(self, delete_idx):
        '''Delete a record from the record list.'''
        idx = 0
        for i in range(len(self._record)):
            if idx == int(delete_idx):
                self._money -= int(self._record[i].amount)
                self._record.pop(i)
                return
            idx += 1

    def find(self, target_categories, cmd = 'norm'):
        ''' takes a category name to find and
        the predefined list categories as parameters,
        and returns a non-nested list containing the specified category
        and all the subcategories under it (if any).'''

        result_list = []
        sorted_record = list(filter(lambda x: x.category in target_categories, self._record))
        tmp_money = 0
        for i in range(len(sorted_record)):
            if cmd == 'norm':
                result_list.append(f'{sorted_record[i].date}  {sorted_record[i].category}  {sorted_record[i].item}  {sorted_record[i].amount}')
            tmp_money += int(sorted_record[i].amount)
        if cmd == 'norm':
            return result_list, tmp_money
        #for Pie Chart
        return abs(tmp_money)
 
    def save(self):
        '''Save the records to the file.'''
        with open('records.txt', 'w') as fh:
            fh.write(f'{str(self._money)}\n')
            for i in range(len(self._record)):
                fh.write(f'{self._record[i].date} {self._record[i].category} {self._record[i].item} {self._record[i].amount}\n')