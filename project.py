from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#Functionlity part
# Clear Button
def clear():
    bathSoapEntry.delete(0,END)
    faceCreamEntry.delete(0,END)
    hairSprayEntry.delete(0,END)
    faceWashEntry.delete(0,END)
    hairGelEntry.delete(0,END)
    bodyLotionEntry.delete(0,END)

    riceEntry.delete(0,END)
    oilEntry.delete(0,END)
    daalEntry.delete(0,END)
    wheatEntry.delete(0,END)
    sugarEntry.delete(0, END)
    teaEntry.delete(0,END)

    maazaEntry.delete(0,END)
    pepsiEntry.delete(0,END)
    spriteEntry.delete(0,END)
    dewEntry.delete(0,END)
    frootiEntry.delete(0,END)
    cococolaEntry.delete(0,END)

    bathSoapEntry.insert(0, 0)
    faceCreamEntry.insert(0, 0)
    hairSprayEntry.insert(0, 0)
    faceWashEntry.insert(0, 0)
    hairGelEntry.insert(0, 0)
    bodyLotionEntry.insert(0, 0)

    riceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    daalEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    teaEntry.insert(0, 0)

    maazaEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    frootiEntry.insert(0, 0)
    cococolaEntry.insert(0, 0)


    cosmeticsPriceEntry.delete(0,END)
    GroceryPriceEntry.delete(0,END)
    drinkPriceEntry.delete(0,END)

    cosmeticsTaxEntry.delete(0,END)
    GroceryTaxEntry.delete(0,END)
    drinkTaxEntry.delete(0,END)

    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)

    textArea.delete(1.0,END)


# Send email
def send_email():
    def send_gmail():
       try:
           ob = smtplib.SMTP('smtp.gmail.com',587)
           ob.starttls()
           ob.login(sender_entry.get(),password_entry.get())
           message=email_textarea.get(1.0,END)
           ob.sendmail(sender_entry.get(),reciever_entry.get(),message)
           ob.quit()
           messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
           root1.destroy()
       except:
           messagebox.showerror('Error','Something went wrong , please try again',parent=root1)
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        #Sender Frame
        sender_frame = LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        sender_frame.grid(column=0,row=0,padx=40,pady=20)

        # sender label
        sender_label = Label(sender_frame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        sender_label.grid(column=0,row=0,padx=10,pady=8)
       # sender Entry
        sender_entry = Entry(sender_frame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        sender_entry.grid(column=1,row=0,padx=10,pady=8)

        #Password label
        password_label = Label(sender_frame, text="Password", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        password_label.grid(column=0, row=1, padx=10, pady=8)
        # Password  Entry
        password_entry = Entry(sender_frame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE,show='*')
        password_entry.grid(column=1, row=1, padx=10, pady=8)

        # recipient
        recipient_frame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'), bd=6, bg='gray20', fg='white')
        recipient_frame.grid(column=0, row=1, padx=40, pady=20)

       # reciever label

        reciever_label = Label(recipient_frame, text="Email Address", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        reciever_label.grid(column=0, row=0, padx=10, pady=8)

       # reciever  Entry

        reciever_entry = Entry(recipient_frame, font=('arial', 14, 'bold'), bd=2, width=23, relief=RIDGE)
        reciever_entry.grid(column=1, row=0, padx=10, pady=8)

       # Message label
        message_label = Label(recipient_frame, text="Message", font=('arial', 14, 'bold'), bd=6, bg='gray20', fg='white')
        message_label.grid(column=0, row=1, padx=10, pady=8)

        # email textarea
        email_textarea=Text(recipient_frame,font=('arial', 14, 'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(column=0,row=2,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textArea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        # Send Button
        send_button = Button(root1,text='SEND',font=('arial', 16, 'bold'),width=15,command=send_gmail)
        send_button.grid(column=0,row=2,pady=20)
        root1.mainloop()

#     Print Bill
def print_bill():
    if textArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
     file = tempfile.mktemp('.txt')
     open(file,'w').write(textArea.get(1.0,END))
     os.startfile(file,'print')

#Search bill by clicking  search button
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
           f = open(f'bills/{i}','r')
           textArea.delete('1.0',END)
           for data in f:
               textArea.insert(END,data)
           f.close()
           break
    else:
        messagebox.showerror('Error','Invalid Bill Number')

# os bills
if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global bill_number
    result = messagebox.askyesno('Confirm','Do You want to save the bill?')
    if result:
        bill_content =textArea.get(1.0,END)
        file = open(f'bills/{bill_number}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill number {bill_number} is Saved successfully')


# Random bill number
bill_number = random.randint(500,1000)

def total():
    global soap_price,face_cream_price,face_wash_price,hair_spray_price,hair_gel_price,body_lotion_price
    global rice_price,oil_price,daal_price,wheat_price,sugar_price,tea_price
    global maaza_price,pepsi_price,sprite_price,dew_price,frooti_price,coco_cola_price
    global totalbill
 #cosmetic price calculation
    soap_price =int(bathSoapEntry.get())*20
    face_cream_price =int(faceCreamEntry.get())*50
    face_wash_price = int(faceWashEntry.get()) * 100
    hair_spray_price = int(hairSprayEntry.get()) * 150
    hair_gel_price = int(hairGelEntry.get()) * 80
    body_lotion_price = int(bodyLotionEntry.get()) * 60
    total_comestic_price =soap_price+face_cream_price+face_wash_price+hair_spray_price+hair_gel_price+body_lotion_price
    cosmeticsPriceEntry.delete(0,END)
    cosmeticsPriceEntry.insert(0,f'{total_comestic_price} Rs')
    cosmetic_tax = total_comestic_price*0.12
    cosmeticsTaxEntry.delete(0,END)
    cosmeticsTaxEntry.insert(0,f'{cosmetic_tax} Rs')
    #Grocery price calculation
    rice_price = int(riceEntry.get())*30
    oil_price  = int(oilEntry.get())*100
    daal_price = int(daalEntry.get())*120
    wheat_price = int(wheatEntry.get())*50
    sugar_price =int(sugarEntry.get())*140
    tea_price = int(teaEntry.get())*80
    total_grocery_price = rice_price+oil_price+daal_price+wheat_price+sugar_price+tea_price
    GroceryPriceEntry.delete(0,END)
    GroceryPriceEntry.insert(0,f'{total_grocery_price} Rs')
    grocery_tax = total_grocery_price * 0.05
    GroceryTaxEntry.delete(0, END)
    GroceryTaxEntry.insert(0, f'{grocery_tax} Rs')

    # Cool drinks Calculation
    maaza_price = int(maazaEntry.get())*50
    pepsi_price = int(pepsiEntry.get())*20
    sprite_price =int(spriteEntry.get())*30
    dew_price = int(dewEntry.get())*20
    frooti_price =int(frootiEntry.get())*45
    coco_cola_price =int(cococolaEntry.get())*90
    total_cool_drinks_price = maaza_price+pepsi_price+sprite_price+dew_price+frooti_price+coco_cola_price
    drinkPriceEntry.delete(0,END)
    drinkPriceEntry.insert(0,f'{total_cool_drinks_price} Rs')
    drink_tax = total_cool_drinks_price * 0.08
    drinkTaxEntry.delete(0, END)
    drinkTaxEntry.insert(0, f'{drink_tax} Rs')

    # total Bill

    totalbill = total_comestic_price+total_grocery_price+total_cool_drinks_price+cosmetic_tax+grocery_tax+drink_tax

#Bill button
def bill_area():

    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticsPriceEntry.get()=='' and GroceryPriceEntry.get()==''and drinkPriceEntry.get()=='':
        messagebox.showerror('Error', 'No Products Are Selected')
    elif cosmeticsPriceEntry.get()=='0 Rs' and GroceryPriceEntry.get()=='0 Rs' and drinkPriceEntry.get()=='0 Rs':
        messagebox.showerror('Error', 'No Products Are Selected')
    else:
        textArea.delete(1.0,END)
        textArea.insert(END,'\t\t **Welcome Customer**\n')
        textArea.insert(END,f'\n Bill Number : {bill_number}\n')
        textArea.insert(END, f'\n Customer Name : {nameEntry.get()}\n')
        textArea.insert(END, f'\n Customer Phone number : {phoneEntry.get()}\n')
        textArea.insert(END,'\n============================================================')
        textArea.insert(END,'Product\t\t\t Quantity\t\t\t Price')
        textArea.insert(END, '\n============================================================')
        #Cosmetics
    if bathSoapEntry.get()!='0':
        textArea.insert(END,f'\n Bath Soap\t\t\t {bathSoapEntry.get()}\t\t\t{soap_price} Rs')
    if faceCreamEntry.get()!='0':
        textArea.insert(END,f'\n Face Cream\t\t\t {faceCreamEntry.get()}\t\t\t{face_cream_price} Rs')
    if faceWashEntry.get()!='0':
        textArea.insert(END,f'\n Face Wash\t\t\t {faceWashEntry.get()}\t\t\t{face_wash_price} Rs')
    if hairSprayEntry.get()!='0':
        textArea.insert(END,f'\n Hair Spray\t\t\t {hairSprayEntry.get()}\t\t\t{hair_spray_price} Rs')
    if hairGelEntry.get()!='0':
        textArea.insert(END,f'\n Hair gel\t\t\t {hairGelEntry.get()}\t\t\t{hair_gel_price} Rs')
    if bodyLotionEntry.get()!='0':
        textArea.insert(END,f'\n Body Lotion\t\t\t {bodyLotionEntry.get()}\t\t\t{body_lotion_price} Rs')

        #Grocery

    if riceEntry.get() != '0':
        textArea.insert(END, f'\n Rice\t\t\t {riceEntry.get()}\t\t\t{rice_price} Rs')
    if oilEntry.get() != '0':
        textArea.insert(END, f'\n Oil\t\t\t {oilEntry.get()}\t\t\t{oil_price} Rs')
    if daalEntry.get() != '0':
        textArea.insert(END, f'\n Daal\t\t\t {daalEntry.get()}\t\t\t{daal_price} Rs')
    if wheatEntry.get() != '0':
        textArea.insert(END, f'\n Wheat\t\t\t {wheatEntry.get()}\t\t\t{wheat_price} Rs')
    if sugarEntry.get() != '0':
        textArea.insert(END, f'\n Sugar\t\t\t {sugarEntry.get()}\t\t\t{sugar_price} Rs')
    if teaEntry.get() != '0':
        textArea.insert(END, f'\n Tea\t\t\t {teaEntry.get()}\t\t\t{tea_price} Rs')

     #Cool Drinks
    if maazaEntry.get() != '0':
        textArea.insert(END, f'\n Maaza\t\t\t {maazaEntry.get()}\t\t\t{maaza_price} Rs')
    if pepsiEntry.get() != '0':
        textArea.insert(END, f'\n Pepsi\t\t\t {pepsiEntry.get()}\t\t\t{pepsi_price} Rs')
    if spriteEntry.get() != '0':
        textArea.insert(END, f'\n Sprite\t\t\t {spriteEntry.get()}\t\t\t{sprite_price} Rs')
    if dewEntry.get() != '0':
        textArea.insert(END, f'\n Dew\t\t\t {dewEntry.get()}\t\t\t{dew_price} Rs')
    if frootiEntry.get() != '0':
        textArea.insert(END, f'\n Frooti\t\t\t {frootiEntry.get()}\t\t\t{frooti_price} Rs')
    if cococolaEntry.get() != '0':
        textArea.insert(END, f'\n Coco Cola\t\t\t {cococolaEntry.get()}\t\t\t{coco_cola_price} Rs')
    textArea.insert(END,'\n------------------------------------------------------------')

    # Tax

    if cosmeticsTaxEntry.get() !='0.0 Rs':
        textArea.insert(END,f'\nCosmetic Tax \t\t\t\t{cosmeticsTaxEntry.get()}')
    if GroceryTaxEntry.get() != '0.0 Rs':
        textArea.insert(END, f'\nGrocery Tax \t\t\t\t{GroceryTaxEntry.get()}')
    if drinkTaxEntry.get() !='0.0 Rs':
        textArea.insert(END,f'\nDrinks Tax \t\t\t\t{drinkTaxEntry.get()}')
    #Insert total bill
    textArea.insert(END,f'\n\nTotal Bill\t\t\t\t{totalbill} Rs')
    textArea.insert(END, '\n------------------------------------------------------------')
    save_bill()

#GUI part
root = Tk()
root.title("Retail Billing System")
root.geometry("1278x685")
root.iconbitmap('icon.ico')

# Label
headinglabel = Label(root,text='Retail Billing System',font=('times new roman',30,'bold',)
                     ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
headinglabel.pack(fill = X)

# Customer details

customer_details_frame =LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)

# Name label
nameLabel = Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(column=0,row=0,padx= 20)

# Name Entry

nameEntry = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(column=1,row=0,padx =8)

# phone label
phoneLabel = Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(column=2,row=0,padx= 20,pady =2)

# phone Entry

phoneEntry = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(column=3,row=0,padx =8)

# Bill Number label
billnumberLabel = Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(column=4,row=0,padx= 20,pady =2)

# bill Entry

billnumberEntry = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(column=5,row=0,padx =8)

# Button

searchbutton =Button(customer_details_frame,text = 'SEARCH',font = ('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchbutton.grid(column = 6,row =0,padx=20,pady=8)

#product frame

productsFrame = Frame(root)
productsFrame.pack()

#Cosmetics
cosmeticsFrame =LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(column = 0,row= 0)



bathSoapLabel = Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathSoapLabel.grid(column = 0,row =0,pady=9,padx=10,sticky='w')

bathSoapEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
bathSoapEntry.grid(column =1,row =0,pady =9,padx=10)
bathSoapEntry.insert(0,0)

#facecream

faceCreamLabel = Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
faceCreamLabel.grid(column = 0,row =1,pady=9,padx=10,sticky='w')

faceCreamEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
faceCreamEntry.grid(column =1,row =1,pady =9,padx=10)
faceCreamEntry.insert(0,0)
#facewash

faceWashLabel = Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
faceWashLabel.grid(column = 0,row =2,pady=9,padx=10,sticky= 'w')

faceWashEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
faceWashEntry.grid(column =1,row =2,pady =9,padx=10)
faceWashEntry.insert(0,0)

# Hairspray


hairSprayLabel = Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairSprayLabel.grid(column = 0,row =3,pady=9,padx=10,sticky='w')

hairSprayEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
hairSprayEntry.grid(column =1,row =3,pady =9,padx=10)
hairSprayEntry.insert(0,0)

# #Hair Gel

hairGelLabel = Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairGelLabel.grid(column = 0,row =4,pady=9,padx=10,stick ='w')

hairGelEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
hairGelEntry.grid(column =1,row =4,pady =9,padx=10)
hairGelEntry.insert(0,0)


# # #Body Lotion

bodyLotionLabel = Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bodyLotionLabel.grid(column = 0,row =5,pady=9,padx=10,sticky = 'w')

bodyLotionEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
bodyLotionEntry.grid(column =1,row =5,pady =9,padx=10)
bodyLotionEntry.insert(0,0)


#Grocery

groceryFrame =LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(column = 1,row= 0)

#Rice

riceLabel = Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLabel.grid(column = 0,row =0,pady=9,padx=10,sticky='w')

riceEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
riceEntry.grid(column =1,row =0,pady =9,padx=10)
riceEntry.insert(0,0)

#Oil

oilLabel = Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLabel.grid(column = 0,row =1,pady=9,padx=10,sticky='w')

oilEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
oilEntry.grid(column =1,row =1,pady =9,padx=10)
oilEntry.insert(0,0)
#Daal

daalLabel = Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
daalLabel.grid(column = 0,row =2,pady=9,padx=10,sticky='w')

daalEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
daalEntry.grid(column =1,row =2,pady =9,padx=10)
daalEntry.insert(0,0)
#wheat

wheatLabel = Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(column = 0,row =3,pady=9,padx=10,sticky='w')

wheatEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
wheatEntry.grid(column =1,row =3,pady =9,padx =10)
wheatEntry.insert(0,0)
#sugar

sugarLabel = Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(column = 0,row =4,pady=9,padx=10,sticky='w')

sugarEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
sugarEntry.grid(column =1,row =4,pady =9,padx=10)
sugarEntry.insert(0,0)
#tea

teaLabel = Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')
teaLabel.grid(column = 0,row =5,pady=9,padx=10,sticky='w')

teaEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
teaEntry.grid(column =1,row =5,pady =9,padx=10)
teaEntry.insert(0,0)

#CoolDrinks

DrinksFrame =LabelFrame(productsFrame,text='Cool Drinks',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
DrinksFrame.grid(column = 2,row= 0)

#Maaza

maazaLabel = Label(DrinksFrame,text='Maaza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
maazaLabel.grid(column = 0,row =0,pady=9,padx=10,sticky='w')

maazaEntry = Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
maazaEntry.grid(column =1,row =0,pady =9,padx=10)
maazaEntry.insert(0,0)
#Pepsi

pepsiLabel = Label(DrinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pepsiLabel.grid(column = 0,row =1,pady=9,padx=10,sticky='w')

pepsiEntry = Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
pepsiEntry.grid(column =1,row =1,pady =9,padx=10)
pepsiEntry.insert(0,0)

#Sprite

spriteLabel = Label(DrinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(column = 0,row =2,pady=9,padx=10,sticky='w')

spriteEntry = Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
spriteEntry.grid(column =1,row =2,pady =9,padx=10)
spriteEntry.insert(0,0)

#Dew

dewLabel = Label(DrinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dewLabel.grid(column = 0,row =3,pady=9,padx=10,sticky='w')

dewEntry = Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
dewEntry.grid(column =1,row =3,pady =9,padx=10)
dewEntry.insert(0,0)

#Frooti

frootiLabel = Label(DrinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',fg='white')
frootiLabel.grid(column = 0,row =4,pady=9,padx=10,sticky='w')

frootiEntry = Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
frootiEntry.grid(column =1,row =4,pady =9,padx=10)
frootiEntry.insert(0,0)

#Coco cola

cococolaLabel = Label(DrinksFrame,text='Coco cola',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cococolaLabel.grid(column = 0,row =5,pady=9,padx=10,sticky='w')

cococolaEntry = Entry(DrinksFrame,font=('times new roman',15,'bold'),width=10,bd=5 )
cococolaEntry.grid(column =1,row =5,pady =9,padx=10)
cococolaEntry.insert(0,0)
#Billframe

billFrame = Frame(productsFrame,bd=8,relief=GROOVE)
billFrame.grid(column=3,row=0,padx=10)

billareaLabel = Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollBar = Scrollbar(billFrame,orient=VERTICAL)
scrollBar.pack(side=RIGHT,fill=Y)
textArea = Text(billFrame,height=18,width=60,yscrollcommand= scrollBar.set,font=('Courier',10,'bold'))
textArea.pack()
scrollBar.config(command=textArea.yview)

#Bill Menu
billMenuFrame =LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
billMenuFrame.pack(fill=X) # # Adjusted the packing here

#cosmetics Price
cosmeticsPriceLabel = Label(billMenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmeticsPriceLabel.grid(column = 0,row =0,pady=6,padx=10,sticky='w')

cosmeticsPriceEntry = Entry(billMenuFrame,font=('times new roman',14,'bold'),width=10,bd=5 )
cosmeticsPriceEntry.grid(column =1,row =0,pady =6,padx=10)

#Grocery Price
GroceryPriceLabel = Label(billMenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
GroceryPriceLabel.grid(column = 0,row =1,pady=6,padx=10,sticky='w')

GroceryPriceEntry = Entry(billMenuFrame,font=('times new roman',14,'bold'),width=10,bd=5 )
GroceryPriceEntry.grid(column =1,row =1,pady =6,padx=10)

#Cool Drink Price
drinkPriceLabel = Label(billMenuFrame,text='Cool Drink Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkPriceLabel.grid(column = 0,row =2,pady=6,padx=10,sticky='w')

drinkPriceEntry = Entry(billMenuFrame,font=('times new roman',14,'bold'),width=10,bd=5 )
drinkPriceEntry.grid(column =1,row =2,pady =6,padx=10)

#cosmetics tax
cosmeticsTaxLabel = Label(billMenuFrame,text='Cosmetic Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmeticsTaxLabel.grid(column = 2,row =0,pady=6,padx=10,sticky='w')

cosmeticsTaxEntry = Entry(billMenuFrame,font=('times new roman',14,'bold'),width=10,bd=5 )
cosmeticsTaxEntry.grid(column =3,row =0,pady =6,padx=10)

#Grocery tax
GroceryTaxLabel = Label(billMenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
GroceryTaxLabel.grid(column = 2,row =1,pady=6,padx=10,sticky='w')

GroceryTaxEntry = Entry(billMenuFrame,font=('times new roman',14,'bold'),width=10,bd=5 )
GroceryTaxEntry.grid(column =3,row =1,pady =6,padx=10)

#Cool Drink Price
drinkTaxLabel = Label(billMenuFrame,text='Cool Drink Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkTaxLabel.grid(column = 2,row =2,pady=6,padx=10,sticky='w')

drinkTaxEntry = Entry(billMenuFrame,font=('times new roman',14,'bold'),width=10,bd=5 )
drinkTaxEntry.grid(column =3,row =2,pady =6,padx=10)

#ButtonFrame

buttonFrame = Frame(billMenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(column=4,row=0,rowspan=3)

totalButton = Button(buttonFrame,text= 'Total',font=('Arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8 ,pady=10,command=total)
totalButton.grid(column=0,row=0,pady=20,padx=5)

billButton = Button(buttonFrame,text= 'Bill',font=('Arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8 ,pady=10,command=bill_area)
billButton.grid(column=1,row=0,pady=20,padx=5)

emailButton = Button(buttonFrame,text= 'Email',font=('Arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8 ,pady=10,command=send_email)
emailButton.grid(column=2,row=0,pady=20,padx=5)

printButton = Button(buttonFrame,text= 'Print',font=('Arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8 ,pady=10,command=print_bill)
printButton.grid(column=3,row=0,pady=20,padx=5)

clearButton = Button(buttonFrame,text= 'Clear',font=('Arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8 ,pady=10,command=clear)
clearButton.grid(column=4,row=0,pady=20,padx=5)


root.mainloop()


