import bpy
from bpy.props import *
from ... events import executionCodeChanged
from ... base_types.node import AnimationNode

items = [("ROUND", "Round", ""),
         ("CEILING", "Ceiling", "The smallest integer that is larger than the input (4.3 -> 5)"),
         ("FLOOR", "Floor", "The largest integer that is smaller than the input (5.8 -> 5)")]

class FloatToIntegerNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_FloatToIntegerNode"
    bl_label = "Float to Integer"

    type = EnumProperty(name = "Conversion Type", items = items, default = "FLOOR", update = executionCodeChanged)

    def create(self):
        self.inputs.new("an_FloatSocket", "Float", "float")
        self.outputs.new("an_IntegerSocket", "Integer", "integer")

    def drawLabel(self):
        return "({}) Float to Integer".format(self.type.capitalize())

    def drawAdvanced(self, layout):
        layout.prop(self, "type", text = "")

    def getExecutionCode(self):
        if self.type == "ROUND": return "integer = int(round(float))"
        if self.type == "CEILING": return "integer = int(math.ceil(float))"
        if self.type == "FLOOR": return "integer = int(math.floor(float))"

    def getUsedModules(self):
        return ["math"]
