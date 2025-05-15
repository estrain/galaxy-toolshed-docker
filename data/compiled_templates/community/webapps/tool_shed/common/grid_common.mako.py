# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1747339872.4124465
_enable_loop = True
_template_filename = '/home/galaxy/galaxy/lib/tool_shed/webapp/templates/webapps/tool_shed/common/grid_common.mako'
_template_uri = '/webapps/tool_shed/category/../common/grid_common.mako'
_source_encoding = 'utf-8'
_exports = ['render_grid_column_filter', 'render_grid_filters']



from galaxy.web.legacy_framework.grids import TextColumn, StateColumn, GridColumnFilter
from galaxy.web.framework.helpers import iff


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_column_filter(context,grid,column):
    __M_caller = context.caller_stack._push_frame()
    try:
        enumerate = context.get('enumerate', UNDEFINED)
        list = context.get('list', UNDEFINED)
        len = context.get('len', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        basestring = context.get('basestring', UNDEFINED)
        cur_filter_dict = context.get('cur_filter_dict', UNDEFINED)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <tr>\n        ')

        column_label = column.label
        if column.filterable == "advanced":
            column_label = column_label.lower()
                
        
        __M_writer('\n')
        if column.filterable == "advanced":
            __M_writer('            <td align="left" style="padding-left: 10px">')
            __M_writer(str(column_label))
            __M_writer(':</td>\n')
        __M_writer('        <td style="padding: 0;">\n')
        if isinstance(column, TextColumn):
            __M_writer('                <form class="text-filter-form" column_key="')
            __M_writer(str(column.key))
            __M_writer('" action="')
            __M_writer(str(url(dict())))
            __M_writer('" method="get" >\n')
            for temp_column in grid.columns:
                if temp_column.key in cur_filter_dict:
                    __M_writer('                            ')
                    value = cur_filter_dict[ temp_column.key ] 
                    
                    __M_writer('\n')
                    if value != "All":
                        __M_writer('                                ')

                        if isinstance( temp_column, TextColumn ):
                            value = h.dumps( value )
                                                        
                        
                        __M_writer('\n                                <input type="hidden" id="')
                        __M_writer(str(temp_column.key))
                        __M_writer('" name="f-')
                        __M_writer(str(temp_column.key))
                        __M_writer('" value=\'')
                        __M_writer(str(value))
                        __M_writer("'/>\n")
            __M_writer('                    <span id="')
            __M_writer(str(column.key))
            __M_writer('-filtering-criteria">\n')
            if column.key in cur_filter_dict:
                __M_writer('                            ')
                column_filter = cur_filter_dict[column.key] 
                
                __M_writer('\n')
                if isinstance( column_filter, basestring ):
                    if column_filter != "All":
                        __M_writer("                                    <span class='text-filter-val'>\n                                        ")
                        __M_writer(str(cur_filter_dict[column.key]))
                        __M_writer('\n                                        ')
                        filter_all = GridColumnFilter( "", { column.key : "All" } ) 
                        
                        __M_writer('\n                                        <a href="')
                        __M_writer(str(url(filter_all.get_url_args())))
                        __M_writer('"><span class="delete-search-icon" /></a>\n                                    </span>\n')
                elif isinstance( column_filter, list ):
                    for i, filter in enumerate( column_filter ):
                        if i > 0:
                            __M_writer('                                        ,\n')
                        __M_writer("                                    <span class='text-filter-val'>")
                        __M_writer(str(filter))
                        __M_writer('\n                                        ')

                        new_filter = list( column_filter )
                        del new_filter[ i ]
                        new_column_filter = GridColumnFilter( "", { column.key : h.dumps( new_filter ) } )
                                                                
                        
                        __M_writer('\n                                        <a href="')
                        __M_writer(str(url(new_column_filter.get_url_args())))
                        __M_writer('"><span class="delete-search-icon" /></a>\n                                    </span>\n')
            __M_writer('                    </span>\n')
            __M_writer('                    <span class="search-box">\n                        ')
 
                            # Set value, size of search input field. Minimum size is 20 characters.
            value = iff( column.filterable == "standard", column.label.lower(), "") 
            size = len( value )
            if size < 20:
                size = 20
            # +4 to account for search icon/button.
            size = size + 4
                                    
            
            __M_writer('\n                        <input class="search-box-input" id="input-')
            __M_writer(str(column.key))
            __M_writer('-filter" name="f-')
            __M_writer(str(column.key))
            __M_writer('" type="text" value="')
            __M_writer(str(value))
            __M_writer('" size="')
            __M_writer(str(size))
            __M_writer('"/>\n                        <button type="submit" title=\'Search\' style="background: transparent; border: none; padding: 4px; margin: 0px;">\n                            <i class="fa fa-search"></i>\n                        </button>\n                    </span>\n                </form>\n')
        else:
            __M_writer('                <span id="')
            __M_writer(str(column.key))
            __M_writer('-filtering-criteria">\n')
            for i, filter in enumerate( column.get_accepted_filters() ):
                __M_writer('                        ')
 
                            # HACK: we know that each filter will have only a single argument, so get that single argument.
                for key, arg in filter.args.items():
                    filter_key = key
                    filter_arg = arg
                                        
                
                __M_writer('\n')
                if i > 0:
                    __M_writer('                            |\n')
                if column.key in cur_filter_dict and column.key in filter.args and cur_filter_dict[column.key] == filter.args[column.key]:
                    __M_writer('                            <span class="categorical-filter ')
                    __M_writer(str(column.key))
                    __M_writer('-filter current-filter">')
                    __M_writer(str(filter.label))
                    __M_writer('</span>\n')
                else:
                    __M_writer('                            <span class="categorical-filter ')
                    __M_writer(str(column.key))
                    __M_writer('-filter">\n                                <a href="')
                    __M_writer(str(url(filter.get_url_args())))
                    __M_writer('" filter_key="')
                    __M_writer(str(filter_key))
                    __M_writer('" filter_val="')
                    __M_writer(str(filter_arg))
                    __M_writer('">')
                    __M_writer(str(filter.label))
                    __M_writer('</a>\n                            </span>\n')
            __M_writer('                </span>\n')
        __M_writer('        </td>\n    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_grid_filters(context,grid,render_advanced_search=True):
    __M_caller = context.caller_stack._push_frame()
    try:
        endif = context.get('endif', UNDEFINED)
        cur_filter_dict = context.get('cur_filter_dict', UNDEFINED)
        default_filter_dict = context.get('default_filter_dict', UNDEFINED)
        url = context.get('url', UNDEFINED)
        def render_grid_column_filter(grid,column):
            return render_render_grid_column_filter(context,grid,column)
        kwargs = context.get('kwargs', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')

        # Show advanced search if flag set or if there are filters for advanced search fields.
        advanced_search_display = "none"
        if 'advanced-search' in kwargs and kwargs['advanced-search'] in ['True', 'true']:
            advanced_search_display = "block"
        
        for column in grid.columns:
            if column.filterable == "advanced":
                ## Show div if current filter has value that is different from the default filter.
                if column.key in cur_filter_dict and column.key in default_filter_dict and \
                    cur_filter_dict[column.key] != default_filter_dict[column.key]:
                        advanced_search_display = "block"
        
        # do not show standard search if showing adv.
        standard_search_display = "block"
        if advanced_search_display == "block":
            standard_search_display = "none"
            
        
        __M_writer('\n')
        __M_writer('    <div id="standard-search" style="display: ')
        __M_writer(str(standard_search_display))
        __M_writer(';">\n        <table>\n            <tr><td style="padding: 0;">\n                <table>\n')
        for column in grid.columns:
            if column.filterable == "standard":
                __M_writer('                       ')
                __M_writer(str(render_grid_column_filter( grid, column )))
                __M_writer('\n')
        __M_writer('                </table>\n            </td></tr>\n            <tr><td>\n')
        __M_writer('                \n')
        __M_writer('                ')

        show_advanced_search_link = False
        if render_advanced_search:
            for column in grid.columns:
                if column.filterable == "advanced":
                    show_advanced_search_link = True
                    break
                endif
                        
        
        __M_writer('\n')
        if show_advanced_search_link:
            __M_writer('                    ')
            args = { "advanced-search" : True } 
            
            __M_writer('\n                    <a href="')
            __M_writer(str(url(args)))
            __M_writer('" class="advanced-search-toggle">Advanced Search</a>\n')
        __M_writer('            </td></tr>\n        </table>\n    </div>\n    \n')
        __M_writer('    <div id="advanced-search" style="display: ')
        __M_writer(str(advanced_search_display))
        __M_writer('; margin-top: 5px; border: 1px solid #ccc;">\n        <table>\n            <tr><td style="text-align: left" colspan="100">\n                ')
        args = { "advanced-search" : False } 
        
        __M_writer('\n                <a href="')
        __M_writer(str(url(args)))
        __M_writer('" class="advanced-search-toggle">Close Advanced Search</a>\n')
        __M_writer('            </td></tr>\n')
        for column in grid.columns:            
            if column.filterable == "advanced":
                if column.key in cur_filter_dict and column.key in default_filter_dict and \
                        cur_filter_dict[column.key] != default_filter_dict[column.key]:
                    __M_writer('                        <script type="text/javascript">\n                            $(\'#advanced-search\').css("display", "block");\n                        </script>\n')
                __M_writer('            \n                    ')
                __M_writer(str(render_grid_column_filter( grid, column )))
                __M_writer('\n')
        __M_writer('        </table>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/galaxy/galaxy/lib/tool_shed/webapp/templates/webapps/tool_shed/common/grid_common.mako", "uri": "/webapps/tool_shed/category/../common/grid_common.mako", "source_encoding": "utf-8", "line_map": {"16": 1, "17": 2, "18": 3, "19": 4, "20": 5, "21": 0, "26": 4, "27": 103, "28": 189, "34": 7, "47": 7, "48": 9, "49": 10, "50": 11, "51": 12, "52": 13, "53": 14, "54": 13, "55": 14, "56": 15, "57": 15, "58": 15, "59": 17, "60": 18, "61": 19, "62": 19, "63": 19, "64": 19, "65": 19, "66": 21, "67": 22, "68": 23, "69": 23, "70": 24, "71": 23, "72": 24, "73": 25, "74": 25, "75": 26, "76": 27, "77": 28, "78": 29, "79": 28, "80": 29, "81": 29, "82": 29, "83": 29, "84": 29, "85": 29, "86": 34, "87": 34, "88": 34, "89": 35, "90": 36, "91": 36, "92": 37, "93": 36, "94": 37, "95": 38, "96": 39, "97": 40, "98": 40, "99": 41, "100": 42, "101": 41, "102": 42, "103": 42, "104": 45, "105": 46, "106": 47, "107": 48, "108": 50, "109": 50, "110": 50, "111": 51, "112": 52, "113": 53, "114": 54, "115": 55, "116": 56, "117": 55, "118": 56, "119": 56, "120": 61, "121": 63, "122": 64, "123": 65, "124": 66, "125": 67, "126": 68, "127": 69, "128": 70, "129": 71, "130": 72, "131": 73, "132": 72, "133": 73, "134": 73, "135": 73, "136": 73, "137": 73, "138": 73, "139": 73, "140": 73, "141": 79, "142": 80, "143": 80, "144": 80, "145": 81, "146": 82, "147": 82, "148": 83, "149": 84, "150": 85, "151": 86, "152": 87, "153": 88, "154": 87, "155": 88, "156": 89, "157": 91, "158": 92, "159": 92, "160": 92, "161": 92, "162": 92, "163": 93, "164": 94, "165": 94, "166": 94, "167": 95, "168": 95, "169": 95, "170": 95, "171": 95, "172": 95, "173": 95, "174": 95, "175": 99, "176": 101, "182": 106, "193": 106, "194": 107, "195": 108, "196": 109, "197": 110, "198": 111, "199": 112, "200": 113, "201": 114, "202": 115, "203": 116, "204": 117, "205": 118, "206": 119, "207": 120, "208": 121, "209": 122, "210": 123, "211": 124, "212": 125, "213": 124, "214": 126, "215": 126, "216": 126, "217": 130, "218": 131, "219": 132, "220": 132, "221": 132, "222": 135, "223": 142, "224": 144, "225": 144, "226": 145, "227": 146, "228": 147, "229": 148, "230": 149, "231": 150, "232": 151, "233": 152, "234": 153, "235": 152, "236": 153, "237": 154, "238": 154, "239": 155, "240": 154, "241": 155, "242": 155, "243": 157, "244": 162, "245": 162, "246": 162, "247": 165, "248": 166, "249": 165, "250": 166, "251": 166, "252": 173, "253": 174, "254": 175, "255": 177, "257": 179, "258": 183, "259": 184, "260": 184, "261": 187, "267": 261}}
__M_END_METADATA
"""
