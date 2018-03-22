from django.shortcuts import render,HttpResponseRedirect,HttpResponse
import json,datetime
# Create your views here.
import utils
import models
from django.core.exceptions import ObjectDoesNotExist

global_msg_dic = {}

def dashboard(request):
    return render(request,'webqq/dashboard.html')

def send_msg(request):

    print request.POST
    data =  request.POST.get("data")
    data = json.loads(data)
    data["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    to_id = data.get("to_id")
    user_obj = models.bbs_models.UserProfile.objects.get(id=to_id)
    contact_type = data.get("contact_type")
    if contact_type == "single":
        if not global_msg_dic.has_key(to_id):
            global_msg_dic[to_id] = utils.Chat()
        global_msg_dic[to_id].msg_queue.put(data)
        print "\033[31;1mPush msg [%s] into user [%s] queue" % (data["msg"],user_obj)
    elif contact_type == "group":
        group_obj = models.QQGroup.objects.get(id = to_id)
        for member in group_obj.members.select_related():
            if member.id != request.user.userprofile.id:
                if not global_msg_dic.has_key(member.id):
                    global_msg_dic[member.id] = utils.Chat()
                global_msg_dic[member.id].msg_queue.put(data)
                print "\033[31;1mPush msg [%s] into user [%s] queue" % (data["msg"], member.name)
    return HttpResponse("dddddddddddddd")


def get_msg(request):
    uid = request.GET.get("uid")
   # new_msgs = []
    if uid:
    #     try:
    #         if not global_msg_dic.has_key(uid):
    #             global_msg_dic[uid] = utils.Chat()
    #         new_msgs = global_msg_dic[uid].get_msg(request)
    #     except ObjectDoesNotExist,e:
    #         print '\033[41;1m%s\033[0m' % str(e)
    # return HttpResponse(json.dumps(new_msgs))
        res = []
        if not global_msg_dic.has_key(uid):
            global_msg_dic[uid] = utils.Chat()
        res = global_msg_dic[uid].get_mmsg(request)
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps("uid not provided"))