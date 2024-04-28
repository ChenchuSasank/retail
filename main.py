from tkinter import *
from tkinter import messagebox
import string
import secrets
import random, os, tempfile, smtplib
import qrcode

user_credentials = {'username1': 'password1', 'username2': 'password2'}

def authenticate_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in user_credentials and user_credentials[username] == password:
        print("Authentication successful. Welcome, {}!".format(username))
    else:
        print("Authentication failed. Incorrect username or password.")

def add_user():
    new_username = input("Enter a new username: ")
    new_password = input("Enter a new password: ")
    user_credentials[new_username] = new_password
    print("User '{}' added successfully.".format(new_username))

if __name__ == "__main__":
    print("Welcome to the secure application.")
    while True:
        print("Select an option:")
        print("1. Authenticate user")
        print("2. Add a new user")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            authenticate_user()
        elif choice == '2':
            add_user()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def clear():
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    hairsprayEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    bodylotionEntry.delete(0, END)

    riceEntry.delete(0, END)
    oilEntry.delete(0, END)
    daalEntry.delete(0, END)
    wheatEntry.delete(0, END)
    sugarEntry.delete(0, END)
    teaEntry.delete(0, END)

    mazzaEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    spriteEntry.delete(0, END)
    dewEntry.delete(0, END)
    frootiEntry.delete(0, END)
    cocacolaEntry.delete(0, END)

    bathsoapEntry.insert(0, 0)
    facecreamEntry.insert(0, 0)
    facewashEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)

    riceEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    daalEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    teaEntry.insert(0, 0)

    mazzaEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    frootiEntry.insert(0, 0)
    cocacolaEntry.insert(0, 0)

    cosmetictaxEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    drinkstaxEntry.delete(0, END)

    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkspriceEntry.delete(0, END)

    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.get(0, END)

    textarea.delete(1.0, END)

def generate_access_token():
  alphabet = string.ascii_letters + string.digits
  token = ''.join(secrets.choice(alphabet) for _ in range(20))
  access_link = "https://buy.stripe.com/test_3cs3eU5YD3YP3yUcN0"
  return access_link

def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            ob.sendmail(senderEntry.get(), recieverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent', parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error', 'Something went wrong, Please try again', parent=root1)

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty')
    
        # Create a QR code with the bill information and save it to a file
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(textarea.get(1.0, END))
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        qr_image.show()
        qr_image.save('QR_Code.png')  # Save the QR code as 'bill_qr.png'



        root1 = Toplevel()
        root1.grab_set()
        root1.title('send gmail')
        root1.config(bg='gray20')
        root1.resizable(0, 0)

        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)

        senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='gray20',fg='white')
        senderLabel.grid(row=0,column=0,padx=10,pady=8)

        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)

        passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='gray20',fg='white')
        passwordLabel.grid(row=1,column=0,padx=10,pady=8)

        passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE, show='*')
        passwordEntry.grid(row=1,column=1,padx=10,pady=8)

        recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)

        recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bg='gray20',fg='white')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)

        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)

        messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='gray20',fg='white')
        messageLabel.grid(row=1,column=0,padx=10,pady=8)

        email_textarea=Text(recipientFrame, font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

        sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)

    root.mainloop()

def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')

if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)

billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are Requird')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
        messagebox.showerror('Error','No Products are Selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
        messagebox.showerror('Error', 'No Products are Selected')
    else:
        textarea.delete(1.0,END)

        textarea.insert(END,'\t\t**Welcome Customers**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}\n')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomer Phone Number: {phoneEntry.get()}\n')
        textarea.insert(END,'\n=======================================================')
        textarea.insert(END,'\nProduct\t\t\tQuantity\t\tPrice')
        textarea.insert(END,'\n=======================================================')
        if bathsoapEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if hairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if facewashEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        if bodylotionEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')

        if riceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if daalEntry.get()!='0':
            textarea.insert(END,f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
        if oilEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if sugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
        if wheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
        if teaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')

        if mazzaEntry.get()!='0':
            textarea.insert(END,f'\nMazza\t\t\t{mazzaEntry.get()}\t\t\t{mazzaprice} Rs')
        if spriteEntry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
        if dewEntry.get()!='0':
            textarea.insert(END,f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
        if frootiEntry.get()!='0':
            textarea.insert(END,f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
        if pepsiEntry.get()!='0':
            textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
        if cocacolaEntry.get()!='0':
            textarea.insert(END,f'\nCoca Cola\t\t\t{cocacolaEntry.get()}\t\t\t{cocacolaprice} Rs')
        textarea.insert(END,'\n-------------------------------------------------------')

        if cosmetictaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmetictaxEntry.get()}')
        if grocerytaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
        if drinkstaxEntry.get()!='0.0 Rs':
            textarea.insert(END,f'\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')
        textarea.insert(END,'\n-------------------------------------------------------')
        save_bill()

def total():
    global soapprice,hairsprayprice,hairgelprice,facecreamprice,facewashprice,bodylotionprice
    global riceprice,daalprice,oilprice,sugarprice,wheatprice,teaprice
    global mazzaprice,spriteprice,dewprice,frootiprice,pepsiprice,cocacolaprice
    global totalbill
    #cosmetics price calculation
    soapprice=int(bathsoapEntry.get()) * 20
    facecreamprice=int(facecreamEntry.get()) * 50
    facewashprice=int(facewashEntry.get()) * 100
    hairsprayprice=int(hairsprayEntry.get()) * 150
    hairgelprice=int(hairgelEntry.get()) * 80
    bodylotionprice=int(bodylotionEntry.get()) * 60

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
    cosmetictax=totalcosmeticprice*0.12
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'{cosmetictax} Rs')

    #grocery price calculation
    riceprice=int(riceEntry.get())*30
    daalprice=int(daalEntry.get())*100
    oilprice=int(oilEntry.get())*120
    sugarprice=int(sugarEntry.get())*50
    teaprice=int(teaEntry.get())*140
    wheatprice=int(wheatEntry.get())*80

    totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax=totalgroceryprice*0.05
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,f'{grocerytax} Rs')

    #drinks price calculation
    mazzaprice=int(mazzaEntry.get())*50
    frootiprice=int(frootiEntry.get())*20
    dewprice=int(dewEntry.get())*30
    pepsiprice=int(pepsiEntry.get())*20
    spriteprice=int(spriteEntry.get())*45
    cocacolaprice=int(cocacolaEntry.get())*90

    totaldrinksprice=mazzaprice+frootiprice+dewprice+pepsiprice+spriteprice+cocacolaprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0, str(totaldrinksprice) + ' Rs')
    drinkstax = totaldrinksprice * 0.08
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0, str(drinkstax) +' Rs')

    totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmetictax+grocerytax+drinkstax

#GUI Part
root = Tk()
root.title('Retail Billing System')
root.geometry('1270x700')
root.iconbitmap('icon.ico')
headingLabel = Label(root, text='Retail Billing System',font=('times new roman',30,'bold'),bg='grey20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=20,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=20)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='gray20',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
drinksFrame.grid(row=0,column=2)

mazzaLabel=Label(drinksFrame,text='Mazza',font=('times new roman',15,'bold'),bg='gray20',fg='white')
mazzaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

mazzaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
mazzaEntry.grid(row=0,column=1,pady=9,padx=10)
mazzaEntry.insert(0,0)

pepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

dewLabel=Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=3,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

frootiLabel=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='gray20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cocacolaLabel=Label(drinksFrame,text='Coca Cola',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cocacolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cocacolaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cocacolaEntry.grid(row=5,column=1,pady=9,padx=10)
cocacolaEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Label Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkspriceLabel=Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinkstaxLabel=Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',14,'bold'),bg='gray20',fg='white')
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()