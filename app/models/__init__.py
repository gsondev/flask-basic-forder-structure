from cuid2 import Cuid
import pytz

CUID_LENGTH: int = 24
CUID: Cuid = Cuid(length=CUID_LENGTH)

UTC_TIME = pytz.timezone("America/Bogota")
