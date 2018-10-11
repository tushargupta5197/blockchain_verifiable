class AST_node(object):
	"""docstring for AST_node"""
	def __init__(self, linenum, operation, reason, line1 = None, line2 = None):
		self.linenum = linenum
		self.operation = operation
		self.reason = reason
		self.line1 = line1
		self.line2 = line2
		
		