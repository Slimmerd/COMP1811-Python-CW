from tkinter import*
from tkinter import ttk, messagebox
import random
import time



#F3 i Shopping Basket

def createListinListBox(shopping):
    for elem in shopping:
        theList.insert(END,elem[0] + "-" + str(elem[1]))

def listIndex(shopping, item):
    index = -1
    for i in range(len(shopping)):
        if shopping[i][0] == item:
            index = i
    return index

def addList(shopping, item, index):
    if index == -1:
        shopping.append([item,1])
    else:
        shopping[index][1] += quantity.get()

def removeList(sopping, index):
    del(shopping[index])

def add():
    index = listIndex(shopping, item.get())
    addList(shopping, item.get(), index)
    if index >=0:
        theList.delete(index)
        theList.insert(index,shopping[index][0] + "-" + str(shopping[index][1]))
    else:
        theList.insert(END,item.get() + "-" + str(quantity.get()))

def remove():
    index = theList.index(ACTIVE)
    print(index)
    removeList(shopping, index)
    theList.delete(index)

shopping = [["Lego Set" ,2],["Barbie Doll", 2], ["Marvel Costume", 1], ["Stuffed Toy", 2]]

window = Tk()
window.title("Shopping Basket")

theList = Listbox(window, selectmode=SINGLE)
theList.grid(row=0,column=0,columnspan=2,sticky=E)

createListinListBox(shopping)

item=StringVar()
quantity=IntVar()

quantity.set(1)

Label(window, text="Item:").grid(row=1, column=0, sticky=E)
Entry(window, textvariable=item).grid(row=1, column=1, sticky=W)

Label(window, text="Quantity:").grid(row=2, column=0, sticky=E)
Entry(window, textvariable=quantity).grid(row=2, column=1, sticky=W)

Button(window, text="Add", command=add).grid(row=3, column=0, columnspan=3)
Button(window, text="Remove", command=remove).grid(row=0, column=3)



root = Tk()
root.geometry("1350x650+0+0")
root.title("Online Ordering System")
root.configure(background='black')

def Exit():
    qExit = messagebox.askyesno("Ordering System", "Do you want to exit")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    CustomerRef.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")

def OrderRef():
    Refpay = random.randint(10300, 709467)
    Refpaid = ("CR" + str(Refpay))
    CustomerRef.set(Refpaid)

def CostofOrder():
    Qty1=float(QtyLegoSet.get())
    Qty2=float(QtyBarbieDoll.get())
    Qty3=float(QtyMarvelCostume.get())
    Qty4=float(QtyStuffedToy.get())

    UnitPrice1 = float(UnitPriceLegoSet.get())
    UnitPrice2 = float(UnitPriceBarbieDoll.get())
    UnitPrice3 = float(UnitPriceMarvelCostume.get())
    UnitPrice4 = float(UnitPriceStuffedToy.get())

    CostofToy1 = "£", str('%.2f'%(Qty1 * UnitPrice1))
    CostofToy2 = "£", str('%.2f'%(Qty2 * UnitPrice2))
    CostofToy3 = "£", str('%.2f'%(Qty3 * UnitPrice3))
    CostofToy4 = "£", str('%.2f'%(Qty4 * UnitPrice4))

    CostofLegoSet.set(CostofToy1)
    CostofBarbieDoll.set(CostofToy2)
    CostofMarvelCostume.set(CostofToy3)
    CostofStuffedToy.set(CostofToy4)

    CostToy1 = (Qty1 * UnitPrice1)
    CostToy2 = (Qty2 * UnitPrice2)
    CostToy3 = (Qty3 * UnitPrice3)
    CostToy4 = (Qty4 * UnitPrice4)

    AllCost = ( (Qty1 * UnitPrice1) + (Qty2 * UnitPrice2) + (Qty3 * UnitPrice3) +(Qty4 * UnitPrice4))
    TaxAll ="£", str('%.2f'%((AllCost) * 0.02))
    Tax.set(TaxAll)
    SubTotalp ="£", str('%.2f'%(AllCost))
    SubTotal.set(SubTotalp)
    TotalCostp ="£", str('%.2f'%(AllCost + ((AllCost) * 0.02)))
    TotalCost.set(TotalCostp)
    return

#================================= Variables ========================================
CustomerRef=StringVar()
Tax =StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofLegoSet=StringVar()
CostofBarbieDoll=StringVar()
CostofMarvelCostume=StringVar()
CostofStuffedToy=StringVar()
CostofDelivery=StringVar()
CustomerName=StringVar()
CustomerPhone=StringVar()
CustomerEmail=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
Discount=StringVar()
UnitPriceLegoSet=StringVar()
UnitPriceBarbieDoll=StringVar()
UnitPriceMarvelCostume=StringVar()
UnitPriceStuffedToy=StringVar()
QtyLegoSet=StringVar()
QtyBarbieDoll=StringVar()
QtyMarvelCostume=StringVar()
QtyStuffedToy=StringVar()

#=============================== Init component ====================================
CostofLegoSet.set(0)
CostofBarbieDoll.set(0)
CostofMarvelCostume.set(0)
CostofStuffedToy.set(0)
CostofDelivery.set(0)
UnitPriceLegoSet.set(0)
UnitPriceBarbieDoll.set(0)
UnitPriceMarvelCostume.set(0)
UnitPriceStuffedToy.set(0)
QtyLegoSet.set(0)
QtyBarbieDoll.set(0)
QtyMarvelCostume.set(0)
QtyStuffedToy.set(0)
Discount.set(0)
TimeOfOrder.set(time.strftime("%H:%M:%S")) # Time
DateOfOrder.set(time.strftime("%d/%m/%Y")) # Date
#================================== Frame ==========================================

Tops=Frame(root, width=1350, height=50,bd=16, relief="raise")
Tops.pack(side=TOP)
LF=Frame(root, width=700, height=650,bd=16, relief="raise")
LF.pack(side=LEFT)
RF=Frame(root, width=600, height=650,bd=16, relief="raise")
RF.pack(side=RIGHT)

Tops.configure(background='black')
LF.configure(background='black')
RF.configure(background='black')

LeftInsideLF=Frame(LF, width=700, height=100,bd=8, relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=700, height=400,bd=8, relief="raise")
LeftInsideLFLF.pack(side=LEFT)

RightInsideLF=Frame(RF, width=604, height=200,bd=8, relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=306, height=400,bd=8, relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF, width=300, height=400,bd=8, relief="raise")
RightInsideRFRF.pack(side=RIGHT)
#======================================== ProjectTitle =============================================
lblInfo = Label(Tops, font=('arial',50, 'bold'),text=" Online Ordering Systems",
                bd=10, anchor='w')
lblInfo.grid(row=0,column=0)
######################################### Top Left Frame ###############################################################

lblCustomerName = Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Name",
                       fg="black", bd=10, anchor="w")
lblCustomerName.grid(row=0,column=0)
txtCustomerName=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=43,
                     bg="white", justify='left', textvariable=CustomerName)
txtCustomerName.grid(row=0,column=1)

lblCustomerPhone = Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Name",
                       fg="black", bd=10, anchor="w")
lblCustomerPhone.grid(row=1,colum=0)
txtCustomerPhone = Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20, width=43,
                         bg="white", justify = 'left',textvariable=CustomerPhone)
txtCustomerPhone.grid(row=1,column=1)

lblCutstomerEmail = Label(LeftInsideLF,font=('arial',14, 'bold'),text="Customer Email ",
                          fg="black", bd=10, anchor='w')
lblCutstomerEmail.grid(row=2,column=0)
txtCustomerEmail = Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20, width=43,
                         bg="white", justify = 'left',textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2,column=1)


######################################### Top Right Frame ###############################################################
lblDateofOrder = Label(RightInsideLF,font=('arial',12,'bold'),text="Date of Order",
                       fg="black", bd=10, anchor="w")
lblDateofOrder.grid(row=0,column=0)
txtDateofOrder=Entry(RightInsideLF,font=('arial',14,'bold'),bd=20,width=43,
                     bg="white", justify='left', textvariable=DateOfOrder)
txtDateofOrder.grid(row=0,column=1)

lblTimeofOrder = Label(RightInsideLF,font=('arial',12,'bold'),text="Time of Order",
                       fg="black", bd=10, anchor="w")
lblTimeofOrder.grid(row=1,column=0)
txtTimeofOrder = Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=43,
                     bg="white", justify = 'left', textvariable=TimeOfOrder)
txtTimeofOrder.grid(row=1,column=1)

lblCustomerRef = Label(RightInsideLF, font=('arial',12,'bold'),text="Customer Ref",
                       fg="black", bd=10, anchor="w")
lblCustomerRef.grid(row=2,column=0)
txtCustomerRef = Entry(RightInsideLF,font=('arial',12,'bold'), bd=20,width=43,
                       bg="white", justify = 'left', textvariable=CustomerRef)
txtCustomerRef.grid(row=2,column=1)

######################################### Bottom Right Frame ##############################################
lblMethodOfPayment=Label(RightInsideLFLF,font=('arial',12,'bold'), text="Method of Payment",
                         fg="black",bd=16, anchor="w")
lblMethodOfPayment.grid(row=0,column=0)
cmdMethodOfPayment=ttk.Combobox(RightInsideLFLF,font=('arial',10,'bold'))
cmdMethodOfPayment['value']=('','Cash','Debit Card','Visa Card','Mater Card')
cmdMethodOfPayment.grid(row=0,column=1)
lblDiscount= Label(RightInsideLFLF, font=('arial',12, 'bold'),text="Discount",
                   fg="black", bd=16, anchor='w')
lblDiscount.grid(row=1,column=0)
txtDiscount = Entry(RightInsideLFLF,font=('arial', 12,'bold'),bd=16, width=18,
                    bg="white", justify = 'left',textvariable=Discount)
txtDiscount.grid(row=1,column=1)

lblTax = Label(RightInsideLFLF, font=('arial',12,'bold'),text="Tax",
               fg="black", bd=16, anchor='w')
lblTax.grid(row=2,column=0)
txtTax = Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16, width=18,
               bg="white", justify = 'left',textvariable=Tax)
txtTax.grid(row=2,column=1)

lblSubTotal = Label(RightInsideLFLF, font=('arial',12, 'bold'),text="Sub Total ",
                    fg="black",bd=16, anchor='w')
lblSubTotal .grid(row=3,column=0)
txtSubTotal = Entry(RightInsideLFLF,font=('arial',12,'bold'), bd=16, width=18,
                    bg="white", justify = 'left',textvariable=SubTotal)
txtSubTotal .grid(row=3,column=1)

lblTotalCost = Label(RightInsideLFLF, font=('arial',12, 'bold'),text="Total Cost",
                     fg="black", bd=16, anchor='w')
lblTotalCost.grid(row=4,column=0)
txtTotalCost = Entry(RightInsideLFLF,font=('arial',12,'bold'), bd=16, width=18,
                     bg="white", justify = 'left',textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1)
############################################# Bottom Left Frame ##################################################################
lblItemOrder = Label(LeftInsideLFLF, font=('arial',14, 'bold'),text="Item Order",fg="black", bd=20)
lblItemOrder.grid(row=0,column=0)
lblQty = Label(LeftInsideLFLF, font=('arial',14, 'bold'),text="Qty",fg="black",bd=10)
lblQty.grid(row=0,column=1)
lblUnitPrice = Label(LeftInsideLFLF, font=('arial',14, 'bold'),text="Item Order",fg="black", bd=20)
lblUnitPrice.grid(row=0,column=2)
lblCostofItem = Label(LeftInsideLFLF, font=('arial',14, 'bold'),text ="Cost of Item",fg="black", bd=20)
lblCostofItem.grid(row=0,column=3)
#====================
lblLegoSet = Label(LeftInsideLFLF, font=('arial',14, 'bold'),text="Lego Set",fg="black",bd=20)
lblLegoSet.grid(row=1,column=0)
lblBarbieDoll = Label(LeftInsideLFLF, font=('arial',14, 'bold'),text="Barbie Doll",fg="black",bd=20)
lblBarbieDoll.grid(row=2,column=0)
lblMarvelCostume = Label(LeftInsideLFLF, font=('arial',14, 'bold'),text="Marvel Costume",fg="black",bd=20)
lblMarvelCostume.grid(row=3,column=0)
lblStuffedToy = Label(LeftInsideLFLF, font=('arial',14, 'bold'),text="Stuffed Toy",fg="black",bd=20)
lblStuffedToy.grid(row=4,column=0)
#=====================
txtQtyLegoSet = Entry(LeftInsideLFLF,font=('arial', 12,'bold'), bd=20, width=16,
                      bg="white", justify = 'left',textvariable=QtyLegoSet)
txtQtyLegoSet.grid(row=1,column=1)
txtQtyBarbieDoll = Entry(LeftInsideLFLF,font=('arial', 12,'bold'), bd=20, width=16,
                      bg="white", justify = 'left',textvariable=QtyBarbieDoll)
txtQtyBarbieDoll.grid(row=2,column=1)
txtQtyMarvelCostume = Entry(LeftInsideLFLF,font=('arial', 12,'bold'), bd=20, width=16,
                      bg="white", justify = 'left',textvariable=QtyMarvelCostume)
txtQtyMarvelCostume.grid(row=3,column=1)
txtQtyStuffedToy = Entry(LeftInsideLFLF,font=('arial', 12,'bold'), bd=20, width=16,
                      bg="white", justify = 'left',textvariable=QtyStuffedToy)
txtQtyStuffedToy.grid(row=4,column=1)
#===================================
txtUnitPriceLegoSet = Entry(LeftInsideLFLF, font=('arial',12,'bold'), bd=20, width=16,
                            bg="white", justify = 'left',textvariable=UnitPriceLegoSet)
txtUnitPriceLegoSet.grid(row=1,column=2)
txtUnitPriceBarbieDoll = Entry(LeftInsideLFLF, font=('arial',12,'bold'), bd=20, width=16,
                            bg="white", justify = 'left',textvariable=UnitPriceBarbieDoll)
txtUnitPriceBarbieDoll.grid(row=2,column=2)
txtUnitPriceMarvelCostume = Entry(LeftInsideLFLF, font=('arial',12,'bold'), bd=20, width=16,
                            bg="white", justify = 'left',textvariable=UnitPriceMarvelCostume)
txtUnitPriceMarvelCostume.grid(row=3,column=2)
txtUnitPriceStuffedToy = Entry(LeftInsideLFLF, font=('arial',12,'bold'), bd=20, width=16,
                            bg="white", justify = 'left',textvariable=UnitPriceStuffedToy)
txtUnitPriceStuffedToy.grid(row=4,column=2)
#====================================
txtCostofLegoSet = Entry(LeftInsideLFLF,font=('arial',12,'bold'), bd=20, width=16,
                         bg="white", justify = 'left',textvariable=CostofLegoSet)
txtCostofLegoSet.grid(row=1,column=3)
txtCostofBarbieDoll = Entry(LeftInsideLFLF,font=('arial',12,'bold'), bd=20, width=16,
                         bg="white", justify = 'left',textvariable=CostofBarbieDoll)
txtCostofBarbieDoll.grid(row=2,column=3)
txtCostofMarvelCostume = Entry(LeftInsideLFLF,font=('arial',12,'bold'), bd=20, width=16,
                         bg="white", justify = 'left',textvariable=CostofMarvelCostume)
txtCostofMarvelCostume.grid(row=3,column=3)
txtCostofStuffedToy = Entry(LeftInsideLFLF,font=('arial',12,'bold'), bd=20, width=16,
                         bg="white", justify = 'left',textvariable=CostofStuffedToy)
txtCostofStuffedToy.grid(row=4,column=3)

#============================================ Buttons Right Frame==================================================
btnTotalCost=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bond'), width=11,
                    text="Total Cost", bg="white",command=CostofOrder).grid(row=0,column=0)
btnReset=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bond'), width=11,
                    text="Reset", bg="white",command=Reset).grid(row=1,column=0)
btnOrderRef=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bond'), width=11,
                    text="Order Ref", bg="white",command=OrderRef).grid(row=2,column=0)
btnExit=Button(RightInsideRFRF,pady=8,bd=8,fg="black",font=('arial',16,'bond'), width=11,
                    text="Exit", bg="white",command=Exit).grid(row=3,column=0)




# F3 part4 Recipt

root = Tk()

def reciept():
    top = Toplevel()
    price1 = 3000
    qty1 = 3
    total1 = price1*qty1

    price2 = 5000
    qty2 = 4
    total2 = price1*qty2

    l = Label(top,text='---------RECIEPT----------')
    l.pack()
    heading = Label(top,text='PRICE\tQTY\tTOTAL')
    heading.pack()

    item1 = Label(top,text=f'{price1}\t{qty1}\t{total1}')
    item1.pack()

    item2 = Label(top,text=f'{price2}\t{qty2}\t{total2}')
    item2.pack()

b = Button(root,text='Print reciept',command=reciept)
b.pack(padx=10,pady=10)
root.mainloop()


root.mainloop()


