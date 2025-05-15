# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747339872.3961942
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/webapps/tool_shed/category/grid.mako'
_template_uri = '/webapps/tool_shed/category/grid.mako'
_source_encoding = 'utf-8'
_exports = ['insert']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('grid_base', context._clean_inheritance_tokens(), templateuri='/legacy/grid_base.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'grid_base')] = ns

    ns = runtime.TemplateNamespace('grid_common', context._clean_inheritance_tokens(), templateuri='../common/grid_common.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'grid_common')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'grid_base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'grid_common')._populate(_import_ns, ['*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        grid_base = _mako_get_namespace(context, 'grid_base')
        capture = _import_ns.get('capture', context.get('capture', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer(str(grid_base.load(False, capture(self.insert))))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_insert(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'grid_base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'grid_common')._populate(_import_ns, ['*'])
        grid_common = _mako_get_namespace(context, 'grid_common')
        __M_writer = context.writer()
        __M_writer('\n    ')

        from tool_shed.grids.repository_grids import RepositoryGrid
        repo_grid = RepositoryGrid()
        grid_common.render_grid_filters(repo_grid)
            
        
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/webapps/tool_shed/category/grid.mako", "uri": "/webapps/tool_shed/category/grid.mako", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "32": 0, "43": 1, "44": 2, "45": 3, "46": 11, "47": 13, "48": 13, "54": 5, "62": 5, "63": 6, "64": 7, "65": 8, "66": 9, "67": 10, "68": 11, "69": 10, "75": 69}}
__M_END_METADATA
"""
