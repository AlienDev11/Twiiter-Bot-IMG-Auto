import pyinotify
import TwitterBot

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print("CREATE event:", event.pathname)
        TwitterBot.ReRun()

def CheckForChanges():
    wm = pyinotify.WatchManager()
    wm.add_watch("./",pyinotify.ALL_EVENTS,rec=True)

    eh = MyEventHandler()

    Notifier = pyinotify.Notifier(wm,eh)
    Notifier.loop()

if __name__ == "__main__":
    CheckForChanges()
