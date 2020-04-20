import sys

import dbus

session_bus = dbus.SessionBus()

## get other arguments than script name
args = sys.argv[1:]


if args:
    message = args[0]
else:
    message = "Generic message from client"

try:
    proxy_greeter = session_bus.get_object("org.heikki.HelloWorld.Hello", "/GreeterObject")
except dbus.DbusException as e:
    print("Error from client!")
else:
    greeter_iface = dbus.Interface(proxy_greeter, "org.heikki.HelloWorld.Greet")
    print(greeter_iface.getProperties())
    quit_iface = dbus.Interface(proxy_greeter, "org.heikki.HelloWorld.Quit")
    if args[0] == "quit":
        quit_iface.quit()
    else:
        greeter_iface.echo(message)


