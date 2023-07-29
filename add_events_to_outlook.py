# v4
# Writes to online archive but nothing else. May need to drag and drop events on to shared calendar. 
# Enterpise Outlook account gets routed back to the online archive so further development may need to involve IT
# Import events from an excel spreadsheet to an Outlook calendar
# Added start and end time variables that correspond with columns in csv.
# Added block to combine time and date since they are now separate fields
# install dependencies using command prompt (ex. pip install pytz)

import csv
import datetime
import pytz
import win32com.client as win32


def add_events_to_outlook(csv_file, calendar_name):
    # Connect to outlook
    outlook = win32.Dispatch('Outlook.Application')
    namespace = outlook.GetNamespace('MAPI')
    
    # Print calendar names for debugging
    print("Available Calendars:")
    for folder in namespace.Folders:
        print(folder.Name)
        
    
    # Find the calendar by name
    calendar_name = "Kyle.Smiley@usda.gov"
    for folder in namespace.Folders:
        if folder.Name ==  calendar_name: #"Kyle.Smiley@usda.gov":
            for subfolder in folder.Folders:
                if subfolder.Name == calendar_name:
                    calendar_name == subfolder
                    break
                break
        
        if calendar_name is None:
            print(f"Calendar ' {calendar_name} ' not found.")
            return
        
    # Get system timezone  #added
    system_timezone = pytz.timezone(pytz.country_timezones['US'][10])
    
    # Read events from CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row if present
        for row in reader:
            TrainingName, start_date_str, end_date_str, start_time_str, end_time_str, description = map(str.strip, row)
            
            # Parse date and time strings
            start_datetime = datetime.datetime.strptime(start_date_str + " " + start_time_str, "%m/%d/%Y %I:%M:%S %p")
            end_datetime = datetime.datetime.strptime(end_date_str + " " + end_time_str, "%m/%d/%Y %I:%M:%S %p")
            
            # Adjust timezone by subtracting 3 hours
            start_datetime -= datetime.timedelta(hours=3)
            end_datetime -= datetime.timedelta(hours=3)
            
            # Convert the datetime objects to the system timezone
            start_datetime = system_timezone.localize(start_datetime)
            end_datetime = system_timezone.localize(end_datetime)
            
            # Convert the datetime objects to UTC timezone
            start_datetime_utc = start_datetime.astimezone(pytz.UTC)
            end_datetime_utc = end_datetime.astimezone(pytz.UTC)
            
            # Create a new event
            appointment = outlook.CreateItem(1)  # 1 represents an appointment item
            
            appointment.Subject = TrainingName
            appointment.Start = start_datetime_utc
            appointment.End = end_datetime_utc
            appointment.Body = description
            
            # Save the event to the calendar
            appointment.Save()
            print(f"Event '{TrainingName}' added to the ' {calendar_name} 'outlook calendar.")
            
    print("All events added successfully")
    
    # example
    # csv_file = "event.csv"  # provide path to csv
    # add_events_to_outlook(csv_file)
            

            
        