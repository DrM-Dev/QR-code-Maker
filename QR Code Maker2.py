# QR-CODE MAKER V2  by  Dr.M-Dev:
#====================================================================================
#====================================================================================
# Imports__________________________
import qrcode
import time
from turtle import Screen
from PIL import Image
#
from loading_manager import LoadingScreen
#
from tkinter import filedialog

#=============
screen = Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.title("QR-code Maker V2")
#-----------bg-pick
screen.bgpic("QR_maker_bg.png")

#+++++++++++++
load_icon = LoadingScreen()
# load_icon.start_loading_screen(0,0, "white")
#=============
#----------------------- #default
data = "ERROR"
#
qr_size = 10
qr_borders = 4
#
qr_back_color = "White"
qr_fill_color= "Black"



available_colors = ["black", "white", "grey", "gray", "blue", "red", "green", "purple", "brown"]




#====================================================================================
print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')


print("******** WELCOME TO QR-CODE MAKER V2   -   By: Dr.m DEV *********")
##=====================================================================
##=====================================================================
##=====================================================================
##=====================================================================USER INPUT\\
qr_type = screen.textinput(title="pick data type",prompt='Pick one of the following data type to turn into QR-code\n1-Type "1" or "URL" for URL/Link'
                                                         '\n2-Type "2" or "file" for txt-file'
                                                         '\n3-Type "3" or "Text" for simple text').lower()
qr_type = str(qr_type)

#DEBUG
# print(qr_type)

#_________________________________________[1]URL/Link
if qr_type == "1" or qr_type == "url" or qr_type == "link":
    data = screen.textinput(title="URL / Link", prompt="Paste your URL link here:")


#_________________________________________[2]TEXT FILE
if qr_type == "2" or qr_type == "file":
    directory_set = False
    while not directory_set:
        try:
            file_directory = filedialog.askopenfilename()
            with open(file_directory) as text_file:
                txt_content = text_file.read()
                data = txt_content
                directory_set = True
        except FileNotFoundError:
            screen.textinput(title="⚠️Invalid Directory⚠️",prompt="Press [OK] to try again :)")
            directory_set = False
        # DEBUG
        # print(data)

#_________________________________________[3]just text
if qr_type == "3" or qr_type == "text":
    data = screen.textinput(title="Input Text", prompt="Write whatever you want here:               ")




#=====================================================================
#=====================================================================
#XXXXXXXXXXXXXXXXXXX
more_options = screen.textinput(title="More Style Options", prompt="Do you want to edit the QR-code details, like size and color?"
                                                                   "\ntype [Yes/Y] or [No/N]"
                                                                   "\nor press [OK] to skip").lower()
#XXXXXXXXXXXXXXXXXXX
#=====================================================================
#=====================================================================




#=====================================================================USER STYLE-INPUT
if more_options == "yes" or more_options == "y":
    global LOADING_TEXT_COLOR
    ########################
    qr_size_picked = False
    qr_borders_picked = False
    ########################
    while not qr_size_picked:
        try:
            qr_size = int(screen.textinput(title="QR-Code size",prompt="Enter the size of the square you want:\n default is [10]"))
            qr_size_picked = True
        except TypeError:
            screen.textinput(title="⚠️Invalid Input⚠️", prompt="Please enter a number, press [OK] to try again :)")
    #--------------------------
    while not qr_borders_picked:
        try:
            qr_borders = int(screen.textinput(title="QR-Code boarder",prompt="Border size/thickness:\n default is [5]"))
            qr_borders_picked = True
        except TypeError:
            screen.textinput(title="⚠️Invalid Input⚠️", prompt="Please enter a number, press [OK] to try again :)")
    #X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
    # X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
    qr_back_color_picked = False
    qr_fill_color_picked = False
    ########################
    while not qr_back_color_picked:
        qr_back_color = screen.textinput(title="QR-Background", prompt="Pick QR-Background color:\n default is [white]").lower()
        if qr_back_color in available_colors:
            qr_back_color_picked = True
            #x-x-x-x-x-x-x-x-x-x-x#
            if qr_back_color == "black":
                screen.bgcolor(qr_back_color)
            if qr_back_color == "white":
                screen.bgcolor(qr_back_color)
        else:
            screen.textinput(title="⚠️Color Unavailable⚠️", prompt="Please enter another color, press [OK] to try again :)")
            qr_back_color_picked = False
    #--------------------------
    while not qr_fill_color_picked:
        qr_fill_color = screen.textinput(title="QR-Fill", prompt="Pick QR-Fill color\n default is [black]").lower()
        if qr_fill_color in available_colors:
            qr_fill_color_picked = True
        else:
            screen.textinput(title="⚠️Color Unavailable⚠️", prompt="Please enter another color, press [OK] to try again :)")
            qr_fill_color_picked = False

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
else:
    qr_size = 10
    qr_borders = 4
    #
    qr_back_color = "white"
    screen.bgcolor(qr_back_color)
    #
    qr_fill_color= "black"



#======================================================================================================QR-Code creation
#___________________________________class & details
qr_code_manager = qrcode.QRCode(
    #########
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=qr_size,
    border=qr_borders,
)
#___________________________________adding info
qr_code_manager.add_data(data)
qr_code_manager.make(fit=True)

#___________________________________Generating the QR-CODE image
final_qr_img = qr_code_manager.make_image(fill_color=qr_fill_color, back_color=qr_back_color)
final_qr_img.save("QR_Code.png")
#
time.sleep(1)
#
try:
    img = Image.open('QR_Code.png')
    img.show()
    # time.sleep(1)
    #-------------
    if qr_back_color == "black":
        load_icon.start_loading_screen(0, 4, "white")
    if qr_back_color == "white":
        load_icon.start_loading_screen(0, 4, "black")
    if qr_back_color != "white" and qr_back_color != "black" :
        load_icon.start_loading_screen(0, 4, "grey")
    # print("DONE")#DEBUG
    #-------------

except IOError:
    load_icon.start_loading_screen(0, 4, "white")
    print("An error occurred while trying to open the image.")

#======================================================================
screen.mainloop()
