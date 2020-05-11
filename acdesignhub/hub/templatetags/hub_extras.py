from django import template

register = template.Library()

@register.filter
def format_design_code(value):
    part1 = value[0:2]
    part2 = value[2:6]
    part3 = value[6:10]
    part4 = value[10:14]
    return "-".join([part1, part2, part3, part4])
