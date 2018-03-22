
import Queue
import datetime

class Chat(object):
    def __init__(self):
        self.msg_queue = Queue.Queue()

    def get_mmsg(self,request):
        new_msgs = []
        if self.msg_queue.qsize() > 0:
            for msg in range(self.msg_queue.qsize()):
                new_msgs.append(self.msg_queue.get_nowait())
        else: #no new message, but wait for 60 secs
            try:
                print "------ no new msg. going to wait for 60 seconds---%s--%s--" % (datetime.datetime.now().strftime("%Y%m%d %H:%M:%S"),request.user.userprofile.name)
                new_msgs.append(self.msg_queue.get(timeout=60))
                print "\033[33;1m Found new message\033[0m", new_msgs
            except Queue.Empty:
                print "\033[31;1m Time out, no new message for user [%s]\033[;0m" % (request.user.userprofile.name)
                return new_msgs
        print "\033[33;1m Found [%s] new messages\033[0m" % (len(new_msgs))
        return new_msgs