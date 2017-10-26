with tempfile.TemporaryText() as f_in:
	f_in.write('Some text goes here')
	f_in.flush()
with open(f_in.name, 'r') as f_out:
	f_out.readlines()