#!/usr/bin/env python
#coding=utf-8

import re,sys
from urllib import urlopen
from Queue import Queue
from threading import Thread
from time import strftime

baseUrl='http://www.hackdig.com/?p='
outPut='hackdigdoclist.html'
pageNum=3
threadNum=10
urlList=[]
threadList=[]
urlNum=0

def spiderIndex(url):
    global urlNum
    try:
        res=urlopen(url)
    except Exception,e:
        print '[-] [%s] [Error] [%s]'

    if res.getcode()==200:
        html=res.read()
        lines=html.split('\n')
        for line in lines:
            print line 
            #rex=re.search(r'(<dt><a href=\")(http://www.freebuf.com/tools/\d*\.html)(\" target=\"_blank\">).*',line)
            rex=re.search(r'(<h2><a rel=\"bookmark\")(href=\".*\"\.htm).*',line)
            if rex !=None:
                urlNum+=1
                print rex.group(1),rex.group(2),rex.group(3)
                urlList.append(rex.group())
                sys.stdout.write('\r[*] [%s] [Working] [%s]'%(str(strftime('%X')),str(urlNum)))


class WorkThread(Thread):

    def __init__(self,q):
        Thread.__init__(self)
        self.q=q

    def run(self):
        while True:
            if self.q.empty()==True:
                break
            _url=baseUrl+str(self.q.get())
            spiderIndex(_url)


def main():
    q=Queue(maxsize=0)
    for i in xrange(1,pageNum,1):
        q.put(i)

    print '[+] [%s] [Start]'%strftime('%X')

    #spiderIndex('http://www.freebuf.com/tools')

    for i in xrange(threadNum):
        t=WorkThread(q)
        threadList.append(t)

    for i in threadList:
        i.start()

    for i in threadList:
        i.join()

    f=open(outPut,'ab')
    f.write('<meta http-equiv="Content-Type" content="text/html";charset=utf-8 />\n')
    f.write('<title>hackdig  List</title>\n')
    f.write('<center><h1><b>Freebuf Tools List</b></h1>\n'+'Time:'+str(strftime("%Y-%b-%d %X"))+'Count:'+str(len(urlList))+'</center><hr/>\n<h5>\n')
    for line in urlList:
        f.write(line+'</br>\n')
    f.close()

    print '\n[+] [%s] [End] [All Done!]'%strftime('%X')
    print '[+] [%s] [Save As] [%s]'%(strftime('%X'),outPut)


if __name__=='__main__':
    main()
