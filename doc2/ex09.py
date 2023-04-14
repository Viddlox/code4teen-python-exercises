from datetime import datetime
import pytz

local_timezone = pytz.timezone('Asia/Singapore')
local_time = datetime.now(local_timezone)
print(local_time.time())
