import logging

class Loggen:

    # @staticmethod
    # def get_log():
    #     logging.basicConfig(filename="automation.txt",filemode='w',
    #                         format='%(asctime)s:%(levelname)s:%(message)s',
    #                         datefmt='%d/%m/%Y%I:%M:%S%p'
    #                         )
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     print('Get Log Method : ',logger)
    #     return logger

    @staticmethod
    def loggen():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(filename=r'../logs/automation.log')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger

