from django import template

register = template.Library()

@register.filter
def test_tag(data):
    print 'tag:',data
    return "<h1>%s</h1>" % data


@register.simple_tag
def test_tag2(data):
    return "<h1>%s</h1>" % data

def insert_comment_node(data_dic,margin_val):
    html = ""
    for p,v in data_dic.items():
        r = '''
                <div style="margin-left:%spx;margin-top:15px;border-left:1px dashed green;border-bottom:1px dashed green">
                <span class="comment-user">%s</span>
                <span class="comment-content">%s</span>
                <span class="comment-date">%s</span>
                </div>''' % (margin_val,p.user.name, p.comment, p.date)
        if v is not None:
            r += insert_comment_node(v,margin_val+20)
        html+=r
    return html

@register.simple_tag
def build_comment_tree(tree_data):

    html_ele = ""
    for p,v in tree_data.items():
        row = '''
        <div stype="margin-top:15px;border-left:1px dashed green;border-bottom:1px dashed green">
        <span class="comment-user">%s</span>
        <span class="comment-content">%s</span>
        <span class="comment-date">%s</span>
        </div>''' % (p.user.name,p.comment,p.date)

        if v is not None:
            row += insert_comment_node(v,10)
        html_ele += row
    return html_ele