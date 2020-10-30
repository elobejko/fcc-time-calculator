def add_time(start, duration, day = None):

  start_time, am_pm = start.split() 
  note = ""
  
  hour = int(start_time.split(':')[0])
  minute = int(start_time.split(':')[1])
  duration_hours = int(duration.split(':')[0])
  duration_minutes =  int(duration.split(':')[1])

  new_minute = minute + duration_minutes
  if new_minute > 60:
    duration_hours = duration_hours + 1
    new_minute = new_minute - 60

  days = int(duration_hours / 24)
  for h in range (duration_hours%24):
    hour = hour + 1
    if hour == 12:
      if am_pm == "AM":
        am_pm = "PM"
      else:
        am_pm = "AM"
        days = days + 1
    if hour > 12:
      hour = 1

  if days == 1:
    note = " (next day)"
  if days > 1:
    note = " (" + str(days) + " days later)"

  new_time = str(hour) + ":" + str(new_minute).zfill(2) + " " + am_pm + note

  if day != None:
    week = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    ii = [d.lower() for d in week].index(day.lower())
    new_time = str(hour) + ":" + str(new_minute).zfill(2) + " " + am_pm + ", " + week[(ii + days)%7] + note

  return new_time