bl_info = {
    "name":"Easy Frame",
    "category":"Grease Pencil",
    "blender":(2,80,0),
    "version":(1,0,0),
    "author":"Mathieu Monfort",
    "description":"2D Animation add on for Grease Pencil, adding features for natural frame manipulation" 
}



import bpy
import threading


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

def init():
    print('timer end reached')
    hasExpAddHotkey = False
    hasExpRemHotkey = False
    for hotkey in bpy.data.window_managers[0].keyconfigs.active.keymaps['Dopesheet'].keymap_items:
        if hotkey.idname == 'gpencil.exposure_add':
            hasExpAddHotkey = True
        if hotkey.idname == 'gpencil.exposure_remove':
            hasExpRemHotkey = True
        
    if hasExpAddHotkey == False :
        bpy.data.window_managers[0].keyconfigs.active.keymaps['Dopesheet'].keymap_items.new('gpencil.exposure_add',value='PRESS',type='NUMPAD_PLUS',ctrl=False,alt=False,shift=True,oskey=False)
    if hasExpRemHotkey == False :
        bpy.data.window_managers[0].keyconfigs.active.keymaps['Dopesheet'].keymap_items.new('gpencil.exposure_remove',value='PRESS',type='NUMPAD_MINUS',ctrl=False,alt=False,shift=True,oskey=False)


def register():
    bpy.utils.register_class(AddExposure)
    bpy.utils.register_class(RemoveExposure)

    timer = threading.Timer(0.1,init)
    timer.start()
    print('launching timer')

def unregister():
    bpy.utils.unregister_class(AddExposure)
    bpy.utils.unregister_class(RemoveExposure)

        
if __name__ == "__main__":
    register()
