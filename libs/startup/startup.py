import libs.startup.update as update
class startup:
   def startup():
       print("Checking for updates...", end=" ")
       if update("Check")==0:
           print("[ DONE ]")
       else:
          print
