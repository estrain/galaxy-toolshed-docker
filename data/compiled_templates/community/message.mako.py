# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747339871.8153884
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/message.mako'
_template_uri = '/message.mako'
_source_encoding = 'utf-8'
_exports = ['init', 'javascript_app', 'center_panel', 'body', 'render_msg']



from galaxy.util.sanitize_html import sanitize_html

def inherit(context):
    if context.get('use_panels'):
        if context.get('webapp'):
            app_name = context.get('webapp')
        elif context.get('app'):
            app_name = context.get('app').name
        else:
            app_name = 'galaxy'
        return '/webapps/%s/base_panels.mako' % app_name
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7f0892ec8ca0', context._clean_inheritance_tokens(), templateuri='/refresh_frames.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7f0892ec8ca0')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f0892ec8ca0')._populate(_import_ns, ['handle_refresh_frames'])
        n_ = _import_ns.get('n_', context.get('n_', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f0892ec8ca0')._populate(_import_ns, ['handle_refresh_frames'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        active_view = _import_ns.get('active_view', context.get('active_view', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')

        self.has_left_panel=False
        self.active_view=active_view
        self.message_box_visible=False
        
        
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_app(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f0892ec8ca0')._populate(_import_ns, ['handle_refresh_frames'])
        handle_refresh_frames = _import_ns.get('handle_refresh_frames', context.get('handle_refresh_frames', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <!-- message.mako javascript_app() -->\n    ')
        __M_writer(str(parent.javascript_app()))
        __M_writer('\n    ')
        __M_writer(str(handle_refresh_frames()))
        __M_writer('\n    <script type="text/javascript">\n        config.addInitialization(function() {\n            if (parent.handle_minwidth_hint) {\n                parent.handle_minwidth_hint(-1);\n            }\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f0892ec8ca0')._populate(_import_ns, ['handle_refresh_frames'])
        def render_msg(msg,status='done'):
            return render_render_msg(context,msg,status)
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(render_msg( message, status )))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f0892ec8ca0')._populate(_import_ns, ['handle_refresh_frames'])
        def render_msg(msg,status='done'):
            return render_render_msg(context,msg,status)
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(render_msg( message, status )))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_msg(context,msg,status='done'):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7f0892ec8ca0')._populate(_import_ns, ['handle_refresh_frames'])
        __M_writer = context.writer()
        __M_writer('\n    ')

        if status == "done":
            status = "success"
        elif status == "error":
            status = "danger"
        if status not in ("danger", "info", "success", "warning"):
            status = "info"
            
        
        __M_writer('\n    <div class="message mt-2 alert alert-')
        __M_writer(str(status))
        __M_writer('">')
        __M_writer(str(sanitize_html(msg)))
        __M_writer('</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/message.mako", "uri": "/message.mako", "source_encoding": "utf-8", "line_map": {"16": 1, "17": 2, "18": 3, "19": 4, "20": 5, "21": 6, "22": 7, "23": 8, "24": 9, "25": 10, "26": 11, "27": 12, "28": 13, "29": 14, "30": 15, "31": 16, "39": 18, "45": 0, "53": 15, "54": 16, "55": 18, "56": 20, "57": 21, "60": 20, "61": 28, "62": 41, "63": 46, "64": 49, "65": 53, "66": 66, "72": 22, "80": 22, "81": 23, "82": 24, "83": 25, "84": 26, "85": 27, "86": 28, "87": 27, "93": 30, "101": 30, "102": 32, "103": 32, "104": 33, "105": 33, "111": 47, "121": 47, "122": 48, "123": 48, "129": 51, "139": 51, "140": 52, "141": 52, "147": 56, "153": 56, "154": 57, "155": 58, "156": 59, "157": 60, "158": 61, "159": 62, "160": 63, "161": 64, "162": 65, "163": 64, "164": 65, "165": 65, "166": 65, "167": 65, "173": 167}}
__M_END_METADATA
"""
