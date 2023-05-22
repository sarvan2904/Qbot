_VERSION = 8
_PRESERVE_FILES = (
'_ioty_name',
'_ioty_network',
'boot.py',
'ioty',
'ioty/ble.py',
'ioty/constants.py',
'ioty/http.py',
'ioty/monitor.py',
'ioty/monitor_mqtt.py',
'ioty/mqtt.py',
'ioty/neopixel.py',
'ioty/pin.py',
'ioty/html',
'ioty/html/index.html',
'umqtt',
'umqtt/robust.py',
'umqtt/simple.py'
)
_NETWORK_CONFIGURATION_FILE = '_ioty_network'

_MODE_OPEN = 1
_MODE_APPEND = 2
_MODE_CLOSE = 3
_MODE_DELETE_ALL = 4
_MODE_GET_VERSION = 5
_MODE_LIST = 6
_MODE_READ = 7
_MODE_DELETE = 8
_MODE_UPDATE = 9
_MODE_FILE_HASH = 10
_MODE_WRITE_FILES = 11
_MODE_GET_INFO = 12
_MODE_MKDIR = 13

_STATUS_SUCCESS = 0
_STATUS_PENDING = 1
_STATUS_FAILED = 2
_STATUS_CHECKSUM_ERROR = 3
_STATUS_ERROR = 4
