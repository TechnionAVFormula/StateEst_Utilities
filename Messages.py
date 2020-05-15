## import depanding on running state / configuration state:
from config import CONFIG, ConfigEnum, IS_DEBUG_MODE 

if (CONFIG == ConfigEnum.REAL_TIME) or (CONFIG == ConfigEnum.COGNATA_SIMULATION):
    from pyFormulaClient import messages
    from pyFormulaClient.MessageDeque import NoFormulaMessages
elif CONFIG == ConfigEnum.LOCAL_TEST:
    from pyFormulaClientNoNvidia import messages
    from pyFormulaClientNoNvidia.MessageDeque import NoFormulaMessages
else:
    raise NameError("User Should Choose Configuration from config.py")

IMPROT_messages = messages
IMPROT_NoFormulaMessages = NoFormulaMessages
NoFormulaMessages = NoFormulaMessages
messages = messages

def get_messages():
    return messages

def  get_NoFormulaMessages():
    return NoFormulaMessages