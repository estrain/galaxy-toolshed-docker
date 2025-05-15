# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747318263.719536
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/base.mako'
_template_uri = '/base.mako'
_source_encoding = 'utf-8'
_exports = ['title', 'init', 'stylesheets', 'javascripts', 'javascript_entry', 'javascript_app', 'metas']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('galaxy_client', context._clean_inheritance_tokens(), templateuri='/galaxy_client_app.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'galaxy_client')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        n_ = context.get('n_', UNDEFINED)
        next = context.get('next', UNDEFINED)
        app = context.get('app', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        self.js_app = None 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        _=n_ 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['_'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!DOCTYPE HTML>\n<html>\n    <!--base.mako-->\n    ')
        __M_writer(str(self.init()))
        __M_writer('\n    <head>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n\n        <title>\n            Galaxy\n')
        if app.config.brand:
            __M_writer('            | ')
            __M_writer(str(app.config.brand))
            __M_writer('\n')
        __M_writer('            | ')
        __M_writer(str(self.title()))
        __M_writer('\n        </title>\n\n')
        __M_writer('        <link rel="index" href="')
        __M_writer(str( h.url_for( '/' ) ))
        __M_writer('"/>\n\n        ')
        __M_writer(str(self.metas()))
        __M_writer('\n        ')
        __M_writer(str(self.stylesheets()))
        __M_writer('\n        ')
        __M_writer(str(self.javascripts()))
        __M_writer('\n        ')
        __M_writer(str(self.javascript_app()))
        __M_writer('\n    </head>\n    <body class="inbound">\n        ')
        __M_writer(str(next.body()))
        __M_writer('\n    </body>\n</html>\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(h.dist_css('base')))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('    ')
        __M_writer(str(h.dist_js(
        'libs.bundled',
    )))
        __M_writer('\n    ')
        __M_writer(str(self.javascript_entry()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(h.dist_js('toolshed.bundled')))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_app(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        form_input_auto_focus = context.get('form_input_auto_focus', UNDEFINED)
        self = context.get('self', UNDEFINED)
        galaxy_client = _mako_get_namespace(context, 'galaxy_client')
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        __M_writer(str( galaxy_client.load( app=self.js_app ) ))
        __M_writer('\n    ')
        __M_writer(str( galaxy_client.config_sentry( app=self.js_app ) ))
        __M_writer('\n')
        if self.js_app and self.js_app.config and self.js_app.config.ga_code:
            __M_writer('        ')
            __M_writer(str( galaxy_client.config_google_analytics(self.js_app.config.ga_code) ))
            __M_writer('\n')
        if self.js_app and self.js_app.config and self.js_app.config.plausible_server and self.js_app.config.plausible_domain:
            __M_writer('        ')
            __M_writer(str( galaxy_client.config_plausible_analytics(self.js_app.config.plausible_server, self.js_app.config.plausible_domain) ))
            __M_writer('\n')
        if self.js_app and self.js_app.config and self.js_app.config.matomo_server and self.js_app.config.matomo_site_id:
            __M_writer('        ')
            __M_writer(str( galaxy_client.config_matomo_analytics(self.js_app.config.matomo_server, self.js_app.config.matomo_site_id) ))
            __M_writer('\n')
        __M_writer('\n')
        if not form_input_auto_focus is UNDEFINED and form_input_auto_focus:
            __M_writer('        <script type="text/javascript">\n            // Auto Focus on first item on form\n            config.addInitialization(function() {\n                console.log("base.mako", "auto focus on first item on form");\n                if ( $("*:focus").html() == null ) {\n                    $(":input:not([type=hidden]):visible:enabled:first").focus();\n                }\n            });\n        </script>\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_metas(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/base.mako", "uri": "/base.mako", "source_encoding": "utf-8", "line_map": {"23": 1, "26": 0, "36": 1, "37": 2, "38": 3, "41": 2, "42": 4, "43": 5, "46": 4, "47": 8, "48": 8, "49": 14, "50": 15, "51": 15, "52": 15, "53": 17, "54": 17, "55": 17, "56": 22, "57": 22, "58": 22, "59": 24, "60": 24, "61": 25, "62": 25, "63": 26, "64": 26, "65": 27, "66": 27, "67": 30, "68": 30, "69": 35, "70": 38, "71": 43, "72": 52, "73": 56, "74": 84, "75": 87, "81": 35, "90": 38, "99": 41, "104": 41, "105": 42, "106": 42, "112": 46, "118": 46, "119": 48, "120": 48, "123": 50, "124": 51, "125": 51, "131": 54, "136": 54, "137": 55, "138": 55, "144": 58, "151": 58, "152": 60, "153": 60, "154": 61, "155": 61, "156": 62, "157": 63, "158": 63, "159": 63, "160": 65, "161": 66, "162": 66, "163": 66, "164": 68, "165": 69, "166": 69, "167": 69, "168": 71, "169": 72, "170": 73, "171": 83, "177": 87, "186": 177}}
__M_END_METADATA
"""
