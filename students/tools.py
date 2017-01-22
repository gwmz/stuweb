#encoding=utf-8
#author:朱晓强
#purposes:提供查询数据库函数
#data:2016/07/8
#phone:17862700815

import sys
import MySQLdb

def _UTF8(str = ""):
	"""decode to utf8

	"""
	return str.decode("gbk").encode("utf-8")

def returnConn():
	conn = MySQLdb.connect(host='172.29.152.190',user='root',passwd='hitdcos',db='student',port=3306,charset='utf8')
	# conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='lql',db='tornado_test',port=3306,charset='utf8')
	return conn

def searchDB(tableName, columns = None, where = None):
	if where == None and columns == None:
		sql = "select * from {0}".format(tableName) 
	elif where == None and columns != None:
		columns = ",".join(columns)
		sql = "select {0} from {1}".format(columns, tableName)
	elif where != None and columns == None:
		sql = "select * from {0} where {1}".format(tableName, where)
	else:
		columns = ",".join(columns)
		sql = "select {0} from {1} where {2}".format(columns, tableName, where)
	conn = returnConn()
	cur = conn.cursor()
	cur.execute(sql.decode('gbk').encode('utf-8') )
	results = cur.fetchall()
	return results
