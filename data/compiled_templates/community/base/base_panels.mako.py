# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747318263.7368233
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/base/base_panels.mako'
_template_uri = '/base/base_panels.mako'
_source_encoding = 'utf-8'
_exports = ['init', 'stylesheets', 'javascripts', 'javascript_entry', 'javascript_app', 'late_javascripts', 'masthead', 'overlay']


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
        app = context.get('app', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE HTML>\n')
        __M_writer('\n\n')

        self.has_left_panel = hasattr( self, 'left_panel' )
        self.message_box_visible = app.config.message_box_visible
        self.show_inactivity_warning = False
        self.overlay_visible=False
        self.active_view=None
        self.body_class=""
        self.require_javascript=False
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('<html>\n    <!-- toolshed webapp base_panels.mako-->\n    ')
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
        __M_writer(str(self.stylesheets()))
        __M_writer('\n\n')
        __M_writer('        ')
        __M_writer(str(self.javascripts()))
        __M_writer('\n        ')
        __M_writer(str(self.javascript_app()))
        __M_writer('\n\n    </head>\n\n    ')

        body_class = self.body_class
        if self.message_box_visible:
            body_class += " has-message-box"
        if self.show_inactivity_warning:
            body_class += " has-inactivity-box"
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['body_class'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n\n    <body scroll="no" class="full-content ')
        __M_writer(str(body_class))
        __M_writer('">\n')
        if self.require_javascript:
            __M_writer('            <noscript>\n                <div class="overlay overlay-background">\n                    <div class="modal dialog-box" border="0">\n                        <div class="modal-header"><h3 class="title">Javascript Required</h3></div>\n                        <div class="modal-body">The Galaxy analysis interface requires a browser with Javascript enabled. <br> Please enable Javascript and refresh this page</div>\n                    </div>\n                </div>\n            </noscript>\n')
        __M_writer('        <div id="everything">\n\n')
        __M_writer('            <div id="background"></div>\n\n')
        __M_writer('            <div>\n                ')
        __M_writer(str(self.masthead()))
        __M_writer('\n            </div>\n\n')
        if self.message_box_visible:
            __M_writer('                <div id="messagebox" class="panel-')
            __M_writer(str(app.config.message_box_class))
            __M_writer('-message" style="display:block">\n                    ')
            __M_writer(str(app.config.message_box_content))
            __M_writer('\n                </div>\n')
        __M_writer('\n')
        if self.show_inactivity_warning:
            __M_writer('                <div id="inactivebox" class="panel-warning-message">\n                    ')
            __M_writer(str(app.config.inactivity_box_content))
            __M_writer(' <a href="')
            __M_writer(str(h.url_for( controller='user', action='resend_verification' )))
            __M_writer('">Resend verification.</a>\n                </div>\n')
        __M_writer('\n            ')
        __M_writer(str(self.overlay(visible=self.overlay_visible)))
        __M_writer('\n\n            <div id="columns" class="d-flex">\n')
        if self.has_left_panel:
            __M_writer('                    <div id="left">\n                        ')
            __M_writer(str(self.left_panel()))
            __M_writer('\n                    </div>\n')
        __M_writer('                <div id="center" class="inbound">\n                    ')
        __M_writer(str(self.center_panel()))
        __M_writer('\n                </div>\n            </div>\n        </div>\n\n        <div id=\'dd-helper\' style="display: none;"></div>\n')
        __M_writer('        ')
        __M_writer(str(self.late_javascripts()))
        __M_writer('\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <!--- base/base_panels.mako stylesheets() -->\n    ')
        __M_writer(str(h.dist_css(
        'base'
    )))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def javascript_entry():
            return render_javascript_entry(context)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <!--- base/base_panels.mako javascripts() -->\n    ')
        __M_writer(str(h.dist_js(
        'libs.bundled',
    )))
        __M_writer('\n    ')
        __M_writer(str( javascript_entry() ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_entry(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <!-- base/base_panels.mako javascript_entry -->\n    ')
        __M_writer(str( h.dist_js('toolshed.bundled')))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_app(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        galaxy_client = _mako_get_namespace(context, 'galaxy_client')
        __M_writer = context.writer()
        __M_writer('\n    <!--- base/base_panels.mako javascript_app() -->\n    ')
        __M_writer(str( galaxy_client.load() ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        t = context.get('t', UNDEFINED)
        app = context.get('app', UNDEFINED)
        galaxy_client = _mako_get_namespace(context, 'galaxy_client')
        __M_writer = context.writer()
        __M_writer('\n    <!--- base/base_panels.mako late_javascripts() -->\n\n')
        if t.webapp.name == 'galaxy' and app.config.ga_code:
            __M_writer('        ')
            __M_writer(str(galaxy_client.config_google_analytics(app.config.ga_code)))
            __M_writer('\n')
        if t.webapp.name == 'galaxy' and app.config.plausible_server and app.config.plausible_domain:
            __M_writer('        ')
            __M_writer(str( galaxy_client.config_plausible_analytics(app.config.plausible_server, app.config.plausible_domain) ))
            __M_writer('\n')
        if t.webapp.name == 'galaxy' and app.config.matomo_server and app.config.matomo_site_id:
            __M_writer('        ')
            __M_writer(str( galaxy_client.config_matomo_analytics(app.config.matomo_server, app.config.matomo_site_id) ))
            __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_overlay(context,title='',content='',visible=False):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer('\n    ')
        __M_writer('\n\n    ')

        if visible:
            display = "style='display: block;'"
            overlay_class = "in"
        else:
            display = "style='display: none;'"
            overlay_class = ""
        
        
        __M_writer('\n\n    <div id="top-modal" class="modal ')
        __M_writer(str(overlay_class))
        __M_writer('" ')
        __M_writer(str(display))
        __M_writer('>\n        <div id="top-modal-backdrop" class="modal-backdrop fade ')
        __M_writer(str(overlay_class))
        __M_writer('" style="z-index: -1"></div>\n        <div id="top-modal-dialog" class="modal-dialog">\n            <div class="modal-content">\n                <div class="modal-header">\n                    <button type=\'button\' class=\'close\' style="display: none;">&times;</button>\n                    <h4 class=\'title\'>')
        __M_writer(str(title))
        __M_writer('</h4>\n                </div>\n                <div class="modal-body">')
        __M_writer(str(content))
        __M_writer('</div>\n                <div class="modal-footer">\n                    <div class="buttons" style="float: right;"></div>\n                    <div class="extra_buttons" style=""></div>\n                    <div style="clear: both;"></div>\n                </div>\n            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/base/base_panels.mako", "uri": "/base/base_panels.mako", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 0, "35": 1, "36": 2, "37": 4, "38": 5, "39": 6, "40": 7, "41": 8, "42": 9, "43": 10, "44": 11, "45": 12, "46": 13, "49": 12, "50": 16, "51": 24, "52": 34, "53": 39, "54": 44, "55": 60, "56": 65, "57": 97, "58": 100, "59": 102, "60": 102, "61": 108, "62": 109, "63": 109, "64": 109, "65": 111, "66": 111, "67": 111, "68": 115, "69": 115, "70": 115, "71": 117, "72": 117, "73": 124, "74": 124, "75": 124, "76": 125, "77": 125, "78": 129, "79": 130, "80": 131, "81": 132, "82": 133, "83": 134, "84": 135, "85": 136, "88": 135, "89": 138, "90": 138, "91": 139, "92": 140, "93": 149, "94": 152, "95": 155, "96": 156, "97": 156, "98": 159, "99": 160, "100": 160, "101": 160, "102": 161, "103": 161, "104": 164, "105": 165, "106": 166, "107": 167, "108": 167, "109": 167, "110": 167, "111": 170, "112": 171, "113": 171, "114": 174, "115": 175, "116": 176, "117": 176, "118": 179, "119": 180, "120": 180, "121": 189, "122": 189, "123": 189, "129": 14, "133": 14, "139": 19, "144": 19, "145": 21, "148": 23, "154": 28, "161": 28, "162": 30, "165": 32, "166": 33, "167": 33, "173": 36, "178": 36, "179": 38, "180": 38, "186": 41, "191": 41, "192": 43, "193": 43, "199": 47, "206": 47, "207": 50, "208": 51, "209": 51, "210": 51, "211": 53, "212": 54, "213": 54, "214": 54, "215": 56, "216": 57, "217": 57, "218": 57, "219": 59, "225": 63, "229": 63, "235": 67, "239": 67, "240": 68, "241": 69, "242": 71, "243": 72, "244": 73, "245": 74, "246": 75, "247": 76, "248": 77, "249": 78, "250": 79, "251": 78, "252": 80, "253": 80, "254": 80, "255": 80, "256": 81, "257": 81, "258": 86, "259": 86, "260": 88, "261": 88, "267": 261}}
__M_END_METADATA
"""
