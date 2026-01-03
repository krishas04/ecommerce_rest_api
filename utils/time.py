from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def now_utc():
  """Return the current UTC time (aware datetime)."""
  return datetime.now(timezone.utc)

def get_local(utc_dt:datetime,tz_name:str="Asia/Kathmandu"):
  """Convert a UTC datetime to the given local timezone."""
  return utc_dt.astimezone(ZoneInfo(tz_name))

def normalize_to_utc(dt:datetime):
  if dt.tzinfo==None:
    return dt.replace(tzinfo=timezone.utc)
  return dt.astimezone(timezone.utc)