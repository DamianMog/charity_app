import collections
from itertools import islice

from django import template
from urllib.parse import urlencode

register = template.Library()


@register.simple_tag(takes_context=True)
def urlparams(context, var_name, **kwargs):
    request = context['request']
    full_path = request.GET
    if kwargs and not full_path:
        final_path = {k: v for k, v in kwargs.items() if v is not None}
        final_path[var_name] = final_path.pop('work_tab')
        final_path = sorted(final_path.items())
        return f'?{urlencode(final_path)}'
    exis = {}
    for k, v in full_path.items():
        exis[k] = v
    safe_args = {k: v for k, v in kwargs.items() if v is not None}
    final_path = {**safe_args, **exis}
    final_path[var_name] = final_path.pop('work_tab')
    copy_sa = final_path.copy()
    for k, v in copy_sa.items():
        if v == 1:
            del final_path[k]
    final_path = sorted(final_path.items())
    return f'?{urlencode(final_path)}'
