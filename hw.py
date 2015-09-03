import lxml.etree
import operator

"""
	Class, which is describing system of tasks running.
"""
class TasksSystem:
	def __init__(self, runtime):
		self.runtime = int(runtime)
		self.tasks = [] # list of objects of class Task

	""" Method for reducing object of TaskSystem to string representation """
	def __str__(self):
		res = str(self.runtime)
		for i in range(len(self.tasks)):
			res += str(i) + ': ' + str(self.tasks[i])
		return res

	"""
	This method is need to call just after filling 'self.tasks' list.
	It sorting 'self.tasks' by priotiry attribute.
	"""
	def SortByPriority(self):
		self.tasks = sorted(self.tasks, key = operator.attrgetter('priority'))

	"""
	At first it set all tasks, which is done and need to start again, to undone state.
	At second it returns number of first task which is in undone state with biggest priority
	"""
	def GetFirstFreeTask(self, cur_time, cur_task):
		for i in range(len(self.tasks)):
			if (self.tasks[i].is_done()) and (cur_time % self.tasks[i].period == 0):
				self.tasks[i].done = 0
		for i in range(len(self.tasks)):
			if self.tasks[i].is_done() == False:
				return i
		return -1

"""
Each oject of this class contains information about one task.
This class provides method 'is_done()' which returns True if task is already done, and False instead
"""
class Task:
	def __init__(self, name, period, priority, duration):
		self.name = name
		self.period = int(period)
		self.priority = int(priority)
		self.duration = int(duration)
		self.done = 0

	def is_done(self):
		return self.done == self.duration

	""" Method for reducing object of Task to string representation """
	def __str__(self):
		return '\nname: ' + str(self.name) + '\nperiod: ' + str(self.period) + '\npriority: ' + str(self.priority) + '\nduration: ' + str(self.duration)


"""
This method creates object of TaskSystem with already filled tasks list from file (.xml format is need)
"""
def TasksSystemFromFile(xml_file):
	root = None
	try:
		root = lxml.etree.parse(xml_file)
	except:
		print 'Error with parsing ', xml_file
		return None
	i = 0
	res = None
	for elem in root.iter():
		if (i == 0):
			try:
				res = TasksSystem(elem.get('runtime'))
			except:
				'Error with parsing tag "system" in ', xml_file, ". runtime attribute wasn't found"
				return None
		else:
			try:
				res.tasks.append(Task(elem.get('name'), elem.get('period'), elem.get('priority'), elem.get('duration')))
			except:
				'Error with parsing some tag "task" in ', xml_file
				return None
		i += 1
	return res

"""
Class for saving logs
"""
class Log:
	"""
	'runtime' - value of runtime from TasksSystem
	"""
	def __init__(self, runtime):
		self.logs = []
		self.runtime = runtime

	"""
	This method adds new log.
	string 'action'   : start, continue
	string 'name'	  : task name
	   int 'timestamp': timestamp of log
	"""
	def add_log(self, action, name, timestamp):
		self.logs.append((action, name, timestamp))

	"""
	It writes xml representation of object of Log to xml file with name 'file_name'
	"""
	def ToFile(self, file_name):
		root = lxml.etree.Element('trace')
		root.set('runtime', str(self.runtime))
		for i in range(len(self.logs)):
			tag = lxml.etree.Element(self.logs[i][0])
			tag.set('name', str(self.logs[i][1]))
			tag.set('time', str(self.logs[i][2]))
			root.append(tag)
		f = file(file_name, 'w')
		f.write(lxml.etree.tostring(root, pretty_print=True))
		f.close()

	""" Method for reducing object of Log to string representation """
	def __str__(self):
		res = 'runtime: ' + str(self.runtime) + '\n'
		for i in range(len(self.logs)):
			res += str(self.logs[i]) + '\n'
		return res

def main():
	#read TaskSystem from file
	sys = TasksSystemFromFile('input_dynamic_pri.xml')
	if sys == None:
		return

	#sorting tasks by priority
	sys.SortByPriority()

	#creating object of Log
	log = Log(sys.runtime)
	cur_task = 0

	for i in range(sys.runtime):
		#get new current task
		new_cur_task = sys.GetFirstFreeTask(i, cur_task)

		#if all tasks is done at now - continue
		if (new_cur_task == -1):
			continue

		#get object, representing current task
		task = sys.tasks[new_cur_task]

		if (task.done == 0):
			#if this task didn't start at this period then it 'starts'
			log.add_log('start', task.name, i)
		else:
			#if this task already was started earlier in that period but was interrupted then it 'continue'
			if (new_cur_task != cur_task):
				log.add_log('continue', task.name, i)
		
		#update number of current task
		cur_task = new_cur_task
		if (task.done < task.duration):
			task.done += 1

	#print all logs to file
	log.ToFile('result.xml')
	print 'Result is written to "result.xml"'

main()