import os
import shutil
import logging
import logging.config
import platform

LOG_CONFIG_FILENAME = "log.ini"
LOG_FILENAME = "d810.log"
Z3_TEST_FILENAME = "z3_check_instructions_substitution.py"

def check_platform():
    return platform.system() == "Windows"

def normalize_path_for_Windows(path):
    return path.replace('\\', '/')

def clear_logs(log_dir):
    shutil.rmtree(log_dir, ignore_errors=True)

def configure_loggers(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    log_main_file = os.path.join(log_dir, LOG_FILENAME)
    z3_test_file = os.path.join(log_dir, Z3_TEST_FILENAME)
    log_conf_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), LOG_CONFIG_FILENAME)
    if check_platform():
        log_main_file=normalize_path_for_Windows(log_main_file)
        z3_test_file=normalize_path_for_Windows(z3_test_file)
    logging.config.fileConfig(log_conf_file, defaults={"default_log_filename": log_main_file,
                                                       "z3_log_filename": z3_test_file})
    z3_file_logger = logging.getLogger('D810.z3_test')
    z3_file_logger.info("from z3 import BitVec, BitVecVal, UDiv, URem, LShR, UGT, UGE, ULT, ULE, prove\n\n")
