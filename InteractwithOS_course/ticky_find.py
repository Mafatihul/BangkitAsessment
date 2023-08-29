# import library
import sys
import csv
import re
from collections import OrderedDict

# Report the error per type and input to dictionary
def get_error(file):
   err_messages = []
   count_err = {}
   with open(file, 'r') as f:
      for line in f.readlines():
        messages = re.search(r"ERROR ([\w\s]*)", line)
        if messages != None:
           err_messages.append(messages[1])
      f.close()
   for err in err_messages:
       if err in count_err:
        count_err[err] += 1
       else:
         count_err[err] = 1
   sorted_err = dict(sorted(count_err.items(), reverse=True))
   with open("error_message.csv", 'w') as f:
      writer = csv.DictWriter(f, fieldnames=["Error", "Count"])
      writer.writeheader()
      [f.write("{0}, {1}\n".format(key,value)) for key,value in sorted_err.items()]
   return sorted_err

# Mengumpulkan error log dan count per username dan jenisnya
def get_users(file):
   per_user = {}
   users = []
   with open(file, 'r') as f:
      for line in f.readlines():
         result = re.search("(ERROR|INFO).+\(([\w\.]+)\)", line)
         if result is None:
            continue
         category = result.groups()[0]
         username = str(result.groups()[1])
         if category == "INFO":
            if username in per_user:
               log = per_user[username]
               log[category] += 1
            else:
               per_user[username] = {'INFO':1, 'ERROR':0}
         if category == "ERROR":
            if username in per_user:
               log = per_user[username]
               log[category] += 1
            else:
               per_user[username] = {'INFO':0, 'ERROR':1}
   sorted_user = sorted(per_user.items())
   return sorted_user

print(get_error('InteractwithOS_course\syslog.txt'))
# def generate_report()

# if __init__ == '__main__':