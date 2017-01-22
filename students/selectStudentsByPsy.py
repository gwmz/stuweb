#encoding=utf-8
#author:朱晓强
#purposes:基于大学生心理中心调查问卷数据筛选的学生
#data:2016/07/10
#phone:17862700815

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import MySQLdb
import json
import tools

class SelectStudentsByPsy(object):
	"""通过大学生心理问卷的得分情况分析筛选学生
	"""

	def __init__(self,):
		"""心理测试的阈值分数
		"""
		self.conn = tools.returnConn()
		self.rules_psychology_score = 3.6
		self.rules_psychology_scores = [0.9,1.8]
		self.normal_students_number = 0
		self.abnormal_students_number = 0

	def entry(self,mode = 0):
		"""mode=0
		   返回筛选出的学生的字典addStudentsDict, key值为"students",value值为筛选出的学生列表
		   格式为{"students":[ 
		   			{"stuId": stu, "reason":"心理测试分数高过阈值", "detailed": "成绩：score"},
		   			{ },
		   			{ } 
		   			]}
		   学生列表的元素是一个字典，字典中有三个key   "stuId"学生ID，  "reason"被筛选出的原因，  "detailed"心理测试得分
									     对应三个value  学生ID           心理测试分数高于阈值      测试得分
		   返回allNumDict    key "allNum"    value 显示总共多少学生的相关提示
		   返回selectNumDict key "selectNum" value 显示筛选出了多少学生的相关提示
		   返回titleDict      key "title"    value 显示相关提示信息,例如(学号   触发项目  具体原因)
		   mode=1:
		   返回学生的测试状况，返回字典addStuDict
		   key为"students"，value为保存学生评定结果的列表addStuList
		   addStuList的每个元素是字典，保存学生信息,每一个字典格式如下：
		   10个key   "situation1"  "situation2" ... "situation10"
		   10个value "是否有状况1" "是否有状况2" ... "是否有状况10"
		"""
		#开始筛选
		if mode == 0:
			stuDict,allNumDict,selectNumDict,titleDict = self.startSifting([0])
			return stuDict,allNumDict,selectNumDict,titleDict
		if mode == 1:
			stuDict = s.get_students_test_situations()
			return stuDict

	def select_by_psychology_data(self, exams = [], stuID = ""):
		"""
		   接收选择的心理测试答卷列表exams和学生学号列表stuID，返回该项该学生是否通过.
		   如果未通过返回false和心理测试的分数（即成绩),如果通过返回true和Null,若未查询到该学生，返回None
		"""
		# print type(stuID)
		exams_score = float(0.0)
		quesAndScore = tools.searchDB('psychology_data_copy', columns = ['testQuesNumber','score'],where = "stuID = {0}".format(stuID))
		#print quesAndScore
		if len(quesAndScore ) == 0 or len(exams) == 0:
			return None, None
		else:
			if len(exams) == 1:
				exams_score = exams_score + float(quesAndScore[int(exams[0])][1])
				if exams_score >= self.rules_psychology_scores[int(exams[0])]:
					return False, "成绩：{0}".format(exams_score)
				else:
					return True, None
			else :
				for i in exams:
					exams_score = exams_score + float(quesAndScore[int(i)][1])
					#print exams_score
				#判断分数是否符合规定标准
				if exams_score >= self.rules_psychology_score:
					return False, "成绩：{0}".format(exams_score)
				else:
					return True, None

	def startSifting(self, examList = []):
		"""开始筛选的函数，接收学生心理测试的试卷列表examList
		   1.返回筛选出的学生的字典addStudentsDict,格式为{"students":[ 
		   												{"stuId": stu, "reason":"心理测试分数高过阈值", "detailed": "成绩：score"},
		   												{ }
		   												] }
		   key 值为"students",value值为筛选出的学生列表，如上面的格式
		   学生列表的元素是一个个字典，字典中有三个key   "stuId"学生ID，  "reason"被筛选出的原因，  "detailed"被筛选出的详细原因即心理测试得分
									       对应三个value  学生ID           心理测试分数高于阈值       测试得分
		   2.返回allNumDict    key "allNum"    value 显示总共多少学生的相关提示
		   3.返回selectNumDict key "selectNum" value 显示筛选出了多少学生的相关提示
		   4.返回titleDict      key "title"    value 显示相关提示信息,例如(学号   触发项目  具体原因)
		"""
		#从数据库得到学生ID列表
		cursor = self.conn.cursor()
		cursor.execute("SELECT distinct stuID from psychology_data_copy")
		rows = cursor.fetchall()
		cursor.close()
		studentsID = []#学生ID列表
		for row in rows:
			studentsID.append(row[0])

		#定义字典,字典的key为"students"
		addStudentsDict = {}
		#字典的value为一个列表addStudentsList,保存筛选出的学生信息
		addStudentsList = []
		for stuID in studentsID:
			#符合条件的学生添加进列表，每一个学生的数据用字典保存
			save = self.select_by_psychology_data(exams = examList,stuID = stuID)
			if save[0] == False:
				addStudentsList.append( {} )
				addStudentsList[len(addStudentsList) - 1]["stuId"] = str(stuID)
				addStudentsList[len(addStudentsList) - 1]["reason"] = "心理测试分数高过阈值"
				addStudentsList[len(addStudentsList) - 1]["detailed"] = save[1]#心理测试成绩"成绩：{0}".format(exams_score)

		#将保存筛选出的学生列表addStudentsList作为字典addStudentsDict的值
		addStudentsDict["students"] = addStudentsList
		#一些提示信息：显示参与筛选的总人数，筛选出的人数等信息
		allStudentsDict = {}
		selectStudentsDict = {}
		titleDict = {}
		allStudentsDict["allNum"] = "正在筛选，筛选总人数:{0}".format(len(studentsID))
		selectStudentsDict["selectNum"] = "筛选完毕，需要重点关注的人数:{0}".format(len(addStudentsList))
		titleDict["title"] = "学号\t\t\t触发项目\t\t\t\t\t具体原因"
		
		self.abnormal_students_number = len(addStudentsList)#统计异常的学生人数
		self.normal_students_number = len(studentsID) - len(addStudentsList)#统计正常的学生人数
		return addStudentsDict,allStudentsDict,selectStudentsDict,titleDict

	def get_stuID_and_testResult(self,):
		"""返回得到的学生ID和心理测试的选项
		"""
		sql = "select stuID,testQuesResult from psychology_data_copy"
		cursor = self.conn.cursor()
		cursor.execute(sql)
		rows = cursor.fetchall()
		cursor.close()
		return rows
		
	def get_students_test_situations(self,):
		"""返回addStuDict
		   key为"students"，value为保存学生评定结果的列表addStuList
		   addStuList的每个元素是字典，保存学生信息,每一个字典格式如下：
		   10个key   "situation1"  "situation2" ... "situation10"
		   10个value "是否有状况1" "是否有状况2" ... "是否有状况10"
		"""
		rows = self.get_stuID_and_testResult()
		addStuDict = {}
		addStuList = []
		for row in rows:
			str_row = str(row[1])
			ans = "0"
			for char in str_row:
				if char == ',':
					continue
				else:
					ans = ans + char
			addStuList.append({})
			addStuList[len(addStuList) - 1]["stuId"] = row[0]
			if(int(ans[1])+int(ans[4])+int(ans[12])+int(ans[27])+int(ans[40])+int(ans[42])+int(ans[48])+int(ans[49])+int(ans[52])+int(ans[53])+int(ans[56])+int(ans[58]) > 36):
				addStuList[len(addStuList) - 1]["situation1"] = "躯体化症"
			else:
				addStuList[len(addStuList) - 1]["situation1"] = "无      "

			if(int(ans[3])+int(ans[9])+int(ans[10])+int(ans[28])+int(ans[38])+int(ans[45])+int(ans[46])+int(ans[51])+int(ans[55])+int(ans[65]) > 30):
				addStuList[len(addStuList) - 1]["situation2"] = "强迫症状"
			else:
				addStuList[len(addStuList) - 1]["situation2"] = "无      "

			if(int(ans[6])+int(ans[21])+int(ans[34])+int(ans[36])+int(ans[37])+int(ans[41])+int(ans[61])+int(ans[69])+int(ans[73]) > 27):
				addStuList[len(addStuList) - 1]["situation3"] = "人际关系"
			else:
				addStuList[len(addStuList) - 1]["situation3"] = "无      "

			if(int(ans[5])+int(ans[14])+int(ans[15])+int(ans[20])+int(ans[22])+int(ans[26])+int(ans[29])+int(ans[30])+int(ans[31])+int(ans[32])+int(ans[54])+int(ans[71])+int(ans[79])> 39):
				addStuList[len(addStuList) - 1]["situation4"] = "忧郁症状"
			else:
				addStuList[len(addStuList) - 1]["situation4"] = "无      "

			if(int(ans[2])+int(ans[17])+int(ans[23])+int(ans[33])+int(ans[39])+int(ans[57])+int(ans[72])+int(ans[78])+int(ans[80])+int(ans[86]) > 30):
				addStuList[len(addStuList) - 1]["situation5"] = "焦虑症状"
			else:
				addStuList[len(addStuList) - 1]["situation5"] = "无      "
			if(int(ans[11])+int(ans[24])+int(ans[63])+int(ans[67])+int(ans[74])+int(ans[81]) > 18):
				addStuList[len(addStuList) - 1]["situation6"] = "敌对症状"
			else:
				addStuList[len(addStuList) - 1]["situation6"] = "无      "

			if(int(ans[13])+int(ans[25])+int(ans[47])+int(ans[50])+int(ans[70])+int(ans[75])+int(ans[82]) > 21):
				addStuList[len(addStuList) - 1]["situation7"] = "恐怖症状"
			else:
				addStuList[len(addStuList) - 1]["situation7"] = "无      "
			if(int(ans[8])+int(ans[18])+int(ans[43])+int(ans[68])+int(ans[76])+int(ans[83]) > 18):
				addStuList[len(addStuList) - 1]["situation8"] = "偏执症状"
			else:
				addStuList[len(addStuList) - 1]["situation8"] = "无      "
			if(int(ans[7])+int(ans[16])+int(ans[35])+int(ans[62])+int(ans[77])+int(ans[84])+int(ans[85])+int(ans[87])+int(ans[88])+int(ans[90]) > 30):
				addStuList[len(addStuList) - 1]["situation9"] = "精神病性"
			else:
				addStuList[len(addStuList) - 1]["situation9"] = "无      "
			if(int(ans[13])+int(ans[25])+int(ans[47])+int(ans[50])+int(ans[70])+int(ans[75])+int(ans[82]) > 21):
				addStuList[len(addStuList) - 1]["situation10"] = "睡眠饮食"
			else:
				addStuList[len(addStuList) - 1]["situation10"] = "无      "
		addStuDict["students"] = addStuList
		return addStuDict

	def testBak(self,stuID = ""):
		"""接受学生ID，返回字典res,格式如下
			试卷类型 分数 结论
			res = {"1":{"grade":"2.85","res":"异常"},
			  "2":{"grade":"1.8","res":"正常"}
				}
		"""
		res = {}
		scores = tools.searchDB('psychology_data_copy', columns = ['score'],where = "stuID = {0}".format(stuID))
		# print scores
		# for score in scores:
		# 	print score[0]
		res["1"] = {}
		if(scores[0][0] > self.rules_psychology_scores[0]):
			res["1"]["grade"] = str(scores[0][0] )
			res["1"]["res"] = "异常"
		else:
			res["1"]["grade"] = str(scores[0][0] )
			res["1"]["res"] = "正常"
		res["2"] = {}
		if(scores[1][0]  > self.rules_psychology_scores[1]):
			res["2"]["grade"] = str(scores[1][0] )
			res["2"]["res"] = "异常"
		else:
			res["2"]["grade"] = str(scores[1][0] )
			res["2"]["res"] = "正常"
		return res

	def getPsyNormalNumber(self,):
		"""返回字典保存正常学生与异常学生的人数统计
		   key为"psy"  value为一个字典{}，字典中有两个key "normal" "abNormal"对应两个值 正常学生人数 异常学生人数
		"""
		count = {}
		count["psy"] = {}
		count["psy"]["normal"] = str(self.normal_students_number)
		count["psy"]["abNormal"] = str(self.abnormal_students_number)
		return count

if __name__ == '__main__':
	#开始筛选 mode=0
	s=SelectStudentsByPsy()
	stuDict,allNumDict,selectNumDict,titleDict = s.entry(mode = 0)
	newStuId = stuDict["students"]
	print allNumDict["allNum"]
	print selectNumDict["selectNum"]
	print titleDict["title"]
	for content in newStuId:
		print ("{0}\t\t{1}\t\t{2}".format(content["stuId"],content["reason"],content["detailed"]))
	#显示每个学生的测试状况 mode=1
	addStuDict = s.entry(mode = 1)
	addStuList = addStuDict["students"]
	for i in addStuList:
		print i["stuId"],i["situation1"],i["situation2"],i["situation3"],i["situation4"],i["situation5"],i["situation6"],i["situation7"],i["situation8"],i["situation9"],i["situation10"]
	#一个简单的示例stuID = "111010108"
	res = s.testBak("111010108")
	print res
	print res["1"]["grade"],res["1"]["res"]
	print res["2"]["grade"],res["2"]["res"]
	#得到正常学生与异常学生的人数统计
	count = s.getPsyNormalNumber()
	print count