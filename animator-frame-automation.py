import bpy

class AddExposure(bpy.types.Operator): 
    bl_idname = "gpencil.exposure_add"
    bl_label = "Add 1 Exposure To Selected Frames"
    bl_options = {'REGISTER','UNDO'}

    def execute(self,context):
        if bpy.context.active_object.type == 'GPENCIL':
            gpencil = bpy.context.active_object
            for lay in gpencil.data.layers:
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
        try:
            if bpy.context.active_object.type == 'GPENCIL':
                gpencil = bpy.context.active_object
                for lay in gpencil.data.layers:
                    shiftvalue = 0
                    for i in range(0,len(lay.frames)-1): 
                        lay.frames[i].frame_number -= shiftvalue
                        if (lay.frames[i].select == True) and (lay.frames[i].frame_number < lay.frames[i+1].frame_number - (shiftvalue +1)):
                            shiftvalue += 1
                    lay.frames[len(lay.frames)-1].frame_number -= shiftvalue
        except IndexError:
            print("Index Error Ignored")
        return {'FINISHED'}



def register():
    bpy.utils.register_class(AddExposure)
    bpy.utils.register_class(RemoveExposure)


def unregister():
    bpy.utils.unregister_class(AddExposure)
    bpy.utils.unregister_class(RemoveExposure)


if __name__ == "__main__":
    register()
