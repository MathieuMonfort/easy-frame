# Changelog     

## [1.0.3]
- Folder restructuration.

## [1.0.2]
### Modified 
- Corrected Operator (bpy.ops.gpencil.exposure_remove) So it always leaves at least 1 exposure to every frame.

## [1.0.1]
### Modified
- Modified Structure for Multiple files implementation.

## [1.0.0]
### Added 
- Added Operator(bpy.ops.gpencil.exposure_addd) purposed to add 1 Exposure to every selected frame in dopesheet( Exposure is a fraction of a second in animation(in 24fps, 1 exposure is 1/24 of a second)) default hotkey automatically assigned to "SHIFT" + "+" 
- Added Operator(bpy.ops.gpancil.exposure_remove) purposed to remove 1 Exposure to every selected frame in dopesheet. default hotkey automatically assigned to "SHIFT" + "-"