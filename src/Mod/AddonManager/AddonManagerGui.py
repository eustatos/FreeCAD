# -*- coding: utf-8 -*-
# FreeCAD tools of the AddonManager workbench
# (c) 2001 Juergen Riegel
# License LGPL

import FreeCAD, FreeCADGui

class CmdHelloWorld:
    def Activated(self):
        FreeCAD.Console.PrintMessage("Hello, World!\n")
    def IsActive(self):
        return True
    def GetResources(self):
        return {'Pixmap': 'freecad', 'MenuText': 'Hello World', 'ToolTip': 'Print Hello World'}

FreeCADGui.addCommand('AddonManager_HelloWorld', CmdHelloWorld())
