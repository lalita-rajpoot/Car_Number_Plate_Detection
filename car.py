#!/usr/bin/python3
import cgi
import os
import subprocess as sp
print("content-type: text/html")
print()
f=cgi.FieldStorage()
cmd = f.getvalue("x")

if cmd == "256 D 259":
	print('''<pre>
	Car Number: 256 D 259
	Car Model: BMW	
	Registration Name: Amith
	Registration Date: 11/1/2010
	Fuel Type: CNG
	Location: Delhi, India
	Vehicle Class: SUV
	Insurance Upto: 19/12/2022
	</pre>''')
elif cmd == "B 2228HM":
	print('''<pre>
	Car Number: B 2228HM
	Car Model: BMW	
	Registration Name: Ram
	Registration Date: 17/1/2013
	Fuel Type: CNG
	Location: Amritsar, India
	Vehicle Class: SUV
	Insurance Upto: 19/12/2026
	</pre>''')

elif cmd == "TTL D4FTY":
	print('''<pre>
	Car Number: TTL D4FTY
	Car Model: BMW	
	Registration Name: Suman
	Registration Date: 17/1/2012
	Fuel Type: CNG
	Location: TamilNadu, India
	Vehicle Class: SUV
	Insurance Upto: 19/12/2022
	</pre>''')
elif cmd == "UP15CU8383":
	print('''<pre>
	Car Number: GD70 EEO
	Car Model: BREZZA VDI AMT	
	Registration Name: Shani Deshwal
	Registration Date: 29/11/2018
	Fuel Type: DIESEL
	Location: Uttar predesh, India
	Vehicle Class: Motor car
	Insurance Upto: 27/10/2019
	</pre>''')
