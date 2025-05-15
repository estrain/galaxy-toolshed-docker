# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747339871.831247
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/galaxy_client_app.mako'
_template_uri = '/galaxy_client_app.mako'
_source_encoding = 'utf-8'
_exports = ['render_json', 'load', 'config_sentry', 'config_google_analytics', 'config_plausible_analytics', 'config_matomo_analytics', 'get_user_dict', 'get_user_json']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_json(context,dictionary):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str( h.dumps( dictionary, indent=( 2 if trans.debug else 0 ) ) ))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_load(context,app=None,**kwargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def render_json(dictionary):
            return render_render_json(context,dictionary)
        h = context.get('h', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        def get_user_dict():
            return render_get_user_dict(context)
        __M_writer = context.writer()
        __M_writer('\n    <script type="text/javascript">\n        // galaxy_client_app.mako, load\n\n        var bootstrapped;\n        try {\n            bootstrapped = ')
        __M_writer(str(render_json(kwargs)))
        __M_writer(';\n        } catch(err) {\n            console.warn("Unable to parse bootstrapped variable", err);\n            bootstrapped = {};\n        }\n\n        var options = {\n            root: \'')
        __M_writer(str(h.url_for( "/" )))
        __M_writer("',\n            user: ")
        __M_writer(str( render_json( get_user_dict() )))
        __M_writer(",\n            session_csrf_token: '")
        __M_writer(str( trans.session_csrf_token ))
        __M_writer("'\n        };\n\n        config.set({\n            options: options,\n            bootstrapped: bootstrapped\n        });\n\n")
        if app:
            __M_writer('            console.warn("Does app ever run? Is it ever not-named app?", \'')
            __M_writer(str(app))
            __M_writer("');\n")
        __M_writer('\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_config_sentry(context,app):
    __M_caller = context.caller_stack._push_frame()
    try:
        trans = context.get('trans', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if app and app.config:
            __M_writer('        <script type="text/javascript">\n\n            var sentry = {};\n')
            if app.config.sentry_dsn:
                __M_writer('                sentry.sentry_dsn_public = "')
                __M_writer(str(app.config.sentry_dsn_public))
                __M_writer('"\n')
                if trans.user:
                    __M_writer('                    sentry.email = "')
                    __M_writer(filters.html_escape(str(trans.user.email)))
                    __M_writer('";\n')
            __M_writer('\n            config.set({\n                sentry: sentry\n            });\n\n        </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_config_google_analytics(context,ga_code):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <script>\n        console.log("config_google_analytics ga_code:", \'')
        __M_writer(str(ga_code))
        __M_writer("');\n")
        if ga_code:
            __M_writer("            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\n            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n            })(window,document,'script','//www.google-analytics.com/analytics.js','ga');\n            ga('create', '")
            __M_writer(str(ga_code))
            __M_writer("', 'auto');\n            ga('send', 'pageview');\n")
        else:
            __M_writer('            console.warn("Missing google analytics code");\n')
        __M_writer('    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_config_plausible_analytics(context,plausible_server,plausible_domain):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        if plausible_server and plausible_domain:
            __M_writer('        <script async defer data-domain="')
            __M_writer(str(plausible_domain))
            __M_writer('" src="')
            __M_writer(str(plausible_server))
            __M_writer('/js/plausible.js"></script>\n')
        else:
            __M_writer('        <script>console.warn("Missing plausible server or plausible domain");</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_config_matomo_analytics(context,matomo_server,matomo_site_id):
    __M_caller = context.caller_stack._push_frame()
    try:
        ga_code = context.get('ga_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <script type="text/javascript">\n        console.log("config_matomo_analytics matomo_server:", \'')
        __M_writer(str(matomo_server))
        __M_writer('\');\n        console.log("config_matomo_analytics matomo_site_id:", \'')
        __M_writer(str(matomo_site_id))
        __M_writer("');\n")
        if ga_code:
            __M_writer('            var _paq = window._paq = window._paq || [];\n            /* tracker methods like "setCustomDimension" should be called before "trackPageView" */\n            _paq.push([\'trackPageView\']);\n            _paq.push([\'enableLinkTracking\']);\n            (function () {\n                var u = "')
            __M_writer(str(matomo_server))
            __M_writer('/";\n                _paq.push([\'setTrackerUrl\', u + \'matomo.php\']);\n                _paq.push([\'setSiteId\', \'')
            __M_writer(str(matomo_site_id))
            __M_writer("']);\n                var d = document;\n                var g = d.createElement('script');\n                var s = d.getElementsByTagName('script')[0];\n                g.type = 'text/javascript';\n                g.async = true;\n                g.src = u + 'matomo.js';\n                s.parentNode.insertBefore(g, s);\n            })();\n")
        else:
            __M_writer('            console.warn("Missing matomo server or matomo site id");\n')
        __M_writer('    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_user_dict(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        Exception = context.get('Exception', UNDEFINED)
        util = context.get('util', UNDEFINED)
        int = context.get('int', UNDEFINED)
        float = context.get('float', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        AssertionError = context.get('AssertionError', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('    ')

        from markupsafe import escape
        user_dict = {}
        try:
            if trans.user:
                user_dict = trans.user.to_dict( view='element',
                    value_mapper={ 'id': trans.security.encode_id, 'total_disk_usage': float, 'email': escape, 'username': escape } )
                user_dict[ 'quota_percent' ] = trans.app.quota_agent.get_percent( trans=trans )
                user_dict[ 'is_admin' ] = trans.user_is_admin
        
                # tags used
                users_api_controller = trans.webapp.api_controllers[ 'users' ]
                tags_used = []
                for tag in users_api_controller.get_user_tags_used( trans, user=trans.user ):
                    tag = escape( tag )
                    if tag:
                        tags_used.append( tag )
                user_dict[ 'tags_used' ] = tags_used
        
                return user_dict
        
            usage = 0
            percent = None
            try:
                usage = trans.app.quota_agent.get_usage( trans, history=trans.history )
                percent = trans.app.quota_agent.get_percent( trans=trans, usage=usage )
            except AssertionError as assertion:
                # no history for quota_agent.get_usage assertion
                pass
            return {
                'total_disk_usage'      : int( usage ),
                'nice_total_disk_usage' : util.nice_size( usage ),
                'quota_percent'         : percent
            }
        
        except Exception as exc:
            pass
            #TODO: no logging available?
            #log.exception( exc )
        
        return user_dict
            
        
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_user_json(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        def get_user_dict():
            return render_get_user_dict(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str( h.dumps( get_user_dict() )))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/galaxy_client_app.mako", "uri": "/galaxy_client_app.mako", "source_encoding": "utf-8", "line_map": {"16": 0, "21": 3, "22": 6, "23": 35, "24": 55, "25": 71, "26": 79, "27": 106, "28": 155, "29": 160, "35": 1, "41": 1, "42": 2, "43": 2, "49": 7, "59": 7, "60": 13, "61": 13, "62": 20, "63": 20, "64": 21, "65": 21, "66": 22, "67": 22, "68": 30, "69": 31, "70": 31, "71": 31, "72": 33, "78": 37, "83": 37, "84": 38, "85": 39, "86": 42, "87": 43, "88": 43, "89": 43, "90": 44, "91": 45, "92": 45, "93": 45, "94": 48, "100": 57, "104": 57, "105": 59, "106": 59, "107": 60, "108": 61, "109": 65, "110": 65, "111": 67, "112": 68, "113": 70, "119": 73, "123": 73, "124": 74, "125": 75, "126": 75, "127": 75, "128": 75, "129": 75, "130": 76, "131": 77, "137": 81, "142": 81, "143": 83, "144": 83, "145": 84, "146": 84, "147": 85, "148": 86, "149": 91, "150": 91, "151": 93, "152": 93, "153": 102, "154": 103, "155": 105, "161": 110, "171": 110, "172": 113, "173": 113, "174": 114, "175": 115, "176": 116, "177": 117, "178": 118, "179": 119, "180": 120, "181": 121, "182": 122, "183": 123, "184": 124, "185": 125, "186": 126, "187": 127, "188": 128, "189": 129, "190": 130, "191": 131, "192": 132, "193": 133, "194": 134, "195": 135, "196": 136, "197": 137, "198": 138, "199": 139, "200": 140, "201": 141, "202": 142, "203": 143, "204": 144, "205": 145, "206": 146, "207": 147, "208": 148, "209": 149, "210": 150, "211": 151, "212": 152, "213": 153, "214": 154, "215": 155, "216": 154, "222": 157, "229": 157, "230": 159, "231": 159, "237": 231}}
__M_END_METADATA
"""
