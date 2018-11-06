# read a file name from user which has content like the one given below. Output the host name and count of queries made separated by space:

## File contents example:
# unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0
# burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0
# burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0
# d104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
# unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
# unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786
# unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204
# d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310
# d104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786

## Ouptput example:
# unicomp6.unicomp.net 4
# burger.letters.com 3
# d104.aa.net 3

filename = input()
file = open(filename, "r") 
hosts = {}

# read from file and create dictionary
for line in file:
    entries = line.split(" ")
    
    if entries[0] in hosts:
        hosts[entries[0]] = 0
    hosts[entries[0]] += 1
    
    if entries[0] not in hosts:
        hosts[entries[0]] = 0
    hosts[entries[0]] += 1
file.close()

# write to file
f = open("records_"+filename, "w")
for key in hosts.keys():
    f.write(key + " " + str(hosts[key]) + "\n")
f.close()