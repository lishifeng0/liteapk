import sys,re,os
a=sys.argv[1]
p0=a+r'\res'

def r0(p):
	f=open(p0+p,'r')
	s=f.read()
	f.close()
	return s

l=r0(r'\values\public.xml')
l=re.findall('(?<=<public type="drawable" name=")[\w\.]+?(?=" id="0x\w+?" />)',l)


d1={}

for d in os.listdir(p0):
	if d.startswith('drawable') or d.startswith('mipmap'):
		p1=p0+'\\'+d
		for f in os.listdir(p1):
			for z in ['.9.png','.png','.jpg','.gif']:
				if f.endswith(z):
					i=f[:-len(z)]
					if i in l:
						p=p1+'\\'+f
						s=os.path.getsize(p)
						if i in d1:
							if s>=d1[i][0]:
								os.remove(p)
								print d+'\\'+f
								break
							else:
								os.remove(p0+'\\'+d1[i][1])
								print d1[i][1]
						d1[i]=(s,d+'\\'+f)
						break
		if len(os.listdir(p1))==0:os.rmdir(p1)
# for d in os.listdir(p0):						
	# p1=p0+'\\'+d
	# if len(os.listdir(p1))==0:os.rmdir(p1)		