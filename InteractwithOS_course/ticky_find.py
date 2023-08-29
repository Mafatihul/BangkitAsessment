# import library
import sys
import csv
import re
import subprocess

# inisialisasi dictionary 
# untuk menampung jumlah eror berdasarkan jenisnya
# type_error_count = dict()
# count_error = int()
# error_type = []
# username = []

#  with open('syslog.txt', 'r') as f:
#     for line in f.readlines():
#       message = re.search(r"ERROR ([\w\s]*).\(([\w]*)\)", line)
#        if message != None:
#           type_error_count[message[1]]
#           # username.append(message[2])
#     f.close()

# print(type_error_count)

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
   return sorted(count_err.items(), reverse=True)

print(get_error('InteractwithOS_course\syslog.txt'))

# def get_users(file):

# def generate_report()