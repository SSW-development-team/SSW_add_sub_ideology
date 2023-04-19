import PySimpleGUI as sg
import re
import database
import edit

class ModSelectWindow:
	def __init__(self):
		self.layout = [
			[sg.Text("作成Mod")],
			[sg.Combo(database.mod_list(), key="mod_name", readonly=True)],
			[sg.Button("決定")],
			[sg.Button("新規作成")]
		]
		self.window = sg.Window("作成Mod", self.layout, finalize = True)
	def main(self):
		while True:
			event, values = self.window.read()
			if event is None:
				sg.Popup("終了")
				break
			if event == "新規作成":
				self.window.close()
				NewModWindow().main()
			if event == "決定":
				if (values["mod_name"] == ""):
					sg.Popup("実装するModを選択してください")
				else:
					self.window.close()
					self.mod_name = values["mod_name"].replace('\n', '')
					AddCountryWindow(self.mod_name).main()
					
		self.window.close()

class NewModWindow:
	def __init__(self):
		self.layout = [
			[sg.Text("略称", size=(15, 1)), sg.InputText()],
			[sg.Text("イデオロギーID", size=(15, 1)), sg.InputText()],
			[sg.Button("決定")]
		]
		self.window = sg.Window("新規MOD", self.layout, finalize=True)

	def main(self):
		while True:
			event, values = self.window.read()
			if event is None:
				break
			if event == "決定":
				if (values["tag"] == ""):
					sg.Popup("MODの略称を入力してください")
				if (values["japanese"] == ""):
					sg.Popup("デフォルトとなるイデオロギーIDを入力してください")
				else:
					self.window.close()
					ModSelectWindow().main()

class AddCountryWindow:
	def __init__(self, mod_name):
		self.mod_name = mod_name
		main_ideology = []
		for t in database.csv_open(mod_name, "main_ideology"):
			main_ideology.append(t["id"])
		database.csv_open(mod_name, "main_ideology")
		self.layout0 = [
			[sg.Text("ID", size=(7, 1)), sg.InputText(key="id")],
			[sg.Text("名称", size=(7, 1)), sg.InputText(key="name")],
			[sg.Text("説明", size=(7, 1)), sg.InputText(key="desc")],
			[sg.Text("メイン", size = (7, 1)), sg.Combo(main_ideology, key = "main_ideology", readonly = True)],
			[sg.Text("特性用", size=(7, 1)), sg.InputText(key="trait")],
			[sg.Submit(button_text="サブイデ追加")],
		]
		self.window = sg.Window("サブイデ追加", self.layout0, finalize=True)
	
	def main(self):
		while True:
			event, values = self.window.read()
			if event is None:
				break
			if event == "サブイデ追加":
				i = 0
				if database.check_value(self.mod_name, "sub_ideology", "id", values["id"]) == True:
					i += 1
					sg.Popup("ID重複")
				if (i == 0):
					self.add_list = {"id": values["id"], "name": values["name"], "desc": values["desc"], "main_ideology": values["main_ideology"], "trait": values["trait"]}
					database.csv_edit(self.mod_name, "sub_ideology", self.add_list)
					
					edit.add_sub_ideology(self.mod_name)
					sg.Popup("サブイデ追加")
				print(i)
		self.window.close()

if __name__ == "__main__":
	ModSelectWindow().main()
