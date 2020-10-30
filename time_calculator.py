def add_time(start, duration):

  start_time, am_pm = start.split() 
  note = ""

  hour = int(start_time.split(':')[0])
  minute = int(start_time.split(':')[1])
  duration_hours = int(duration.split(':')[0])
  duration_minutes =  int(duration.split(':')[1])

  new_minute = int(minute) + int(duration_minutes)
  if new_minute > 60:
    duration_hours = duration_hours + 1
    new_minute = new_minute - 60

  days = 0
  for h in range (duration_hours):
    hour = hour + 1
    if hour == 12:
      

  

  if new_hour >= 12:
    if am_pm == "AM":
      am_pm = "PM"
    else:
      am_pm = "AM"
    if new_hour > 12:
      new_hour = new_hour - 12

  new_time = str(new_hour) + ":" + str(new_minute).zfill(2) + " " + am_pm + " " + note
  return new_time