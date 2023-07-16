class TextAnalyser:
	def __init__(self,text):
		self.text = text
		self.letters = []
		self.eror_text = "no unique letter"
	def analys(self):
		words = self.symbol_replaced().split(" ")
		for word in words:
			first_letter = True
			for letter in word:
				if first_letter == True:
					i=0
					for eqlet in word:
						if letter == eqlet:
							i = i+1
					if i == 1:
						self.letters.append(letter)
						first_letter = False
		for letter in self.letters:
			only_one = 0
			for ol in self.letters:
				if letter == ol:
					only_one = only_one+1
			if only_one == 1:
				return print(letter)
		return print(self.eror_text)
	def symbol_replaced(self):
		self.replaced_text = self.text
		self.replaced_text = self.replaced_text.replace("\n", " ")
		self.replaced_text = self.replaced_text.replace("-", "")
		self.replaced_text = self.replaced_text.replace(".", "")
		self.replaced_text = self.replaced_text.replace(",", "")
		self.replaced_text = self.replaced_text.replace("'", "")
		self.replaced_text = self.replaced_text.replace('"', "")
		return self.replaced_text
  
if __name__ == '__main__':
    textfortest = """


C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, it blows away your whole leg. (с) Bjarne Stroustrup

"""  
    tft = TextAnalyser(textfortest)
    tft.analys()