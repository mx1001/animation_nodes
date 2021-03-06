import bpy
from bpy.props import *
from ... base_types.node import AnimationNode

class DebugNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_DebugNode"
    bl_label = "Debug"

    text = StringProperty()
    printData = BoolProperty(name = "Print to Console", description = "Can be very slow when used often")

    def create(self):
        socket = self.inputs.new("an_GenericSocket", "Data", "data")
        socket.display.text = True
        socket.text = "None"

    def drawAdvanced(self, layout):
        layout.prop(self, "printData")

    def execute(self, data):
        if isinstance(data, float): text = str(round(data, 5))
        else: text = str(data)

        self.inputs[0].text = text
        if self.printData: print(text)
