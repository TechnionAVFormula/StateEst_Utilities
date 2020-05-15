from enum import Enum

## import depanding on running state / configuration state:
from config import CONFIG, ConfigEnum, IS_DEBUG_MODE 
from Messages import messages , NoFormulaMessages

# if (CONFIG == ConfigEnum.REAL_TIME) or (CONFIG == ConfigEnum.COGNATA_SIMULATION):
#     from pyFormulaClient import messages
#     from pyFormulaClient.MessageDeque import NoFormulaMessages
# elif CONFIG == ConfigEnum.LOCAL_TEST:
#     from pyFormulaClientNoNvidia import messages
#     from pyFormulaClientNoNvidia.MessageDeque import NoFormulaMessages
# else:
#     raise NameError("User Should Choose Configuration from config.py")


class ConeType(Enum):
    YELLOW      = messages.perception.Yellow
    BLUE        = messages.perception.Blue
    ORANGE_BIG  = messages.perception.OrangeBig
    ORANGE_SMALL= messages.perception.Orange
    UNKOWN      = messages.perception.UnknownType
