# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747339871.8234925
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/refresh_frames.mako'
_template_uri = '/refresh_frames.mako'
_source_encoding = 'utf-8'
_exports = ['handle_refresh_frames']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_handle_refresh_frames(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        refresh_frames = context.get('refresh_frames', UNDEFINED)
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        app = context.get('app', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('    ')
        if not refresh_frames: return '' 
        
        __M_writer('\n\n    <script type="text/javascript">\n\n        // TODO: I hate that we have a random globally-defined state update\n        // function here but since we\'re about to rewrite the app container,\n        // I\'m not sure it\'s worth the headache to refactor this\n\n        function user_changed(user_email, is_admin) {\n            if ( user_email ) {\n                $(".loggedin-only").show();\n                $(".loggedout-only").hide();\n                $("#user-email").text( user_email );\n                if ( is_admin ) {\n                    $(".admin-only").show();\n                }\n            } else {\n                $(".loggedin-only").hide();\n                $(".loggedout-only").show();\n                $(".admin-only").hide();\n            }\n        }\n\n')
        if 'everything' in refresh_frames:
            __M_writer('            config.addInitialization(function() {\n                var destination = "')
            __M_writer(str(h.url_for( controller='root' )))
            __M_writer('";\n                console.log("refresh_frames.mako, refresh everything", destination);\n                parent.location.href = destination;\n            });\n')
        __M_writer('\n')
        if 'masthead' in refresh_frames:
            __M_writer('    \n            config.addInitialization(function(galaxy, config) {\n                console.log("refresh_frames.mako, refresh masthead");\n                var userEmail = "')
            __M_writer(filters.html_escape(str(trans.user.email )))
            __M_writer('";\n                var isAdmin = ')
            __M_writer(str(h.to_js_bool(app.config.is_admin_user( trans.user))))
            __M_writer(';\n                if (parent.user_changed) {\n')
            if trans.user:
                __M_writer('                        parent.user_changed(userEmail, isAdmin);\n')
            else:
                __M_writer('                        parent.user_changed( null, false );\n')
            __M_writer('                }\n            });\n')
        __M_writer('\n')
        if 'history' in refresh_frames:
            __M_writer('            config.addInitialization(function(galaxy) {\n                console.log("refresh_frames.mako, refresh history");\n                if(galaxy.currHistoryPanel){\n                    galaxy.currHistoryPanel.loadCurrentHistory();\n                }\n            })\n')
        __M_writer('\n')
        if 'tools' in refresh_frames:
            __M_writer('            config.addInitialization(function(galaxy) {\n                console.log("refresh_frames.mako, refresh tools");\n                if ( parent.frames && galaxy.toolPanel ) {\n                    // FIXME: refreshing the tool menu does not work with new JS-based approach,\n                    // but refreshing the tool menu is not used right now, either.\n                    if (parent.force_left_panel) {\n                        parent.force_left_panel(\'show\');\n                    }\n                }\n            });\n')
        __M_writer('\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/refresh_frames.mako", "uri": "/refresh_frames.mako", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 76, "27": 2, "35": 2, "36": 5, "37": 5, "38": 6, "39": 5, "40": 28, "41": 29, "42": 30, "43": 30, "44": 35, "45": 36, "46": 38, "47": 41, "48": 41, "49": 42, "50": 42, "51": 44, "52": 45, "53": 46, "54": 47, "55": 49, "56": 52, "57": 53, "58": 54, "59": 61, "60": 62, "61": 63, "62": 74, "68": 62}}
__M_END_METADATA
"""
