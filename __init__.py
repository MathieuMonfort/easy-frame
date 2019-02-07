bl_info = {
    "name":"Easy Frame",
    "category":"Grease Pencil",
    "blender":(2,80,0),
    "version":(1,0,2),
    "author":"Mathieu Monfort",
    "description":"2D Animation add on for Grease Pencil, adding features for natural frame manipulation" 
}



import bpy
import threading
import sys
import importlib


modulesNames = ['animator-frame-automation']

modulesFullNames = []
for currentModuleName in modulesNames:
    modulesFullNames.append('{}.{}'.format(__name__, currentModuleName))
	
 
for currentModuleFullName in modulesFullNames:
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)



def init():
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
    for currentModuleName in modulesFullNames:
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()
    timer = threading.Timer(0.1,init)
    timer.start()

def unregister():
    for currentModuleName in modulesFullNames:
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()
        
if __name__ == "__main__":
    register()
