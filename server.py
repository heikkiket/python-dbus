import sys

from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

## This is the greeter object that is being connected through dbus
class Greeter(dbus.service.Object):

    ## Publish echo as service method
    ## @-syntax here is basically just passing this method as a callback
    @dbus.service.method("org.heikki.HelloWorld.Greet", in_signature='s', out_signature='')
    def echo(self, message):
        message = str(message)
        print("Server: Hello World, %r" % message)

    @dbus.service.method("org.heikki.HelloWorld.Quit")
    def quit(self):
        self.mainloop.quit()

DBusGMainLoop(set_as_default=True)

session_bus = dbus.SessionBus()
try:
    name = dbus.service.BusName("org.heikki.HelloWorld.Hello", session_bus, do_not_queue=True)
except dbus.NameExistsException:
    sys.exit('Server is already running.')


greeter = Greeter(session_bus, "/GreeterObject")
loop = GLib.MainLoop()
greeter.mainloop = loop
loop.run()
