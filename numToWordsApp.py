import customtkinter as ctk
import tkinter as tk
import numToWords as ntw
from tkcalendar import Calendar


class Cal(tk.Toplevel):
    def __init__(self, parent, date):
        super().__init__(parent)
        self.date = date
        self.cal = Calendar(self, selectmode = 'day', year=2023, month=8, day=27)
        self.cal.pack(expand=True, fill='both')

        self.cal.bind('<<CalendarSelected>>', self.updateLabel)
    
    def updateLabel(self, *args):
        self.date.set(self.cal.get_date())
        self.destroy()

class Layout(ctk.CTkFrame):
    def __init__(self, parent, varValue, varWords, varDate, address, bankRoute, account):
        super().__init__(parent)

        self.rowconfigure((0,1,2,3), weight=1, uniform='a')
        self.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

        self.date = varDate

        txtAddr = ctk.CTkTextbox(self)
        txtAddr.grid(row=0, column=0, columnspan=2, padx=2, pady=5, sticky='ew')
        txtAddr.insert('0.0', address)
        btnDate = ctk.CTkButton(self, text='Date:', command=self.btnDate)
        btnDate.grid(row=0, column=3, sticky='e')
        entryDate = ctk.CTkEntry(self, textvariable=varDate, justify='center', state='disabled')
        entryDate.grid(row=0, column=4, padx=5)

        entryNumToWords = ctk.CTkEntry(self, state='disabled', textvariable=varWords)
        entryNumToWords.grid(row=1, column=0, columnspan=3, sticky='ew')
        lblValue = ctk.CTkLabel(self, text='Amount:')
        lblValue.grid(row=1, column=3, sticky='e')
        entryAmt = ctk.CTkEntry(self, textvariable=varValue)
        entryAmt.grid(row=1, column=4, padx=5)

        lblMemo = ctk.CTkLabel(self, text='Memo:')
        lblMemo.grid(row=2, column=0, sticky='e')
        entryMemo = ctk.CTkEntry(self)
        entryMemo.grid(row=2, column=1, sticky='ew')
        lblSign = ctk.CTkLabel(self, text='Signature:')
        lblSign.grid(row=2, column=2, sticky='e')
        entrySign = ctk.CTkEntry(self)
        entrySign.grid(row=2, column=3, columnspan=2, padx=5, sticky='ew')

        lblBankRoute = ctk.CTkLabel(self, text=bankRoute)
        lblBankRoute.grid(row=3, column=3)
        lblAct = ctk.CTkLabel(self, text=account)
        lblAct.grid(row=3, column=4, sticky='w')

    def btnDate(self):
        cal = Cal(self, self.date)
        

class NumToWordsApp(ctk.CTk):
    def __init__(self, address='', bankRoute='', account=''):
        super().__init__()
        self.title('Checkbook App')
        self._geo(800, 300)

        self.varValue = ctk.StringVar(value='')
        self.varValue.trace('w', self.convertToWords)
        self.varWords = ctk.StringVar(value='')
        self.varDate = ctk.StringVar(value='')

        l = Layout(self, self.varValue, self.varWords, self.varDate, address, bankRoute, account)
        l.pack(fill='both', expand=True)

        self.bind('<Shift-Escape>', quit)
        self.mainloop()
    

    def _geo(self, w, h):
        pWidth = w
        pHeight = h
        sWidth = self.winfo_screenwidth()
        sHeight = self.winfo_screenheight()
        mWidth = sWidth//2 - pWidth//2
        mHeight = sHeight//2 - pHeight//2

        self.minsize(w, h)
        self.geometry(f'{pWidth}x{pHeight}+{mWidth}+{mHeight}')
    
    def convertToWords(self, *args):
        try:
            value = float(self.varValue.get())
            # print(f'value: {value}')
            self.varWords.set(ntw.numToWords(value).numToWords())
        except:
            print(f'ERROR: Invalid Float Value')
            self.varWords.set('')

if __name__ == '__main__':
    addr = f'Chris Olarti\n3265 Preserve Dr\nOrlando, FL 32824'
    bankRoute = f'4596878'
    acct = f'4563289'
    n = NumToWordsApp(addr, bankRoute, acct)

