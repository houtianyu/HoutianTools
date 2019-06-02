import logging,datetime,os
class Logs:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        base_dir_path = os.path.dirname(os.path.dirname(__file__)) + '\\files\\toolslogs\\httoolsSystemFunction'
        log_file_dir = base_dir_path + '_' + datetime.datetime.now().strftime('%Y_%m_%d') + '.log'
        self.file_logs = logging.FileHandler(log_file_dir,'a',encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelno)s %(levelname)s<->%(message)s')
        self.file_logs.setFormatter(formatter)
        self.logger.addHandler(self.file_logs)
    def get_logger(self):
        return self.logger
    def close_log(self):
        self.file_logs.close()
        self.logger.removeHandler(self.file_logs)
    def LogsSave(self,msg_content,level_info=None):
        logging = self.get_logger()
        if level_info == 'info':
            logging.info(msg_content)
        if level_info == 'debug':
            logging.debug(msg_content)
        if level_info == 'warning':
            logging.warning(msg_content)
        if level_info == 'error':
            logging.error(msg_content)
        if level_info == 'critical':
            logging.critical(msg_content)
        else:
            logging.debug(msg_content)