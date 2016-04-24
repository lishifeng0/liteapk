import sys,re,os
l=['\.line \w*','\.prologue','nop']
#l+=['\.(?:end |restart )?local [vp]\d+.+?','\.param p\d+.+?','\.end param','\.annotation[\w\W]+?\.end annotation']

l=[re.compile('[\r\n]\s*'+i+'\s*[\r\n]') for i in l]
l+=[re.compile('const\S* (v\d+,).+\s*(?=const\S* \\1)')]

p0=sys.argv[1]
lp=len(p0)
for a in os.listdir(p0):
	if re.search('^smali(?:_classes\d+)?$',a):
		for root,dirs,files in os.walk(p0+'\\'+a):
			for name in files:                        
				p=os.path.join(root,name)
				f=open(p,'r')
				s=f.read()
				f.close()
				b=False		
				for i in l:
					if not b:b=i.search(s)
					while i.search(s):s=i.sub('\r\n',s)
				if b:
					print p[lp:]
					f=open(p,'w')
					f.write(s)
					f.close()