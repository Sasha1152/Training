class Coyote():
	@staticmethod
	def voice():
		print('Uuuuu..uuuuu..uuu')

	@classmethod
	def voice_2(cls):
		print('Rrrr..rr')

Coyote.voice()  # Uuuuu..uuuuu..uuu
Coyote.voice_2()  # Rrrr..rr

a = Coyote()
a.voice()
a.voice_2()
