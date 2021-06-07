# def render_input(field):
#     return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username111')
# print(username_f)

###

# def p_wrapper(func):
#     print(func)
#
#     def tag_wrapper(*args, **kwargs):
#         print('args', args)
#         print('kwargs', kwargs)
#         markup = func(*args, **kwargs)
#         print(markup)
#         return markup
#
#     return tag_wrapper
#
#
# @p_wrapper
# def render_input(field):
#     return f'<input id="id_{field}" type="text" name="{field}">'
#
#
# username_f = render_input('username')
# print(render_input)


###

def p_wrapper(func):
    def tag_wrapper(*args, **kwargs):
        markup = func(*args, **kwargs)
        return f'<p>{markup}</p>'

    return tag_wrapper


@p_wrapper
def render_input(field):
    return f'<input id="id_{field}" type="text" name="{field}">'


username_f = render_input('username')
print(username_f)
