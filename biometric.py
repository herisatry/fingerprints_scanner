from guizero import * ## import all the GUI element

## start functions ##

def open_admin():
    window_admin.show()
    app.hide()

def back_to_main(): 
    app.show()
    window_admin.hide()

def open_Display_info():
    window_info_user.show()
    window_admin.hide()
    app.hide()

def open_add_user():
    WindowAdd_user.show()
    window_info_user.hide()
    


## end functions ##


## Start GUI ##
## can replace fingerprint by the project name
## main windows
app = App(title="Fingerprint")
text = Text(app, text=" PLACE YOUR FINGER TO ACCESS",size=21)
picture= Picture(app, image="img/fingerprint_icon.png")

close_button = PushButton(app, text="< Back", command=back_to_main) ##dummy button to go back
open_button = PushButton(app, text="next >", command=open_admin) ##dummy button to see next window

## second window / access granted to admin panel
window_admin = Window(app, title="Admin panel")
text = Text(window_admin, text=" Welcome to the Admin panel",size=14)
picture= Picture(window_admin, image="img/fingerprint_icon.png")
window_admin.hide()


close_button = PushButton(window_admin, text="< Back", command=back_to_main)##dummy button to go back
open_button = PushButton(window_admin, text="Next >", command=open_Display_info) ##dummy button to see next window


##User info display window
window_info_user = Window(app, title="User informations")
picture=Picture(window_info_user, image="img/User.png")
window_info_user.hide()

##User details

text = Text(window_info_user, text=" Name : ",size=14)
text = Text(window_info_user, text=" User ID : ",size=14)
text = Text(window_info_user, text=" Sex : ",size=14)
text = Text(window_info_user, text=" Birthday : ",size=14)

open_button = PushButton(window_info_user, text="Next >", command=open_add_user) ##dummy button to see next window

app.display()


## Add user window / needs correction

##WindowAdd_user = Window ( app, title =" Add User")

##User details

##text = Text(Add_user, text=" Name ")
##input_name = TextBox(Add_user, text=" Name ")
##text = Text(Add_user, text=" Sex ")
##input_sex = TextBox(Add_user, text=" M or F")
##text = Text(Add_user, text=" Birthday : ",size=14)
##text = TextBox(Add_user, text=" DD/MM/YYYY ")
##app.display()




