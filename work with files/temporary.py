import tempfile

with tempfile.TemporaryFile() as f_in:
	f_in.write('Some text goes here')
	f_in.flush()
with open(f_in.name, 'r') as f_out:
	data = f_out.readlines()
	print("Data from temporary file: %s" % data)
