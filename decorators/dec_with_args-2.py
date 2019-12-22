def a_decorator_passing_arbitrary_arguments(function_to_decorate):
	def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
		print('*args:', args)
		print('**kwargs:', kwargs)
		function_to_decorate(*args, **kwargs)
	return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
	print("Python is cool, no argument here.")

function_with_no_argument()
print('----'*3)

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c, d=None, e=None):
	print('arguments:', a, b, c, d, e)

function_with_arguments(1, 2, 3, d=100, e=200)
