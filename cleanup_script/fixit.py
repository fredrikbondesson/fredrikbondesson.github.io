import sys


def fix_none_in_file(file_name):
  with open(file_name) as file: # Use file to refer to the file object
    data = file.readline()
    prev_value = None
    buffer = data.rstrip("\n\r")
    while data:
      csv_parts = data.split(',')
      if 'None' in data:
        if prev_value != None and prev_value != 'None':
          buffer = buffer.replace('None', prev_value)

      if csv_parts[1] != None and csv_parts[1] != 'None':
        prev_value = csv_parts[1]
      data = file.readline()
      print buffer
      buffer = data.rstrip("\n\r")

      
def fix_missing_column_in_file(file_name):
  with open(file_name) as file: # Use file to refer to the file object
    data = file.readline()
    prev_value = None
    buffer = data.rstrip("\n\r")
    while data:
      csv_parts = buffer.split(',')
      if len(csv_parts) != 3:
        csv_parts.insert(1, prev_value)
        buffer = ','.join(csv_parts)
      else:
        prev_value = csv_parts[1]
      
      data = file.readline()
      print buffer
      buffer = data.rstrip("\n\r")


def check_order(file_name):

#2016-02-02 19:13:25,37.64,1.72,0.00
#                 2016-02-02 19:13:25
#date_time_str = '2018-06-29 08:15:27.243860'
#date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

#print('Date:', date_time_obj.date())
#print('Time:', date_time_obj.time())
  import datetime
  prev_value = None
  with open(file_name) as file: # Use file to refer to the file object
    data = file.readline()
    data = file.readline()
    while data:
      csv_parts = data.split(',')
      # if timestamp like 2016-02-02 19:13:25
      date_time_obj = datetime.datetime.strptime(csv_parts[0], '%Y-%m-%d %H:%M:%S')
      # if timestamp like 2017-06-08 22:10
      #date_time_obj = datetime.datetime.strptime(csv_parts[0], '%Y-%m-%d %H:%M')
      if prev_value != None and date_time_obj < prev_value:
        print "data=" + str(date_time_obj)
        print "prev_value=" + str(prev_value)
      prev_value = date_time_obj
      data = file.readline()
    
def main():
  if len(sys.argv) >= 2:
    file_name = sys.argv[1]
    
    #fix_none_in_file(file_name)
    
    # Note that nr of columns might need to be adjusted
    #fix_missing_column_in_file(file_name)
    
    check_order(file_name)

  
if __name__== "__main__":
  main()