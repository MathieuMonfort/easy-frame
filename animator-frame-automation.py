import bpy

class AddExposure(bpy.types.Operator): 
    bl_idname = "gpencil.exposure_add"
    bl_label = "Add 1 Exposure To Selected Frames"
    bl_options = {'REGISTER','UNDO'}

    def execute(self,context):
        if bpy.context.active_object.type == 'GPENCIL':
            gpencil = bpy.context.active_object
            for lay in gpencil.data.layers:
                #if lay.select == True:
                activeFrameCount = 0
                for frame in lay.frames:
                    if frame.select == True:
                        activeFrameCount = activeFrameCount + 1
                for frame in reversed(lay.frames):
                    if frame.select == True:
                        activeFrameCount = activeFrameCount - 1 
                    frame.frame_number = frame.frame_number + activeFrameCount
            return {'FINISHED'}

class RemoveExposure(bpy.types.Operator):
    bl_idname = "gpencil.exposure_remove"
    bl_label = "Remove 1 Exposure To Selected Frames"
    bl_options = {'REGISTER','UNDO'}

    def execute(self,context):
        if bpy.context.active_object.type == 'GPENCIL':
            gpencil = bpy.context.active_object
            for lay in gpencil.data.layers:
                shiftvalue = 0
                for frame in lay.frames:
                    frame.frame_number = frame.frame_number - shiftvalue
                    if frame.select == True:
                        shiftvalue = shiftvalue + 1
            return {'FINISHED'}


def register():
    bpy.utils.register_class(AddExposure)
    bpy.utils.register_class(RemoveExposure)


def unregister():
    bpy.utils.unregister_class(AddExposure)
    bpy.utils.unregister_class(RemoveExposure)


if __name__ == "__main__":
    register()
