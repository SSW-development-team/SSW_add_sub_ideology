import database
import re

class Ideology:
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.main_ideology_list = database.csv_open(mod_name, "main_ideology")
		self.sub_ideology_list = database.csv_open(mod_name, "sub_ideology")
		
	def add_sub_ideologies(self):
		self.file = open('./{0}/common/ideologies/{0}_ideologies.txt'.format(self.mod_name), 'r', encoding='UTF-8')
		old_text = re.sub('types = [\s\S\n]*?\n\t\t\}\n\t\t\n\t\t' , "", self.file.read()).splitlines()
		new_text = []
		for line in old_text:
			new_text.append(line)
			for self.main_ideology in self.main_ideology_list:
				if self.main_ideology["id"] in line:
					new_text.append("\t\ttypes = {")
					new_text.append("\t\t\t" + self.main_ideology["id"] + "_ideology = {\t#" + self.main_ideology["name"])
					new_text.append("\t\t\t}")
					self.list = database.csv_filter_sort(self.sub_ideology_list, "main_ideology", self.main_ideology["id"], "name")
					for self.sub_ideology in self.list:
						new_text.append("\t\t\t" + self.sub_ideology["id"] + "_ideology = {\t#" + self.sub_ideology["name"])
						new_text.append("\t\t\t\tcan_be_randomly_selected = no")
						new_text.append("\t\t\t}")
					new_text.append("\t\t}")
		self.file = open('./{0}/common/ideologies/{0}_ideologies.txt'.format(self.mod_name), 'w', encoding='UTF-8')
		for line2 in new_text:
			self.file.write(line2)
			self.file.write("\n")
		
	def main(self):
		self.add_sub_ideologies()

class CountryLeader:
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.main_ideology_list = database.csv_open(mod_name, "main_ideology")
		self.sub_ideology_list = database.csv_open(mod_name, "sub_ideology")
		
	def add_trait(self):
		self.file = open('./{0}/common/country_leader/_{0}_ideology.txt'.format(self.mod_name), 'w', encoding='UTF-8')
		for self.main_ideology in self.main_ideology_list:
			self.list = database.csv_filter_sort(self.sub_ideology_list, "main_ideology", self.main_ideology["id"], "name")
			self.file.write('leader_traits = {{\t#{}\n'.format(self.main_ideology["name"]))
			self.file.write('\t{}_ideology_trait = {{\t#{}\n'.format(self.main_ideology["id"], self.main_ideology["trait"]))
			self.file.write("\t\trandom = no\n\t\tai_will_do = {\tfactor = 0\t}\n\t}\n")
			for t in self.list:
				self.file.write('\t{}_trait = {{\t#{}\n'.format(t["id"], t["trait"]))
				self.file.write("\t\trandom = no\n\t\tai_will_do = {\tfactor = 0\t}\n\t}\n")
			self.file.write('}\n')
	def main(self):
		self.add_trait()

class ScriptedLocalisation:
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.main_ideology_list = database.csv_open(mod_name, "main_ideology")
		self.sub_ideology_list = database.csv_open(mod_name, "sub_ideology")
		
	def add_scripted_localisation(self):
		self.file = open('./{0}/common/scripted_localisation/_{0}_sub_ideology.txt'.format(self.mod_name), 'w', encoding='UTF-8')
		self.file.write('defined_text = {\n\tname = GetIdeologyType\n')
		for self.main_ideology in self.main_ideology_list:
			self.file.write('\ttext = {{\t#{}\n'.format(self.main_ideology["name"]))
			self.file.write('\t\ttrigger = {{\thas_government = {}\t}}\n'.format(self.main_ideology["id"]))
			self.file.write('\t\tlocalization_key = [GetIdeologyType_{}]\n'.format(self.main_ideology["id"]))
			self.file.write('\t}\n')
		self.file.write('}\n')
		for self.main_ideology in self.main_ideology_list:
			self.file.write('defined_text = {{\t#{}\n'.format(self.main_ideology["name"]))
			self.file.write('\tname = GetIdeologyType_{}\n'.format(self.main_ideology["id"]))
			self.list = database.csv_filter_sort(self.sub_ideology_list, "main_ideology", self.main_ideology["id"], "name")
			for t in self.list:
				self.file.write('\ttext = {{\t#{}\n'.format(t["name"]))
				self.file.write('\t\ttrigger = {{\thas_country_leader_ideology = {}\t}}\n'.format(t["id"]))
				self.file.write('\t\tlocalization_key = {}\n'.format(t["id"]))
				self.file.write('\t}\n')
			self.file.write('\ttext = {\n\t\ttrigger = {\talways = yes\t}\n')
			self.file.write('\t\tlocalization_key = {}_ideology\n\t}}\n'.format(self.main_ideology["id"]))
			self.file.write('}\n')
	def main(self):
		self.add_scripted_localisation()

class Interface:
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.main_ideology_list = database.csv_open(mod_name, "main_ideology")
		self.sub_ideology_list = database.csv_open(mod_name, "sub_ideology")
		
	def add_graphics(self):
		self.file = open('./{0}/interface/icon_of_system/_{0}_ideologies.gfx'.format(self.mod_name), 'w', encoding='UTF-8')
		self.file.write('spriteTypes = {\t#メインイデオロギー\n')
		for self.main_ideology in self.main_ideology_list:
			self.file.write('\tspriteType = {{\t#{}\n'.format(self.main_ideology["name"]))
			self.file.write('\t\tname = "GFX_ideology_{}_group"\n'.format(self.main_ideology["id"]))
			self.file.write('\t\ttexturefile = "gfx/interface/ideologies/{}.png"\n'.format(self.main_ideology["id"]))
			self.file.write('\t}\n')
		self.file.write('}\n')
		for self.main_ideology in self.main_ideology_list:
			self.file.write('defined_text = {{\t#{}\n'.format(self.main_ideology["name"]))
			self.list = database.csv_filter_sort(self.sub_ideology_list, "main_ideology", self.main_ideology["id"], "name")
			for t in self.list:
				self.file.write('\tspriteType = {{\t#{}\n'.format(t["name"]))
				self.file.write('\t\tname = "GFX_ideology_{}"\n'.format(t["id"]))
				self.file.write('\t\ttexturefile = "gfx/interface/ideologies/{}/{}.png"\n'.format(self.main_ideology["id"], t["id"]))
				self.file.write('\t}\n')
			self.file.write('}\n')
	def main(self):
		self.add_graphics()

class Localisation:
	def __init__(self, mod_name):
		self.mod_name = mod_name
		self.main_ideology_list = database.csv_open(mod_name, "main_ideology")
		self.sub_ideology_list = database.csv_open(mod_name, "sub_ideology")
		
	def add_localisation(self):
		self.file = open('./{0}/localisation/japanese/generic/{0}_ideologies_l_japanese.yml'.format(self.mod_name), 'w', encoding = 'UTF-8-sig')
		self.file.write('l_japanese:\n')
		for self.main_ideology in self.main_ideology_list:
			self.file.write('#{}\n'.format(self.main_ideology["name"]))
			self.file.write(' {}:0 "{}"\n'.format(self.main_ideology["id"], self.main_ideology["name"]))
			self.file.write(' {}_noun:0 "{}"\n'.format(self.main_ideology["id"], self.main_ideology["name"]))
			self.file.write(' {}_desc:0 "{}政権"\n'.format(self.main_ideology["id"], self.main_ideology["name"]))
			self.file.write(' {}_drift:0 "日毎の{}への支援"\n'.format(self.main_ideology["id"], self.main_ideology["name"]))
			self.file.write(' {}_acceptance:0 "{}との外交容認"\n'.format(self.main_ideology["id"], self.main_ideology["trait"]))
			self.file.write(' {}_ideology:0 "{}"\n'.format(self.main_ideology["id"], self.main_ideology["name"]))
			self.file.write(' {}_ideology_desc:0 "{}"\n'.format(self.main_ideology["id"], self.main_ideology["desc"]))
			self.file.write(' {}_ideology_trait:0 "{}"\n'.format(
				self.main_ideology["id"], self.main_ideology["trait"]))
			self.list = database.csv_filter_sort(self.sub_ideology_list, "main_ideology", self.main_ideology["id"], "name")
			for t in self.list:
				self.file.write(' {}:0 "{}"\n'.format(t["id"], t["name"]))
				self.file.write(' {}_desc:0 "{}"\n'.format(t["id"], t["desc"]))
			self.file.write(' \n')
	def main(self):
		self.add_localisation()


def add_sub_ideology(mod_name):
	Ideology(mod_name).main()
	CountryLeader(mod_name).main()
	ScriptedLocalisation(mod_name).main()
	Interface(mod_name).main()
	Localisation(mod_name).main()
