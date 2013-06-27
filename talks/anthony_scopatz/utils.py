import os
from collections import Mapping

_tablemeta = """<script type="text/javascript">
window.onload=function(){{
    var tfrow = document.getElementById('{name}id').rows.length;
    var tbRow=[];
    for (var i=1;i<tfrow;i++) {{
        tbRow[i]=document.getElementById('{name}id').rows[i];
        tbRow[i].onmouseover = function(){{this.style.backgroundColor = '{hlcolor}';}};
        tbRow[i].onmouseout = function() {{this.style.backgroundColor = '{bgcolor}';}};
    }}
}};
</script>
<style type="text/css">
table.{name}class {{{style}}}
table.{name}class th {{{th}}}
table.{name}class tr {{{tr}}}
table.{name}class td {{{td}}}
</style>
"""

def _dict2style(d):
    s = ";".join(['{0}:{1}'.format(k, v) for k, v in d.items()])
    s += "" if len(s) == 0 else ';'
    return s

_table_style = {
  'style': {
    'color': '#333333',
    'width': '80%',
    'border-width': '1px',
    'border-color': '#a9a9a9', 
    'border-collapse': 'collapse', 
    'text-align': 'center', 
    'margin': 'auto',
    },
  'th': {
    'background-color': '#b8b8b8',
    'border-width': '1px',
    'padding': '4px',
    'border-style':'solid',
    'border-color': '#a9a9a9',
    'text-align': 'left',
    },
  'tr': {
    'background-color': '#ffffff',
    'text-align': 'center',
    },
  'td': {
    'border-width': '1px',
    'padding': '4px', 
    'border-style': 'solid', 
    'border-color': '#a9a9a9',
    'text-align': 'center',
    },
  }

def htmltable(table, name, title=None, style=None, highlight_color='#f3f8aa', 
              headers=frozenset([0])):
    if style is None:
        style = {}
    dmeta = {}
    for key in ['style', 'td', 'tr', 'th']:
        d = dict(_table_style[key])
        d.update(style.get(key, {}))
        if key == 'tr':
            dmeta['bgcolor'] = d['background-color']
        dmeta[key] = _dict2style(d)
    dmeta['name'] = name
    dmeta['hlcolor'] = highlight_color
    meta = _tablemeta.format(**dmeta)
    tstr = '<table id="{name}id" class="{name}class" border="1">\n'.format(name=name)
    for i, row in enumerate(table):
        tstr += "<tr>"
        tx = "th" if i in headers else "td"
        for cell in row:
            if isinstance(cell, Mapping):
                tstr += '<{tx} style="{style}">{val}</{tx}>'.format(val=cell['value'], 
                                              tx=tx, style=_dict2style(cell['style']))
            else:
                tstr += "<{tx}>{val}</{tx}>".format(val=cell, tx=tx)
        tstr += "</tr>\n"
    tstr += '</table>'
    if title is not None:
        title = '<div style="text-align:center;"><b>{0}</b></div>\n'.format(title)
        tstr = title + tstr
    return meta, tstr
