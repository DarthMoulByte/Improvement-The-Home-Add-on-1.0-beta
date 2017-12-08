# Blend info
# line 9 | used for warning icon and text in addons panel
bl_info = {
    "name": "My Script",
    "description": "Improvement The Home",
    "author": "DarthMoulByte",
    "version": (0, 1),
    "blender": (2, 7, 0),
    "location": "Properties ",
    "warning": "Beta mo warranty, becarefull",
    "wiki_url": "1millionparanoidtterabytes@gmail.com/https://discordea.net/lack-of-love-tm/"
                "Scripts/My_Script",
    "tracker_url": "unknow",
    "support": "PyrokinesisStudio",
    "category": "Properties"
    }
    
import bpy
from bpy.types import Header

class PROPERTIES_HT_header(Header):
    bl_space_type = 'PROPERTIES'

    def draw(self, context):
        layout = self.layout

        view = context.space_data

        row = layout.row()
        row.template_header()
        row.prop(view, "context", expand=True, icon_only=True)
