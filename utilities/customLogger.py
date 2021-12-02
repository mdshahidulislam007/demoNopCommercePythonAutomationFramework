import logging

class LogGen:
    @staticmethod
    def loggen():
        #logging.basicConfig(filename=".\\Logs\\automation.log",
                            #format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.basicConfig(filename="automation.log", level=logging.INFO)
        lg = logging.getLogger()
        return lg
