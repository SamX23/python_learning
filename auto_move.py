from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json


class HandlerFile(FileSystemEventHandler):
    i = 1

    def file_modified(self, event):
        for filename in os.listdir(track_folder):
            src = destination_folder + '/' + filename
            new_destination = destination_folder + '/' + filename
            os.rename(src, new_destination)


track_folder = '/Users/KFSL/Desktop/folder1/'
destination_folder = '/Users/KFSL/Desktop/folder2/'
handler_event = HandlerFile()
observer = Observer()
observer.schedule(handler_event, track_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

# still not working