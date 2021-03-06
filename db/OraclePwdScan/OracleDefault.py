#-*- coding:utf-8 -*-
import sys
import getopt 
import time
import re
import cx_Oracle
import telnetlib
from cx_Oracle import DatabaseError

#cx_oracle:http://cx-oracle.sourceforge.net/

pe = re.compile(r'^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$')

def Usage():
    print '''
    ####################################################################
    #                                                                  #
    #             Oracle Default User and Password Sc4nner             #
    #                           By : Gavin                             #
    #                                                                  #
    ####################################################################
    Usage:
        python OracleDefault.py -t [target] 
    Option:
        -d [database] The Database which you Want to connect Oracle(orcl).
        -p [port]     Oracle service port,Default number is 1521.
    --------------------------------------------------------------------
    Warn:
        target     -->  Must be IP.example:192.168.1.x .
    --------------------------------------------------------------------
    '''
    sys.exit()

def oraclelogin(target,user,password,database,port):
    print "[+] Trying Default User and Password (%s----->%s)" % (user,password)
    try:
        conn = cx_Oracle.connect(user,password,cx_Oracle.makedsn(target,port,database))
        conn.close()
	return (True,user,password)
    except DatabaseError:
        try:
            conn = cx_Oracle.connect(user,password,cx_Oracle.makedsn(target,port,database),cx_Oracle.SYSDBA)
            conn.close()
            return (True,user,password)
        except:
            return (False,user,password)
    except:
        return (False,user,password)
    
def main():
    port = 1521
    database = 'orcl'
    try:
        opts,args = getopt.getopt(sys.argv[1:],"t: p: d:")
    except: 
        Usage()
    if len(opts) < 1:
        Usage()
    for o,a in opts:
        if o == "-t":
            target = a
        if o == "-p":
            port = int(a)
        if o == "-d":
            database = a 
    if pe.match(target) == None:
        print "\r-------------------------------------------------"
        print "[!]Enter the target error,it Must be IP."
        sys.exit()
    try:
        tn = telnetlib.Telnet()
        tn.open(target,port)
        tn.close()        
    except:
        print "\r-------------------------------------------------"
        print "\r[!] Can not connect to the target!"
        tn.close()
        sys.exit()
    data = {
        'UOP_CEN1':'uopcen1dev',
        'BRIO_ADMIN':'BRIO_ADMIN',
        'BRUGERNAVN':'ADGANGSKODE',
        'BRUKERNAVN':'PASSWORD',
        'BSC':'BSC',
        'BUG_REPORTS':'BUG_REPORTS',
        'CALVIN':'HOBBES',
        'CATALOG':'CATALOG',
        'CCT':'CCT',
        'CDEMO82':'CDEMO82',
        'CDEMO82':'CDEMO83',
        'CDEMOCOR':'CDEMOCOR',
        'CDEMORID':'CDEMORID',
        'CDEMOUCB':'CDEMOUCB',
        'CDOUGLAS':'CDOUGLAS',
        'CE':'CE',
        'CENTRA':'CENTRA',
        'CENTRAL':'CENTRAL',
        'CIDS':'CIDS',
        'CIS':'CIS',
        'CIS':'ZWERG',
        'CISINFO':'CISINFO',
        'CISINFO':'ZWERG',
        'CLARK':'CLOTH',
        'CN':'CN',
        'COMPANY':'COMPANY',
        'COMPIERE':'COMPIERE',
        'CQSCHEMAUSER':'PASSWORD',
        'CQUSERDBUSER':'PASSWORD',
        'CRP':'CRP',
        'CS':'CS',
        'CSC':'CSC',
        'CSD':'CSD',
        'CSE':'CSE',
        'CSF':'CSF',
        'CSI':'CSI',
        'CSL':'CSL',
        'CSMIG':'CSMIG',
        'CSP':'CSP',
        'CSR':'CSR',
        'CSS':'CSS',
        'CTXDEMO':'CTXDEMO',
        'CTXSYS':'CHANGE_ON_INSTALL',
        'CTXSYS':'CTXSYS',
        'CUA':'CUA',
        'CUE':'CUE',
        'CUF':'CUF',
        'CUG':'CUG',
        'CUI':'CUI',
        'CUN':'CUN',
        'CUP':'CUP',
        'CUS':'CUS',
        'CZ':'CZ',
        'DBI':'MUMBLEFRATZ',
        'HR':'CHANGE_ON_INSTALL',
        'HR':'HR',
        'HRI':'HRI',
        'HVST':'HVST',
        'HXC':'HXC',
        'HXT':'HXT',
        'IBA':'IBA',
        'IBE':'IBE',
        'IBP':'IBP',
        'IBU':'IBU',
        'IBY':'IBY',
        'ICDBOWN':'ICDBOWN',
        'ICX':'ICX',
        'IDEMO_USER':'IDEMO_USER',
        'IEB':'IEB',
        'IEC':'IEC',
        'IEM':'IEM',
        'IEO':'IEO',
        'IES':'IES',
        'IEU':'IEU',
        'IEX':'IEX',
        'IFSSYS':'IFSSYS',
        'IGC':'IGC',
        'IGF':'IGF',
        'IGI':'IGI',
        'IGS':'IGS',
        'IGW':'IGW',
        'IMAGEUSER':'IMAGEUSER',
        'IMC':'IMC',
        'IMEDIA':'IMEDIA',
        'IMT':'IMT',
        '#INTERNAL':'ORACLE',
        '#INTERNAL':'SYS_STNT',
        'INTERNAL':'ORACLE',
        'INTERNAL':'SYS_STNT',
        'INV':'INV',
        'IPA':'IPA',
        'IPD':'IPD',
        'IPLANET':'IPLANET',
        'ISC':'ISC',
        'ITG':'ITG',
        'JA':'JA',
        'JAKE':'PASSWO4',
        'JE':'JE',
        'JG':'JG',
        'JILL':'PASSWO2',
        'JL ':'JL ',
        'JMUSER':'JMUSER',
        'JOHN':'JOHN',
        'JONES':'STEEL',
        'JTF':'JTF',
        'JTM':'JTM',
        'JTS':'JTS',
        'JWARD':'AIROPLANE',
        'KWALKER':'KWALKER',
        'L2LDEMO':'L2LDEMO',
        'LBACSYS':'LBACSYS',
        'LIBRARIAN':'SHELVES',
        'MANPROD':'MANPROD',
        'MARK':'PASSWO3',
        'MASCARM':'MANAGER',
        'MASTER':'PASSWORD',
        'MDDATA':'MDDATA',
        'MDDEMO':'MDDEMO',
        'MDDEMO_CLERK':'CLERK',
        'MDDEMO_CLERK':'MGR',
        'MDDEMO_MGR':'MDDEMO_MGR',
        'MDSYS':'MDSYS',
        'ME':'ME',
        'MFG':'MFG',
        'MGR':'MGR',
        'MGWUSER':'MGWUSER',
        'MIGRATE':'MIGRATE',
        'MILLER':'MILLER',
        'MMO2':'MMO2',
        'MMO2':'MMO3',
        'MODTEST':'YES',
        'MOREAU':'MOREAU',
        'MRP':'MRP',
        'MSC':'MSC',
        'MSD':'MSD',
        'MSO':'MSO',
        'MSR':'MSR',
        'MTS_USER':'MTS_PASSWORD',
        'MTSSYS':'MTSSYS',
        'MWA':'MWA',
        'MXAGENT':'MXAGENT',
        'NAMES':'NAMES',
        'NEOTIX_SYS':'NEOTIX_SYS',
        'NNEUL':'NNEULPASS',
        'NOM_UTILISATEUR':'MOT_DE_PASSE',
        'NOMEUTENTE':'PASSWORD',
        'NOME_UTILIZADOR':'SENHA',
        'NUME_UTILIZATOR':'PAROL',
        'OAS_PUBLIC':'OAS_PUBLIC',
        'OCITEST':'OCITEST',
        'OCM_DB_ADMIN':'OCM_DB_ADMIN',
        'ODM':'ODM',
        'ODM_MTR':'MTRPW',
        'ODS':'ODS',
        'ODS_SERVER':'ODS_SERVER',
        'ODSCOMMON':'ODSCOMMON',
        'OE':'CHANGE_ON_INSTALL',
        'OE':'UNKNOWN',
        'OE':'OE',
        'OEMADM':'OEMADM',
        'OEMREP':'OEMREP',
        'OKB':'OKB',
        'OKC':'OKC',
        'OKE':'OKE',
        'OKI':'OKI',
        'OKO':'OKO',
        'OKR':'OKR',
        'OKS':'OKS',
        'OKX':'OKX',
        'OLAPDBA':'OLAPDBA',
        'OLAPSVR':'INSTANCE',
        'OLAPSVR':'OLAPSVR',
        'OLAPSYS':'MANAGER',
        'OLAPSYS':'OLAPSYS',
        'OMWB_EMULATION':'ORACLE',
        'ONT':'ONT',
        'OO':'OO',
        'OPENSPIRIT':'OPENSPIRIT',
        'OPI':'OPI',
        'ORACACHE':'ORACACHE',
        'ORACLE':'ORACLE',
        'ORADBA':'ORADBAPASS',
        'ORAPROBE':'ORAPROBE',
        'ORAREGSYS':'ORAREGSYS',
        'ORASSO':'ORASSO',
        'ORASSO_DS':'ORASSO_DS',
        'ORASSO_PA':'ORASSO_PA',
        'ORASSO_PS':'ORASSO_PS',
        'ORASSO_PUBLIC':'ORASSO_PUBLIC',
        'ORASTAT':'ORASTAT',
        'ORCLADMIN':'WELCOME',
        'ORDCOMMON':'ORDCOMMON',
        'DATA_SCHEMA':'LASKJDF098KSDAF09',
        'DBSNMP':'DBSNMP',
        'DBVISION':'DBVISION',
        'DDIC':'199220706',
        'DEMO':'DEMO',
        'DEMO8':'DEMO8',
        'DEMO9':'DEMO9',
        'DES':'DES',
        'DES2K':'DES2K',
        'DEV2000_DEMOS':'DEV2000_DEMOS',
        'DIANE':'PASSWO1',
        'DIP':'DIP',
        'DISCOVERER_ADMIN':'DISCOVERER_ADMIN',
        'DMSYS':'DMSYS',
        'DPF':'DPFPASS',
        'DSGATEWAY':'DSGATEWAY',
        'DSSYS':'DSSYS',
        'DTSP':'DTSP',
        'EAA':'EAA',
        'EAM':'EAM',
        'EARLYWATCH':'SUPPORT',
        'EAST':'EAST',
        'EC':'EC',
        'ECX':'ECX',
        'EJB':'EJB',
        'EJSADMIN':'EJSADMIN',
        'EJSADMIN':'EJSADMIN_PASSWORD',
        'EMP':'EMP',
        'ENG':'ENG',
        'ENI':'ENI',
        'ESTOREUSER':'ESTORE',
        'EVENT':'EVENT',
        'EVM':'EVM',
        'EXAMPLE':'EXAMPLE',
        'EXFSYS':'EXFSYS',
        'EXTDEMO':'EXTDEMO',
        'EXTDEMO2':'EXTDEMO2',
        'FA':'FA',
        'FEM':'FEM',
        'FII':'FII',
        'FINANCE':'FINANCE',
        'FINPROD':'FINPROD',
        'FLM':'FLM',
        'FND':'FND',
        'FOO':'BAR',
        'FPT':'FPT',
        'FRM':'FRM',
        'FROSTY':'SNOWMAN',
        'FTE':'FTE',
        'FV':'FV',
        'GL':'GL',
        'GMA':'GMA',
        'GMD':'GMD',
        'GME':'GME',
        'GMF':'GMF',
        'GMI':'GMI',
        'GML':'GML',
        'GMP':'GMP',
        'GMS':'GMS',
        'GPFD':'GPFD',
        'GPLD':'GPLD',
        'GR':'GR',
        'HADES':'HADES',
        'HCPARK':'HCPARK',
        'HLW':'HLW',
        'ABM':'ABM',
        'ADAMS':'WOOD',
        'ADLDEMO':'ADLDEMO',
        'ADMIN':'JETSPEED',
        'ADMIN':'WELCOME',
        'ADMINISTRATOR':'ADMIN',
        'ADMINISTRATOR':'ADMINISTRATOR',
        'AHL':'AHL',
        'AHM':'AHM',
        'AK':'AK',
        'ALR':'ALR',
        'AMS':'AMS',
        'AMV':'AMV',
        'ANDY':'SWORDFISH',
        'ANONYMOUS':'ANONYMOUS',
        'AP':'AP',
        'APPLMGR':'APPLMGR',
        'APPLSYS':'APPLSYS',
        'APPLSYS':'APPS',
        'APPLSYS':'FND',
        'APPLSYSPUB':'APPLSYSPUB',
        'APPLSYSPUB':'PUB',
        'APPLSYSPUB':'FNDPUB',
        'APPLYSYSPUB':'FNDPUB',
        'APPLYSYSPUB':'PUB',
        'APPS':'APPS',
        'APPS_MRC':'APPS',
        'APPUSER':'APPPASSWORD',
        'AQ':'AQ',
        'AQDEMO':'AQDEMO',
        'AQJAVA':'AQJAVA',
        'AQUSER':'AQUSER',
        'AR':'AR',
        'ASF':'ASF',
        'ASG':'ASG',
        'ASL':'ASL',
        'ASO':'ASO',
        'ASP':'ASP',
        'AST':'AST',
        'ATM':'SAMPLEATM',
        'AUDIOUSER':'AUDIOUSER',
        'AX':'AX',
        'AZ':'AZ',
        'BC4J':'BC4J',
        'BEN':'BEN',
        'BIC':'BIC',
        'BIL':'BIL',
        'BIM':'BIM',
        'BIS':'BIS',
        'BIV':'BIV',
        'BIX':'BIX',
        'BLAKE':'PAPER',
        'BLEWIS':'BLEWIS',
        'BOM':'BOM',
        'SYSMAN':'SYSMAN',
        'SYSTEM':'CHANGE_ON_INSTALL',
        'SYSTEM':'D_SYSPW',
        'SYSTEM':'MANAGER',
        'SYSTEM':'ORACLE',
        'SYSTEM':'SYSTEMPASS',
        'SYSTEM':'SYSTEM',
        'SYSTEM':'MANAG3R',
        'SYSTEM':'ORACL3',
        'SYSTEM':'0RACLE',
        'SYSTEM':'0RACL3',
        'SYSTEM':'ORACLE8',
        'SYSTEM':'ORACLE9',
        'SYSTEM':'ORACLE9I',
        'SYSTEM':'0RACLE9I',
        'SYSTEM':'0RACL39I',
        'TAHITI':'TAHITI',
        'TALBOT':'MT6CH5',
        'TDOS_ICSAP':'TDOS_ICSAP',
        'TEC':'TECTEC',
        'TEST':'PASSWD',
        'TEST':'TEST',
        'TEST_USER':'TEST_USER',
        'TESTPILOT':'TESTPILOT',
        'THINSAMPLE':'THINSAMPLEPW',
        'TIBCO':'TIBCO',
        'TIP37':'TIP37',
        'TRACESVR':'TRACE',
        'TRAVEL':'TRAVEL',
        'TSDEV':'TSDEV',
        'TSUSER':'TSUSER',
        'TURBINE':'TURBINE',
        'ULTIMATE':'ULTIMATE',
        'UM_ADMIN':'UM_ADMIN',
        'UM_CLIENT':'UM_CLIENT',
        'USER':'USER',
        'USER_NAME':'PASSWORD',
        'USER0':'USER0',
        'USER1':'USER1',
        'USER2':'USER2',
        'USER3':'USER3',
        'USER4':'USER4',
        'USER5':'USER5',
        'USER6':'USER6',
        'USER7':'USER7',
        'USER8':'USER8',
        'USER9':'USER9',
        'UTILITY':'UTILITY',
        'USUARIO':'CLAVE',
        'UTLBSTATU':'UTLESTAT',
        'VEA':'VEA',
        'VEH':'VEH',
        'VERTEX_LOGIN':'VERTEX_LOGIN',
        'VIDEOUSER':'VIDEOUSER',
        'VIF_DEVELOPER':'VIF_DEV_PWD',
        'VIRUSER':'VIRUSER',
        'VPD_ADMIN':'AKF7D98S2',
        'VRR1':'VRR1',
        'VRR1':'VRR2',
        'WEBCAL01':'WEBCAL01',
        'WEBDB':'WEBDB',
        'WEBREAD':'WEBREAD',
        'WEBSYS':'MANAGER',
        'WEBUSER':'YOUR_PASS',
        'WEST':'WEST',
        'WFADMIN':'WFADMIN',
        'WH':'WH',
        'WIP':'WIP',
        'WKADMIN':'WKADMIN',
        'WKPROXY':'WKPROXY',
        'WKPROXY':'CHANGE_ON_INSTALL',
        'WKSYS':'CHANGE_ON_INSTALL',
        'WKSYS':'WKSYS',
        'WKUSER':'WKUSER',
        'WK_TEST':'WK_TEST',
        'WMS':'WMS',
        'WMSYS':'WMSYS',
        'WOB':'WOB',
        'WPS':'WPS',
        'WSH':'WSH',
        'WSM':'WSM',
        'WWW':'WWW',
        'WWWUSER':'WWWUSER',
        'XADEMO':'XADEMO',
        'XDB':'CHANGE_ON_INSTALL',
        'XDP':'XDP',
        'XLA':'XLA',
        'XNC':'XNC',
        'XNI':'XNI',
        'XNM':'XNM',
        'XNP':'XNP',
        'XNS':'XNS',
        'XPRT':'XPRT',
        'XTR':'XTR',
        'MDDEMO_MGR':'MGR',
        'SYSTEM':'D_SYSTPW',
        'SYSTEM':'ORACLE8I',
        'SYSTEM':'0RACLE8',
        'SYSTEM':'0RACLE9',
        'SYSTEM':'0RACLE8I',
        'SYSTEM':'0RACL38',
        'SYSTEM':'0RACL39',
        'SYSTEM':'0RACL38I',
        'SYS':'0RACLE8',
        'SYS':'0RACLE9',
        'SYS':'0RACLE8I',
        'SYS':'0RACL38',
        'SYS':'0RACL39',
        'SYS':'0RACL38I',
        'ORDPLUGINS':'ORDPLUGINS',
        'ORDSYS':'ORDSYS',
        'OSM':'OSM',
        'OSP22':'OSP22',
        'OTA':'OTA',
        'OUTLN':'OUTLN',
        'OWA':'OWA',
        'OWA_PUBLIC':'OWA_PUBLIC',
        'OWF_MGR':'OWF_MGR',
        'OWNER':'OWNER',
        'OZF':'OZF',
        'OZP':'OZP',
        'OZS':'OZS',
        'PA':'PA',
        'PANAMA':'PANAMA',
        'PATROL':'PATROL',
        'PAUL':'PAUL',
        'PERFSTAT':'PERFSTAT',
        'PERSTAT':'PERSTAT',
        'PJM':'PJM',
        'PLANNING':'PLANNING',
        'PLEX':'PLEX',
        'PLSQL':'SUPERSECRET',
        'PM':'CHANGE_ON_INSTALL',
        'PM':'PM',
        'PMI':'PMI',
        'PN':'PN',
        'PO':'PO',
        'PO7':'PO7',
        'PO8':'PO8',
        'POA':'POA',
        'POM':'POM',
        'PORTAL_DEMO':'PORTAL_DEMO',
        'PORTAL_SSO_PS':'PORTAL_SSO_PS',
        'PORTAL30':'PORTAL30',
        'PORTAL30':'PORTAL31',
        'PORTAL30_ADMIN':'PORTAL30_ADMIN',
        'PORTAL30_DEMO':'PORTAL30_DEMO',
        'PORTAL30_PS':'PORTAL30_PS',
        'PORTAL30_PUBLIC':'PORTAL30_PUBLIC',
        'PORTAL30_SSO':'PORTAL30_SSO',
        'PORTAL30_SSO_ADMIN':'PORTAL30_SSO_ADMIN',
        'PORTAL30_SSO_PS':'PORTAL30_SSO_PS',
        'PORTAL30_SSO_PUBLIC':'PORTAL30_SSO_PUBLIC',
        'POS':'POS',
        'POWERCARTUSER':'POWERCARTUSER',
        'PRIMARY':'PRIMARY',
        'PSA':'PSA',
        'PSB':'PSB',
        'PSP':'PSP',
        'PUBSUB':'PUBSUB',
        'PUBSUB1':'PUBSUB1',
        'PV':'PV',
        'QA':'QA',
        'QDBA':'QDBA',
        'QP':'QP',
        'QS':'CHANGE_ON_INSTALL',
        'QS':'QS',
        'QS_ADM':'CHANGE_ON_INSTALL',
        'QS_ADM':'QS_ADM',
        'QS_CB':'CHANGE_ON_INSTALL',
        'QS_CB':'QS_CB',
        'QS_CBADM':'CHANGE_ON_INSTALL',
        'QS_CBADM':'QS_CBADM',
        'QS_CS':'CHANGE_ON_INSTALL',
        'QS_CS':'QS_CS',
        'QS_ES':'CHANGE_ON_INSTALL',
        'QS_ES':'QS_ES',
        'QS_OS':'CHANGE_ON_INSTALL',
        'QS_OS':'QS_OS',
        'QS_WS':'CHANGE_ON_INSTALL',
        'QS_WS':'QS_WS',
        'RE':'RE',
        'REP_MANAGER':'DEMO',
        'REP_OWNER':'DEMO',
        'REP_OWNER':'REP_OWNER',
        'REP_USER':'DEMO',
        'REPADMIN':'REPADMIN',
        'REPORTS_USER':'OEM_TEMP',
        'REPORTS':'REPORTS',
        'RG':'RG',
        'RHX':'RHX',
        'RLA':'RLA',
        'RLM':'RLM',
        'RMAIL':'RMAIL',
        'RMAN':'RMAN',
        'RRS':'RRS',
        'SAMPLE':'SAMPLE',
        'SAP':'SAPR3',
        'SAP':'6071992',
        'SAPR3':'SAP',
        'SCOTT':'TIGER',
        'SCOTT':'TIGGER',
        'SDOS_ICSAP':'SDOS_ICSAP',
        'SECDEMO':'SECDEMO',
        'SERVICECONSUMER1':'SERVICECONSUMER1',
        'SH':'CHANGE_ON_INSTALL',
        'SH':'SH',
        'SITEMINDER':'SITEMINDER',
        'SI_INFORMTN_SCHEMA':'SI_INFORMTN_SCHEMA',
        'SLIDE':'SLIDEPW',
        'SPIERSON':'SPIERSON',
        'SSP':'SSP',
        'STARTER':'STARTER',
        'STRAT_USER':'STRAT_PASSWD',
        'SWPRO':'SWPRO',
        'SWUSER':'SWUSER',
        'SYMPA':'SYMPA',
        'SYS':'CHANGE_ON_INSTALL',
        'SYS':'D_SYSPW',
        'SYS':'MANAGER',
        'SYS':'ORACLE',
        'SYS':'SYS',
        'SYS':'SYSPASS',
        'SYS':'MANAG3R',
        'SYS':'ORACL3',
        'SYS':'0RACLE',
        'SYS':'0RACL3',
        'SYS':'ORACLE8',
        'SYS':'ORACLE9',
        'SYS':'ORACLE8I',
        'SYS':'ORACLE9I',
        'SYS':'0RACLE9I',
        'SYS':'0RACL39I',
        'SYSADM':'SYSADM',
        'SYSADMIN':'SYSADMIN',
        'SYSMAN':'OEM_TEMP'
        }
    data_count = len(data)
    print "\r----------------------------------------------------"
    print "\r[+] The number of Default dict is:%s" % data_count
    resault = {}
    try:
        #创建开始时间戳
        start = time.clock()
        for i in data:
            user = i
            password = data[i]
            flag = oraclelogin(target,user,password,database,port)
            if flag[0]:
                resault[flag[1]] = flag[2]
            data_count = data_count - 1
        
        elapsed = (time.clock() - start)
        if len(resault) != 0:
            print "\r-------------------------------------------------"
            print "\r[!] Good luck O(^.^)O"
            j = 1
            for i in resault:
                print "%2d:Default User and Password is (%s----->%s)" % (j,i,resault[i])
                j+=1
            print "\r-------------------------------------------------"
        else :
            print "\r-------------------------------------------------"
            print "\r[!] Done,No Default Passwd Right %>_<%"
            print "\r-------------------------------------------------" 
        print "\r[+] Time used: %s%s" % (elapsed,"sec")
        print "\r[+] Pless enter 'Ctrl + C' or hold 10 sec to exit"
        time.sleep(10)
        print "\r-------------------------------------------------"
        print "\r[+] Thank you ! Bye."
    except KeyboardInterrupt:
        print "\r-------------------------------------------------"
	print "\r[!] Aborting..."
	print "\r[!] Exiting ... wait"
	sys.exit()
    except:
        print "\r-------------------------------------------------"
        print "\r[+] Thank you ! Bye."
        sys.exit()

if __name__ == "__main__":
    main()
