# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747339871.8389509
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/webapps/tool_shed/base_panels.mako'
_template_uri = '/webapps/tool_shed/base_panels.mako'
_source_encoding = 'utf-8'
_exports = ['title', 'init', 'javascript_app', 'javascripts', 'masthead']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('galaxy_client', context._clean_inheritance_tokens(), templateuri='/galaxy_client_app.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'galaxy_client')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
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
        __M_writer('Tool Shed')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.init()))
        __M_writer('\n    ')

        self.body_class = "toolshed"
            
        
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascript_app(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.javascript_app()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.javascripts()))
        __M_writer('\n    <script type="text/javascript">\n        config.addInitialization(function() {\n            console.log("toolshed/base_panels.mako", "hardcoded dropdown init");\n\n            // Masthead dropdown menus\n            var $dropdowns = $("#masthead ul.nav > li.dropdown > .dropdown-menu");\n            $("body").on( "click.nav_popups", function( e ) {\n                $dropdowns.hide();\n                $("#dd-helper").hide();\n                // If the target is in the menu, treat normally\n                if ( $(e.target).closest( "#masthead ul.nav > li.dropdown > .dropdown-menu" ).length ) {\n                    return;\n                }\n                // Otherwise, was the click in a tab\n                var $clicked = $(e.target).closest( "#masthead ul.nav > li.dropdown" );\n                if ( $clicked.length ) {\n                    $("#dd-helper").show();\n                    $clicked.children( ".dropdown-menu" ).show();\n                    e.preventDefault();\n                }\n            });\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_masthead(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def tab(id,display,href,target='_parent',visible=True,extra_class='',menu_options=None):
            __M_caller = context.caller_stack._push_frame()
            try:
                self = context.get('self', UNDEFINED)
                len = context.get('len', UNDEFINED)
                __M_writer = context.writer()
                __M_writer('\n                ')

                cls = "nav-item"
                a_cls = "nav-link"
                extra = ""
                if extra_class:
                    cls = extra_class
                if self.active_view == id:
                    cls += " active"
                if menu_options:
                    cls += " dropdown"
                    a_cls += " dropdown-toggle"
                    extra = "<b class='caret'></b>"
                style = ""
                if not visible:
                    style = "display: none;"
                
                
                __M_writer('\n\n                <li class="')
                __M_writer(str(cls))
                __M_writer('" style="')
                __M_writer(str(style))
                __M_writer('">\n                    <a\n')
                if href:
                    __M_writer('                        class="')
                    __M_writer(str(a_cls))
                    __M_writer('" target="')
                    __M_writer(str(target))
                    __M_writer('" href="')
                    __M_writer(str(href))
                    __M_writer('"\n')
                else:
                    __M_writer('                        class="')
                    __M_writer(str(a_cls))
                    __M_writer('"\n')
                if menu_options:
                    __M_writer('                        role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"\n')
                __M_writer('                    >\n                        ')
                __M_writer(str(display))
                __M_writer(str(extra))
                __M_writer('\n                    </a>\n')
                if menu_options:
                    __M_writer('                        <div class="dropdown-menu" aria-labelledby="navbarDropdown">\n')
                    for menu_item in menu_options:
                        if not menu_item:
                            __M_writer('                                    <div class="dropdown-divider"></div>\n')
                        else:
                            if len ( menu_item ) == 1:
                                __M_writer('                                        <a class="dropdown-item" href="javascript:void(0)" role="button">\n                                            ')
                                __M_writer(str(menu_item[0]))
                                __M_writer('\n                                        </a>\n')
                            elif len ( menu_item ) == 2:
                                __M_writer('                                        ')
                                name, link = menu_item 
                                
                                __M_writer('\n                                        <a class="dropdown-item" href="')
                                __M_writer(str(link))
                                __M_writer('">')
                                __M_writer(filters.html_escape(str(name )))
                                __M_writer('</a>\n')
                            else:
                                __M_writer('                                        ')
                                name, link, target = menu_item 
                                
                                __M_writer('\n                                        <a class="dropdown-item" target="')
                                __M_writer(str(target))
                                __M_writer('" href="')
                                __M_writer(str(link))
                                __M_writer('">')
                                __M_writer(filters.html_escape(str(name )))
                                __M_writer('</a>\n')
                    __M_writer('                        </div>\n')
                __M_writer('                </li>\n            ')
                return ''
            finally:
                context.caller_stack._pop_frame()
        app = context.get('app', UNDEFINED)
        galaxy_client = _mako_get_namespace(context, 'galaxy_client')
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if app.config.ga_code:
            __M_writer('        ')
            __M_writer(str( galaxy_client.config_google_analytics(app.config.ga_code)))
            __M_writer('\n')
        if app.config.plausible_server and app.config.plausible_domain:
            __M_writer('        ')
            __M_writer(str( galaxy_client.config_plausible_analytics(app.config.plausible_server, app.config.plausible_domain) ))
            __M_writer('\n')
        if app.config.matomo_server:
            __M_writer('        ')
            __M_writer(str( galaxy_client.config_matomo_analytics(app.config.matomo_server) ))
            __M_writer('\n')
        __M_writer('\n')
        __M_writer('    <nav id="masthead" class="masthead-simple navbar navbar-expand navbar-fixed-top justify-content-center navbar-dark">\n\n')
        __M_writer('        <a href="')
        __M_writer(str(h.url_for( app.config.get( 'logo_url', '/' ) )))
        __M_writer('" aria-label="homepage" class="navbar-brand">\n            <img alt="logo" class="navbar-brand-image" src="')
        __M_writer(str(h.url_for('/static/favicon.svg')))
        __M_writer('">\n            <span class="navbar-brand-title">\n                Tool Shed\n')
        if app.config.brand:
            __M_writer('                    / ')
            __M_writer(str(app.config.brand))
            __M_writer('\n')
        __M_writer('            </span>\n        </a>\n\n')
        __M_writer('        <ul class="navbar-nav">\n            ')
        __M_writer('\n\n')
        __M_writer('            ')
        __M_writer(str(tab( "repositories", "Repositories", h.url_for( controller='/repository', action='index' ) )))
        __M_writer('\n\n')
        __M_writer('            ')
        __M_writer(str(tab( "groups", "Groups", h.url_for( controller='/groups', action='index' ) )))
        __M_writer('\n\n')
        __M_writer('            ')
        __M_writer(str(tab( "admin", "Admin", h.url_for( controller='/admin', action='index' ), extra_class="admin-only", visible=( trans.user and app.config.is_admin_user( trans.user ) ) )))
        __M_writer('\n\n')
        __M_writer('            ')

        menu_options = []
        menu_options.extend( [
            ['About Tool Shed', app.config.get( "wiki_url", "https://galaxyproject.org/toolshed" ), "_blank" ],
            ['Support', app.config.get( "support_url", "https://galaxyproject.org/support" ), "_blank" ],
            ['Videos', app.config.get( "screencasts_url", "https://vimeo.com/galaxyproject" ), "_blank" ],
            ['How to Cite Tool Shed', app.config.get( "citation_url", "https://galaxyproject.org/citing-galaxy" ), "_blank" ]
        ] )
        tab( "help", "Help", None, menu_options=menu_options )
                    
        
        __M_writer('\n\n')
        __M_writer('            ')

        from markupsafe import escape
        # Menu for user who is not logged in.
        menu_options = [ [ "Login", h.url_for( controller='/user', action='login' ), "galaxy_main" ] ]
        if app.config.allow_user_creation:
            menu_options.append( [ "Register", h.url_for( controller='/user', action='create', cntrller='user' ), "galaxy_main" ] )
        extra_class = "loggedout-only"
        visible = ( trans.user == None )
        tab( "user", "User", None, visible=visible, menu_options=menu_options )
        # Menu for user who is logged in.
        if trans.user:
            email = escape( trans.user.email )
        else:
            email = ""
        menu_options = [ [ 'Logged in as <span id="user-email">%s</span>' %  email ] ]
        if app.config.use_remote_user:
            if app.config.remote_user_logout_href:
                menu_options.append( [ 'Logout', app.config.remote_user_logout_href, "_top" ] )
        else:
            menu_options.append( [ 'Preferences', h.url_for( controller='/user', action='index', cntrller='user' ), "galaxy_main" ] )
            menu_options.append( [ 'API Keys', h.url_for( controller='/user', action='api_keys', cntrller='user' ), "galaxy_main" ] )
            logout_url = h.url_for( controller='/user', action='logout' )
            menu_options.append( [ 'Logout', logout_url, "_top" ] )
        if app.config.use_remote_user:
            menu_options.append( [ 'Public Name', h.url_for( controller='/user', action='edit_username', cntrller='user' ), "galaxy_main" ] )
        
        extra_class = "loggedin-only"
        visible = ( trans.user != None )
        tab( "user", "User", None, visible=visible, menu_options=menu_options )
                    
        
        __M_writer('\n        </ul>\n    </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/webapps/tool_shed/base_panels.mako", "uri": "/webapps/tool_shed/base_panels.mako", "source_encoding": "utf-8", "line_map": {"23": 2, "29": 0, "34": 1, "35": 2, "36": 5, "37": 12, "38": 16, "39": 43, "40": 183, "46": 5, "50": 5, "56": 7, "62": 7, "63": 8, "64": 8, "65": 9, "66": 10, "67": 11, "68": 12, "69": 11, "75": 14, "80": 14, "81": 15, "82": 15, "88": 18, "93": 18, "94": 19, "95": 19, "101": 46, "110": 74, "111": 75, "112": 76, "113": 77, "114": 78, "115": 79, "116": 80, "117": 81, "118": 82, "119": 83, "120": 84, "121": 85, "122": 86, "123": 87, "124": 88, "125": 89, "126": 90, "127": 91, "128": 90, "129": 92, "130": 92, "131": 92, "132": 92, "133": 94, "134": 95, "135": 95, "136": 95, "137": 95, "138": 95, "139": 95, "140": 95, "141": 96, "142": 97, "143": 97, "144": 97, "145": 99, "146": 100, "147": 102, "148": 103, "149": 103, "150": 103, "151": 105, "152": 106, "153": 107, "154": 108, "155": 109, "156": 110, "157": 111, "158": 112, "159": 113, "160": 113, "161": 115, "162": 116, "163": 116, "164": 117, "165": 116, "166": 117, "167": 117, "168": 117, "169": 117, "170": 118, "171": 119, "172": 119, "173": 120, "174": 119, "175": 120, "176": 120, "177": 120, "178": 120, "179": 120, "180": 120, "181": 124, "182": 126, "191": 46, "192": 48, "193": 49, "194": 49, "195": 49, "196": 51, "197": 52, "198": 52, "199": 52, "200": 54, "201": 55, "202": 55, "203": 55, "204": 57, "205": 59, "206": 62, "207": 62, "208": 62, "209": 63, "210": 63, "211": 66, "212": 67, "213": 67, "214": 67, "215": 69, "216": 73, "217": 127, "218": 130, "219": 130, "220": 130, "221": 133, "222": 133, "223": 133, "224": 136, "225": 136, "226": 136, "227": 139, "228": 139, "229": 140, "230": 141, "231": 142, "232": 143, "233": 144, "234": 145, "235": 146, "236": 147, "237": 148, "238": 149, "239": 148, "240": 151, "241": 151, "242": 152, "243": 153, "244": 154, "245": 155, "246": 156, "247": 157, "248": 158, "249": 159, "250": 160, "251": 161, "252": 162, "253": 163, "254": 164, "255": 165, "256": 166, "257": 167, "258": 168, "259": 169, "260": 170, "261": 171, "262": 172, "263": 173, "264": 174, "265": 175, "266": 176, "267": 177, "268": 178, "269": 179, "270": 180, "271": 181, "272": 180, "278": 272}}
__M_END_METADATA
"""
