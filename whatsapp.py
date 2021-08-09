import webbrowser as wb
import pyautogui as p
from urllib.parse import quote
import time
from platform import system
import os
from PIL import Image


#file extentions
pn = ["PNG","png"]
jp = ["jpg","jpeg","JPG","JPEG"]


def close_tab():
    p.hotkey("ctrl","w")


def single_sms():
    '''
    Function to send single sms
    '''
    phone = str(input("[*]Enter phone no.(with country code): "))
    msg = str(input("[*]Enter full message here: "))
    parsed_message = quote(msg)

    #open whatsapp web
    wb.open("https://web.whatsapp.com/send?phone="+phone+"&text="+parsed_message)
    time.sleep(6) #time to load
    
    width,height=p.size()
    
    #click in the message box
    p.click(width/2,height/2)
    time.sleep(3)

    #press ennter to send
    p.press('enter')

    time.sleep(3)

    #close the current tab
    close_tab()


def single_image():
    '''
    Sending Image Function we gonna copy the image in clip board and then paste it in whatsapp
    '''

    phone = str(input("[*]Enter phone no.(with country code): "))
    caption = str(input("[*]Enter caption: "))
    parsed_caption = quote(caption)
    full_path = str(input("[*]Enter full image path: "))
    if not os.path.exists(full_path):
        print("[*]Wrong path")
        exit()
    wb.open('https://web.whatsapp.com/send?phone=' + phone + '&text=' + caption)
    time.sleep(6) #to get it load
    
    '''
    for linux
    '''
    if full_path.split("/")[-1].split(".")[1] in pn:
        os.system("xclip -selection clipboard -target image/png -i " + full_path)
    elif full_path.split("/")[-1].split(".")[1] in jp:
    	'''
    	convert it in png and then use it 
    	'''
    	file_name = full_path.split("/")[-1].split(".")[0]
    	image_path = os.getcwd()+"/"+file_name+".png"
	#image_path = os.getcwd()+"/"+file_name+".png"    	
    	img1 = Image.open(full_path)
    	img1.save(image_path)
    	os.system("xclip -selection clipboard -target image/png -i " + image_path)
    	
 
        
    else:
        print("[*]Wrong format")
        exit()
    #to paste the image
    p.hotkey("ctrl","v")
    time.sleep(4)
    p.press('enter')
    time.sleep(11) # give it time to load
    #close the tab
    close_tab()

def bulk_sms():

	'''
	Function to send same message to mulitple contacts
	'''

	phones = []
	with open('contacts.txt','r') as f:

		for line in f.readlines():
			number = line.strip("\n")
			phones.append(number)
	f.close()
	msg = str(input("[*]Enter message here: "))
	parsed_message = quote(msg)
	for phone in phones:
		wb.open("https://web.whatsapp.com/send?phone="+phone+"&text="+parsed_message)
		
		time.sleep(6) # time to get it load
		width,height = p.size()
		
		#click in the message box
		p.click(width/2,height/2)
		time.sleep(3)
		
		#press enter to send
		p.press('enter')
		
		time.sleep(3)
		
		#close current tab
		close_tab()
		time.sleep(7)
    		
	
def bulk_img():
	'''
	Function to send same image multiple ppl
	'''
	phones=[]
	with open('contacts.txt','r') as f:
		for line in f.readlines():
			number =line.strip("\n")
			phones.append(number)
	f.close()
	caption = str(input("[*]Enter caption: "))
	full_path = str(input("[*]Enter full image path: "))
	if not os.path.exists(full_path):
		print("[*]Wrong path")
		exit()
	#convert it if needed and load it in clip board
	if full_path.split("/")[-1].split(".")[1] in jp:
		file_name = full_path.split("/")[-1].split(".")[0]
		image_path = os.getcwd()+"/"+file_name+".png"
		img1 = Image.open(full_path)
		img1.save(image_path)
		full_path = image_path
	'''
	for linux
	'''
	os.system("xclip -selection clipboard -target image/png -i " + full_path)
		
		
	for phone in phones:
		
		wb.open('https://web.whatsapp.com/send?phone=' + phone + '&text=' + caption)
		time.sleep(8) # to get it load
		
		#paste it
		p.hotkey("ctrl","v")
		
		time.sleep(4)
		
		#press enter
		p.press('enter')
		time.sleep(12) #time to send it
		
		close_tab()
		time.sleep(9)
		
		
			
		
		   

def print_menu():
    print("[*]Press 1 to send single text")
    print("[*]Press 2 to send an image")
    print("[*]Press 3 to send bulk message")
    print("[*]Press 4 to send bulk image")
    
    op = int(input("[*]Enter option:- "))

    if op == 1:
        single_sms()
    if op == 2:
        single_image()
    if op == 3:
        bulk_sms()
    if op== 4:
        bulk_img()
    

if __name__ == "__main__":
    print_menu()
