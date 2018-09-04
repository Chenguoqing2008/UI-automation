# encoding=utf-8
import os
import platform

home_path = os.getcwd().split('src')[0]
if 'Ubuntu' in platform.platform() or 'Darwin' in platform.platform():
    tmp_path = os.getcwd().split('public')[0] + '/tmp/'
    chrome_driver_path = home_path + 'testdata/chromedriver'
    log_path = home_path+'log/'
    config_path = home_path+"testdata/"
else:
    tmp_path = os.getcwd().split('public')[0] + '\\tmp\\'
    chrome_driver_path = os.path.join(os.path.join(home_path, 'testdata'), 'chromedriver.exe')
    ie_driver_path = 'C:\\workspace\\IEDriverServer.exe'
    log_path = home_path+'log\\'
    config_path = home_path+"testdata\\"



