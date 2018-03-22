
import models
from s10day12bbs import settings
class ArticleGen(object):
    def __init__(self,request):
        self.request = request

    def parse_data(self):
        form_data = {
        "title" : self.request.POST.get("title"),
        "content" : self.request.POST.get("content"),
        "category_id" : 1,
            "summary":self.request.POST.get("summary"),
            "author_id":self.request.user.userprofile.id,
            "head_img":"",
        }
        return form_data

    def create(self):
        self.data = self.parse_data()
        bbs_obj = models.Article(**self.data)
        bbs_obj.save()
        file_name = handle_upload_file(self.request,self.request.FILES["head_img"])
        bbs_obj.head_img = "imgs/upload/%s" % file_name
        bbs_obj.save()
        return bbs_obj
    def update(self):
        pass

def handle_upload_file(request, file_obj):
    upload_dir = '%s/%s' % (settings.BASE_DIR, settings.FileUploadDir)
    # if not os.path.isdir(upload_dir):
    #    os.mkdir(upload_dir)
    print '-->', dir(file_obj)
    with open('%s/%s' % (upload_dir, file_obj.name), 'wb') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

    return file_obj.name


def recursive_search(data_dic,comment):
    for parent,v in data_dic.items():
        if parent == comment.parent_comment:
            print "find parent of [%s]" % comment
            data_dic[comment.parent_comment][comment] = {}
        else:
            print "Cannot find [%s]'s parent, going to further layer" % comment
            recursive_search(data_dic[parent],comment)


def build_comments_tree(request):
    bbs_obj = models.Article.objects.first()
    tree_dic = {}
    for comment in bbs_obj.comment_set.select_related().order_by("id"):
        if not comment.parent_comment: # first layer
            tree_dic[comment] = {}
        else:
            recursive_search(tree_dic,comment)

    return tree_dic
    for k,v in tree_dic.items():
        print "-->",k,v