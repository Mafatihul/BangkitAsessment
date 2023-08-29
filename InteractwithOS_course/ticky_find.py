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
   sorted_user = [("USERNAME", "INFO", "ERROR")] + sorted(per_user.items())
   with open("user_statistics.csv", "w") as user_file:
       for line in sorted_user:
           if isinstance(line[1], dict):
            user_file.write("{}, {}, {}\n".format(line[0], line[1].get("INFO"), line[1].get("ERROR")))
           else:
              user_file.write("{}, {}, {}\n".format(line[0], line[1], line[2]))
   return sorted_user

def main():
   file = 'InteractwithOS_course\syslog.txt'
   get_error(file)
   get_users(file)

main()