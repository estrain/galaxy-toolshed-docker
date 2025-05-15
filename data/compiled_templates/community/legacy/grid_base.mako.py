# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747318747.317912
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/legacy/grid_base.mako'
_template_uri = '/legacy/grid_base.mako'
_source_encoding = 'utf-8'
_exports = ['init', 'title', 'body', 'load', 'get_grid_config']



from galaxy.util import unicodify
from galaxy.web.legacy_framework.grids import TextColumn

def inherit(context):
    kwargs = context.get( 'kwargs', {} )
    if kwargs.get( 'embedded', False ):
        # No inheritance - using only embeddable content (self.body)
        return None
    return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context,embedded=False,insert=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')

        self.has_left_panel         = False
        self.has_right_panel        = False
        self.message_box_visible    = False
        self.overlay_visible        = False
        self.active_view            = 'user'
        
        
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        grid = context.get('grid', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str(grid.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(self.load()))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_load(context,embedded=False,insert=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n    <!-- grid_base.mako, load -->\n    <div id="grid-container"></div>\n\n    <script type="text/javascript">\n        config.addInitialization(function() {\n            var legacyGridViewConfig = ')
        __M_writer(str( h.dumps( self.get_grid_config( embedded=embedded, insert=insert ) ) ))
        __M_writer(';\n            console.log("grid_base.mako, javascript_app", legacyGridViewConfig);\n            new window.bundleToolshed.LegacyGridView(legacyGridViewConfig);\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_get_grid_config(context,embedded=False,insert=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        bytes = context.get('bytes', UNDEFINED)
        advanced_search = context.get('advanced_search', UNDEFINED)
        util = context.get('util', UNDEFINED)
        refresh_frames = context.get('refresh_frames', UNDEFINED)
        cur_filter_dict = context.get('cur_filter_dict', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        num_pages = context.get('num_pages', UNDEFINED)
        endif = context.get('endif', UNDEFINED)
        endfor = context.get('endfor', UNDEFINED)
        sort_key = context.get('sort_key', UNDEFINED)
        status = context.get('status', UNDEFINED)
        message = context.get('message', UNDEFINED)
        current_item = context.get('current_item', UNDEFINED)
        query = context.get('query', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        cur_page_num = context.get('cur_page_num', UNDEFINED)
        num_page_links = context.get('num_page_links', UNDEFINED)
        grid = context.get('grid', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        url = context.get('url', UNDEFINED)
        default_filter_dict = context.get('default_filter_dict', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')

        item_class = grid.model_class.__name__
        self.grid_config = {
            'title'                         : grid.title,
            'url_base'                      : trans.request.path_url,
            'async'                         : grid.use_async,
            'async_ops'                     : [],
            'categorical_filters'           : {},
            'filters'                       : cur_filter_dict,
            'sort_key'                      : sort_key,
            'show_item_checkboxes'          : context.get('show_item_checkboxes', False),
            'cur_page_num'                  : cur_page_num,
            'num_pages'                     : num_pages,
            'num_page_links'                : num_page_links,
            'allow_fetching_all_results'    : grid.allow_fetching_all_results,
            'status'                        : status,
            'message'                       : util.restore_text(message),
            'global_actions'                : [],
            'operations'                    : [],
            'items'                         : [],
            'columns'                       : [],
            'model_class'                   : str( grid.model_class ),
            'use_paging'                    : grid.use_paging,
            'legend'                        : grid.legend,
            'current_item_id'               : False,
            'use_panels'                    : context.get('use_panels'),
            'use_hide_message'              : grid.use_hide_message,
            'insert'                        : insert,
            'default_filter_dict'           : default_filter_dict,
            'advanced_search'               : advanced_search,
            'refresh_frames'                : [],
            'embedded'                      : embedded,
            'info_text'                     : grid.info_text,
            'url'                           : url(dict())
        }
        
        ## add refresh frames
        if refresh_frames:
            self.grid_config['refresh_frames'] = refresh_frames
        
        ## add current item if exists
        if current_item:
            self.grid_config['current_item_id'] = current_item.id
        endif
        
        ## column
        for column in grid.columns:
        
            ## add column sort links
            href = None
            extra = ''
            if column.sortable:
                if sort_key.endswith(column.key):
                    if not sort_key.startswith("-"):
                        href = url( sort=( "-" + column.key ) )
                        extra = "&darr;"
                    else:
                        href = url( sort=( column.key ) )
                        extra = "&uarr;"
                else:
                    href = url( sort=column.key )
        
            ## add to configuration
            self.grid_config['columns'].append({
                'key'               : column.key,
                'visible'           : column.visible,
                'nowrap'            : column.nowrap,
                'attach_popup'      : column.attach_popup,
                'label_id_prefix'   : column.label_id_prefix,
                'sortable'          : column.sortable,
                'label'             : column.label,
                'filterable'        : column.filterable,
                'target'            : column.target,
                'is_text'           : isinstance(column, TextColumn),
                'href'              : href,
                'extra'             : extra
            })
        endfor
        
        ## operations
        for operation in grid.operations:
            self.grid_config['operations'].append({
                'allow_multiple'        : operation.allow_multiple,
                'allow_popup'           : operation.allow_popup,
                'target'                : operation.target,
                'label'                 : operation.label,
                'confirm'               : operation.confirm,
                'global_operation'      : False
            })
            if operation.allow_multiple:
                self.grid_config['show_item_checkboxes'] = True
        
            if operation.global_operation:
                self.grid_config['global_operation'] = url( ** (operation.global_operation()) )
        endfor
        
        ## global actions
        for action in grid.global_actions:
            self.grid_config['global_actions'].append({
                'url_args'  : url(**action.url_args),
                'label'     : action.label,
                'target'    : action.target
            })
        endfor
        
        ## Operations that are async (AJAX) compatible.
        for operation in [op for op in grid.operations if op.async_compatible]:
            self.grid_config['async_ops'].append(operation.label.lower());
        endfor
        
        ## Filter values for categorical filters.
        for column in grid.columns:
            if column.filterable is not None and not isinstance( column, TextColumn ):
                self.grid_config['categorical_filters'][column.key] = dict([ (filter.label, filter.args) for filter in column.get_accepted_filters() ])
            endif
        endfor
        
        # items
        for i, item in enumerate( query ):
            item_dict = {
                'id'                    : item.id,
                'encode_id'             : trans.security.encode_id(item.id),
                'link'                  : [],
                'operation_config'      : {},
                'column_config'         : {}
            }
        
            ## data columns
            for column in grid.columns:
                if column.visible:
                    ## get link
                    link = column.get_link(trans, grid, item)
                    if link:
                        link = url(**link)
                    else:
                        link = None
                    endif
        
                    ## target
                    target = column.target
        
                    ## get value
                    value = column.get_value( trans, grid, item )
        
                    # Handle non-ascii chars.
                    if isinstance(value, bytes):
                        value = unicodify(value, 'utf-8')
                        value = value.replace('/', '//')
                    endif
        
                    ## Item dictionary
                    item_dict['column_config'][column.label] = {
                        'link'      : link,
                        'value'     : value,
                        'target'    : target
                    }
                endif
            endfor
            ## add operation details to item
            for operation in grid.operations:
                item_dict['operation_config'][operation.label] = {
                    'allowed'   : operation.allowed(item),
                    'url_args'  : url( **operation.get_url_args( item ) )
                }
            endfor
        
            ## add item to list
            self.grid_config['items'].append(item_dict)
        endfor
        
        return self.grid_config
        
        
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/legacy/grid_base.mako", "uri": "/legacy/grid_base.mako", "source_encoding": "utf-8", "line_map": {"16": 1, "17": 2, "18": 3, "19": 4, "20": 5, "21": 6, "22": 7, "23": 8, "24": 9, "25": 10, "26": 11, "27": 12, "39": 0, "44": 11, "45": 12, "46": 17, "47": 26, "48": 29, "49": 34, "50": 49, "51": 225, "57": 18, "62": 18, "63": 19, "64": 20, "65": 21, "66": 22, "67": 23, "68": 24, "69": 25, "70": 26, "71": 25, "77": 29, "82": 29, "88": 32, "93": 32, "94": 33, "95": 33, "101": 37, "107": 37, "108": 44, "109": 44, "115": 51, "143": 51, "144": 53, "145": 54, "146": 55, "147": 56, "148": 57, "149": 58, "150": 59, "151": 60, "152": 61, "153": 62, "154": 63, "155": 64, "156": 65, "157": 66, "158": 67, "159": 68, "160": 69, "161": 70, "162": 71, "163": 72, "164": 73, "165": 74, "166": 75, "167": 76, "168": 77, "169": 78, "170": 79, "171": 80, "172": 81, "173": 82, "174": 83, "175": 84, "176": 85, "177": 86, "178": 87, "179": 88, "180": 89, "181": 90, "182": 91, "183": 92, "184": 93, "185": 94, "186": 95, "187": 96, "188": 97, "189": 98, "190": 99, "191": 100, "192": 101, "193": 102, "194": 103, "195": 104, "196": 105, "197": 106, "198": 107, "199": 108, "200": 109, "201": 110, "202": 111, "203": 112, "204": 113, "205": 114, "206": 115, "207": 116, "208": 117, "209": 118, "210": 119, "211": 120, "212": 121, "213": 122, "214": 123, "215": 124, "216": 125, "217": 126, "218": 127, "219": 128, "220": 129, "221": 130, "222": 131, "223": 132, "224": 133, "225": 134, "226": 135, "227": 136, "228": 137, "229": 138, "230": 139, "231": 140, "232": 141, "233": 142, "234": 143, "235": 144, "236": 145, "237": 146, "238": 147, "239": 148, "240": 149, "241": 150, "242": 151, "243": 152, "244": 153, "245": 154, "246": 155, "247": 156, "248": 157, "249": 158, "250": 159, "251": 160, "252": 161, "253": 162, "254": 163, "255": 164, "256": 165, "257": 166, "258": 167, "259": 168, "260": 169, "261": 170, "262": 171, "263": 172, "264": 173, "265": 174, "266": 175, "267": 176, "268": 177, "269": 178, "270": 179, "271": 180, "272": 181, "273": 182, "274": 183, "275": 184, "276": 185, "277": 186, "278": 187, "279": 188, "280": 189, "281": 190, "282": 191, "283": 192, "284": 193, "285": 194, "286": 195, "287": 196, "288": 197, "289": 198, "290": 199, "291": 200, "292": 201, "293": 202, "294": 203, "295": 204, "296": 205, "297": 206, "298": 207, "299": 208, "300": 209, "301": 210, "302": 211, "303": 212, "304": 213, "305": 214, "306": 215, "307": 216, "308": 217, "309": 218, "310": 219, "311": 220, "312": 221, "313": 222, "314": 223, "315": 224, "316": 225, "317": 224, "323": 317}}
__M_END_METADATA
"""
