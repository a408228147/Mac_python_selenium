import logging
import os.path
import time

class Logger(object):

    def __init__(self,logger):
        '''
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定文件中
        :param logger:
        '''
        #创建一个logger,设置等级输出为DEBUG logger：测试用例的对象 类名
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler ，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        #log_path = os.path.dirname(os.getcwd())+'/Logs/'#项目根目录下/Log 保存日志
        log_path = os.path.dirname(os.path.abspath('.'))+'/logs/'
        log_name = log_path+rq +'.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        #再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handler 的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger