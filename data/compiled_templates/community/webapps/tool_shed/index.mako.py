# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747318263.7101996
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/webapps/tool_shed/index.mako'
_template_uri = '/webapps/tool_shed/index.mako'
_source_encoding = 'utf-8'
_exports = ['stylesheets', 'javascripts', 'init', 'left_panel', 'center_panel']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0x7fbfde129d30', context._clean_inheritance_tokens(), templateuri='/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0x7fbfde129d30')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/webapps/tool_shed/base_panels.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fbfde129d30')._populate(_import_ns, ['render_msg'])
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


def render_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fbfde129d30')._populate(_import_ns, ['render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('    ')
        __M_writer(str(parent.stylesheets()))
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fbfde129d30')._populate(_import_ns, ['render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.javascripts()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fbfde129d30')._populate(_import_ns, ['render_msg'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.init()))
        __M_writer('\n    ')

        self.has_left_panel=True
        self.active_view="tools"
            
        
        __M_writer('\n')
        if trans.app.config.require_login and not trans.user:
            __M_writer('        <script type="text/javascript">\n            if ( window != top ) {\n                top.location.href = location.href;\n            }\n        </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fbfde129d30')._populate(_import_ns, ['render_msg'])
        repository_id = _import_ns.get('repository_id', context.get('repository_id', UNDEFINED))
        user_id = _import_ns.get('user_id', context.get('user_id', UNDEFINED))
        util = _import_ns.get('util', context.get('util', UNDEFINED))
        has_deprecated_repositories = _import_ns.get('has_deprecated_repositories', context.get('has_deprecated_repositories', UNDEFINED))
        repository_metadata = _import_ns.get('repository_metadata', context.get('repository_metadata', UNDEFINED))
        can_administer_repositories = _import_ns.get('can_administer_repositories', context.get('can_administer_repositories', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    <div class="unified-panel-header" unselectable="on">\n        <div class=\'unified-panel-header-inner\'>')
        __M_writer(filters.html_escape(str(trans.app.shed_counter.unique_valid_tools )))
        __M_writer(' valid tools on ')
        __M_writer(filters.html_escape(str(util.unicodify( trans.app.shed_counter.generation_time ) )))
        __M_writer('</div>\n    </div>\n    <div style="padding: 0.5rem;">\n        <div class="toolMenu">\n            <div class="toolSectionList">\n')
        if user_id or repository_id:
            __M_writer('                    <div class="toolSectionPad"></div>\n                    <div class="toolSectionTitle">\n                        All Repositories\n                    </div>\n                    <div class="toolTitle">\n                        <a href="')
            __M_writer(str(h.url_for( controller='repository', action='index' )))
            __M_writer('">Browse by category</a>\n                    </div>\n')
        else:
            if repository_metadata:
                __M_writer('                        <div class="toolSectionPad"></div>\n                        <div class="toolSectionTitle">\n                            Search\n                        </div>\n                        <div class="toolSectionBody">\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                __M_writer(str(h.url_for( controller='repository', action='find_tools' )))
                __M_writer('">Search for valid tools</a>\n                            </div>\n                        </div>\n                        <div class="toolSectionPad"></div>\n                        <div class="toolSectionTitle">\n                            Valid Galaxy Utilities\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                __M_writer(str(h.url_for( controller='repository', action='browse_tools' )))
                __M_writer('">Tools</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                __M_writer(str(h.url_for( controller='repository', action='browse_datatypes' )))
                __M_writer('">Custom datatypes</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                __M_writer(str(h.url_for( controller='repository', action='browse_repository_dependencies' )))
                __M_writer('">Repository dependency definitions</a>\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                __M_writer(str(h.url_for( controller='repository', action='browse_tool_dependencies' )))
                __M_writer('">Tool dependency definitions</a>\n                        </div>\n')
            __M_writer('                    <div class="toolSectionPad"></div>\n                    <div class="toolSectionTitle">\n                        All Repositories\n                    </div>\n                    <div class="toolTitle">\n                        <a target="galaxy_main" href="')
            __M_writer(str(h.url_for( controller='repository', action='browse_categories' )))
            __M_writer('">Browse by category</a>\n                    </div>\n')
            if trans.user:
                if trans.user.active_repositories or can_administer_repositories:
                    __M_writer('                            <div class="toolSectionPad"></div>\n                            <div class="toolSectionTitle">\n                                Repositories I Can Change\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    __M_writer(str(h.url_for( controller='repository', action='browse_repositories_i_own' )))
                    __M_writer('">Repositories I own</a>\n                            </div>\n')
                    if can_administer_repositories:
                        __M_writer('                                <div class="toolTitle">\n                                    <a target="galaxy_main" href="')
                        __M_writer(str(h.url_for( controller='repository', action='browse_repositories_i_can_administer' )))
                        __M_writer('">Repositories I can administer</a>\n                                </div>\n')
                    if has_deprecated_repositories:
                        __M_writer('                                <div class="toolTitle">\n                                    <a target="galaxy_main" href="')
                        __M_writer(str(h.url_for( controller='repository', action='browse_deprecated_repositories_i_own' )))
                        __M_writer('">Deprecated repositories I own</a>\n                                </div>\n')
                    __M_writer('                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    __M_writer(str(h.url_for( controller='repository', action='browse_my_writable_repositories' )))
                    __M_writer('">My writable repositories</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    __M_writer(str(h.url_for( controller='repository', action='reset_metadata_on_my_writable_repositories_in_tool_shed' )))
                    __M_writer('">Reset metadata on my repositories</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    __M_writer(str(h.url_for( controller='repository', action='browse_my_writable_repositories_missing_tool_test_components' )))
                    __M_writer('">Latest revision: missing tool tests</a>\n                            </div>\n                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    __M_writer(str(h.url_for( controller='repository', action='browse_my_writable_repositories_with_invalid_tools' )))
                    __M_writer('">Latest revision: invalid tools</a>\n                            </div>\n')
                __M_writer('                        <div class="toolSectionPad"></div>\n                        <div class="toolSectionTitle">\n                            Available Actions\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                __M_writer(str(h.url_for( controller='repository', action='create_repository' )))
                __M_writer('">Create new repository</a>\n                        </div>\n')
                if trans.app.config.enable_galaxy_flavor_docker_image:
                    __M_writer('                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    __M_writer(str(h.url_for( controller='repository', action='create_galaxy_docker_image' )))
                    __M_writer('">Create Galaxy Docker Image</a>\n                            </div>\n')
            else:
                __M_writer('                        <div class="toolSectionPad"></div>\n                        <div class="toolSectionTitle">\n                            Available Actions\n                        </div>\n                        <div class="toolTitle">\n                            <a target="galaxy_main" href="')
                __M_writer(str(h.url_for( controller='/user', action='login' )))
                __M_writer('">Login to create a repository</a>\n                        </div>\n')
                if trans.app.config.enable_galaxy_flavor_docker_image:
                    __M_writer('                            <div class="toolTitle">\n                                <a target="galaxy_main" href="')
                    __M_writer(str(h.url_for( controller='repository', action='create_galaxy_docker_image' )))
                    __M_writer('">Create Galaxy Docker Image</a>\n                            </div>\n')
        __M_writer('            </div>\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x7fbfde129d30')._populate(_import_ns, ['render_msg'])
        repository_id = _import_ns.get('repository_id', context.get('repository_id', UNDEFINED))
        user_id = _import_ns.get('user_id', context.get('user_id', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        changeset_revision = _import_ns.get('changeset_revision', context.get('changeset_revision', UNDEFINED))
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')

        if trans.app.config.require_login and not trans.user:
            center_url = h.url_for( controller='user', action='login', message=message, status=status )
        elif repository_id and changeset_revision:
            # Route in was a sharable url: /view/{owner}/{name}/{changeset_revision}.
            center_url = h.url_for( controller='repository', action='view_repository', id=repository_id, changeset_revision=changeset_revision, message=message, status=status )
        elif repository_id:
            # Route in was a sharable url: /view/{owner}/{name}.
            center_url = h.url_for( controller='repository', action='view_repository', id=repository_id, message=message, status=status )
        elif user_id:
            # Route in was a sharable url: /view/{owner}.
            center_url = h.url_for( controller='repository', action='browse_repositories', operation="repositories_by_user", user_id=user_id, message=message, status=status )
        else:
            center_url = h.url_for( controller='repository', action='browse_categories', message=message, status=status )
            
        
        __M_writer('\n    <iframe name="galaxy_main" id="galaxy_main" frameborder="0" style="position: absolute; width: 75%; height: 100%;" src="')
        __M_writer(str(center_url))
        __M_writer('"></iframe>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/webapps/tool_shed/index.mako", "uri": "/webapps/tool_shed/index.mako", "source_encoding": "utf-8", "line_map": {"23": 2, "29": 0, "36": 1, "37": 2, "38": 8, "39": 12, "40": 27, "41": 142, "42": 161, "48": 4, "55": 4, "56": 6, "57": 6, "58": 6, "64": 10, "71": 10, "72": 11, "73": 11, "79": 14, "88": 14, "89": 15, "90": 15, "91": 16, "92": 17, "93": 18, "94": 19, "95": 20, "96": 19, "97": 20, "98": 21, "104": 29, "118": 29, "119": 31, "120": 31, "121": 31, "122": 31, "123": 36, "124": 38, "125": 43, "126": 43, "127": 45, "128": 46, "129": 47, "130": 53, "131": 53, "132": 61, "133": 61, "134": 64, "135": 64, "136": 67, "137": 67, "138": 70, "139": 70, "140": 73, "141": 78, "142": 78, "143": 80, "144": 81, "145": 82, "146": 87, "147": 87, "148": 89, "149": 90, "150": 91, "151": 91, "152": 94, "153": 95, "154": 96, "155": 96, "156": 99, "157": 100, "158": 100, "159": 103, "160": 103, "161": 106, "162": 106, "163": 109, "164": 109, "165": 112, "166": 117, "167": 117, "168": 119, "169": 120, "170": 121, "171": 121, "172": 124, "173": 125, "174": 130, "175": 130, "176": 132, "177": 133, "178": 134, "179": 134, "180": 139, "186": 144, "199": 144, "200": 145, "201": 146, "202": 147, "203": 148, "204": 149, "205": 150, "206": 151, "207": 152, "208": 153, "209": 154, "210": 155, "211": 156, "212": 157, "213": 158, "214": 159, "215": 160, "216": 159, "217": 160, "218": 160, "224": 218}}
__M_END_METADATA
"""
