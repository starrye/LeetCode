import re

m = 7
n = 3

# def xx(i, j):
#     if i == 1 or j == n:
#         return 1
#     else:
#         return xx(i - 1, j) + xx(i, j + 1)
#
# a = xx(7,1)
# print(a)
from logging.handlers import TimedRotatingFileHandler
import os, logging, datetime

# if not os.path.isdir(logdir):
#         cmd = 'mkdir -p %s' % logdir
#         run_cmd(cmd)
# logdate = datetime.datetime.now().strftime("%Y%m%d")
# logfile = logdir + logdate + ".log"
# def init_log():
#     logger = logging.getLogger()
#     # 指定记录器将处理的最低严重性日志信息
#     logger.setLevel(logging.INFO)
#     datefmt = '%Y-%m-%d %H:%M:%S'
#     # 以下消息格式字符串将以人类可读的格式记录时间，消息的严重性以及消息的内容
#     format_str = '%(asctime)s - %(levelname)s - %(message)s'
#     # format_str：消息格式字符串 datefmt：日期格式字符串
#     formatter = logging.Formatter(format_str, datefmt)
#
#     # when是单位 interval是间隔 backupCount会自动删除30+when之前的日志文件
#     #handle = TimedRotatingFileHandler(logfile, when='d', interval=1, backupCount=30)
#     # 选择此处理程序要使用的Formatter对象
#     #handle.setFormatter(formatter)
#     # 从记录器对象中添加 处理程序 对象
#     #logger.addHandler(handle)
#
#     console = logging.StreamHandler()
#     console.setFormatter(formatter)
#     console.setLevel(level=logging.INFO)
#     logger.addHandler(console)
#     return logger
#
# bigdata_logger = init_log()
# bigdata_logger.info('---------info')
# bigdata_logger.error('---------error')
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 栈的利用
        result = [0] * len(T)
        stack = []
        for index, value in enumerate(T):
            if not stack or value <= stack[-1][1]:
                stack.append([index, value])
            else:
                while True:
                    if stack:
                        pre_T = stack[-1][1]
                        if pre_T < value:
                            result[stack[-1][0]] = index - stack[-1][0]
                            stack.pop()
                        else:
                            stack.append([index, value])
                            break
                    else:
                        stack.append([index, value])
                        break
        return result


a = Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
print(a)