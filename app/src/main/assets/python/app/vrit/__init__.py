from rubicon.java import JavaClass, JavaInterface

IPythonApp = JavaInterface('org/beeware/android/IPythonApp')

class Application(IPythonApp):
    def onCreate(self):
        print('called Python onCreate()')

    def onStart(self):
        print('called Python onStart()')

    def onResume(self):
        print('called Python onResume()')