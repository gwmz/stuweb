#coding=utf-8
#encoding=utf-8
#author:赵振华
#purpose:渲染前台首页内容
#date：2016/07/12
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import tools

from tools import _UTF8

class initIndex:
	"""返回首页上需要显示的信息

	"""
	def __init__(self):
		self.db = tools.returnConn()
		self.getGrade()

	def getGrade(self):
		#课程名 挂科人数
		courDict = {}
		courData = tools.searchDB(tableName = "course_data")
		for con in courData:
			courDict[con["courseID"]] = {"name":con["courseName"],"count":0}
		examData = tools.searchDB(tableName = "exam_results")
		for con in examData:
			if con["initialScore"] < 60:
				courDict[con["courseID"]]["count"] += 1
		res = {}
		for con in courDict:
			res[courDict[con]]
		return res

	def getPsy(self):
		#心理健康人数、心里不健康人数
		pass

	def getHeatly(self):
		#健康人数、不健康人数
		pass

	def stuBasic(self):
		#姓名 学号 联系方式 家庭住址
		pass

#initBak,cardBak,familyBak,gradeBak,healthyBak,sleepBak,timelineBak,testBak
def initBak():
	res = {"grade":{"线性代数":"30","工科数学":"40"},
		"psy":{"normal":"50","abNormal":"60"},
		"healthy":{"normal":"40","abNormal":"1"},
		"stuInfo":{
			"11040120":{"name":"张三","phone":"13883838","familyAdd":"湖南省尼玛市"},
			"11040121":{"name":"张四","phone":"1388323438","familyAdd":"陕西省尼玛市"}
			}
		}
	return res

def cardBak(stuID = ""):
	#日期 消费总金额 消费总次数 分数
	res = {"data":"20140101",
		"money":"20123",
		"num":"2154",
		"grade":"0.7"
		}
	return res

def familyBak(stuID = ""):
	#父母姓名 联系方式 工作单位
	res = {"fatherName":"张三",
		"fatherMobileNumber":"18363120000",
		"fatherWorkUnit":"湖南科技有限责任公司",
		"motherName":"李四",
		"motherWorkUnit":"18363121111",
		"motherMobileNumber":"湖南小学"
		}
	return res

def gradeBak(stuID = ""):
	#科目	考试成绩	学分
	res = {"工科数学":{"grade":"60","credit":"6.5","examData":"20140404"},
		"线性代数":{"grade":"62","credit":"6","examData":"20140405"},
		}
	return res

def testBak(stuID = ""):
	#试卷类型 分数 结论
	res = {"1":{"grade":"2.85","res":"异常"},
	  "2":{"grade":"1.8","res":"正常"}
		}
	return res

def sleepBak(stuID = ""):
	#日期 异常归寝时间
	res = {"20140404":"23:56:67归寝",
		"20140405":"23:30:12归寝",
		}
	return res

def healthyBak(stuID = ""):
	res = {stuID:"健康"}
	return res

def timelineBak(stuID = ""):
	res = {"20140404":"工科数学分数为59",
		"20140404":"23:56:67归寝",
		"20140405":"线性代数分数为45",
		}
	return res


if __name__ == "__main__":
	test = initIndex()
	
