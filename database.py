import csv
import os

def mod_list():	#MODリストの読み取り
	with open(f'./mod_list.txt', 'r', encoding='utf-8') as modlist:
		return modlist.readlines()

def csv_open(mod_name, csv_name):	#CSVの読み取り
	with open('./{}/{}.csv'.format(mod_name, csv_name), encoding='utf8') as f:
		reader = csv.DictReader(f)
		return [row for row in reader]

def csv_edit(mod_name, csv_name, add_data):
	print(add_data)
	field_name = add_data.keys()
	current_list = csv_open(mod_name, csv_name)
	current_list.append(add_data)
	with open('./{}/{}.csv'.format(mod_name, csv_name), mode="w", encoding='utf8') as f:
		writer = csv.DictWriter(f, fieldnames=field_name)
		writer.writeheader()
		writer.writerows(current_list)

def csv_filter(list_name, key_name, value):
	return list(filter(lambda item: item[key_name] == value, list_name))
	
def csv_sort(list_name, key_name):
	return sorted(list_name, key=lambda x: x[key_name])

def csv_filter_sort(list_name, filter_key, filter_value, sort_key):
	tmp = csv_filter(list_name, filter_key, filter_value)
	return csv_sort(tmp, sort_key)


def check_value(mod_name, csv_name, key_name, value_name):
	country_data = csv_open(mod_name, csv_name)
	for d in country_data:
		if value_name in d[key_name]:
			return True

def check_folder(mod_name):
	ideology_folder = "./{0}/common/ideologies".format(mod_name)
	country_leader_folder = "./{0}/common/country_leader".format(mod_name)
	scripted_localisation_folder = "./{0}/common/scripted_localisation".format(mod_name)
	interface_folder = "./{0}/interface/icon_of_system".format(mod_name)
	localisation_folder = "./{0}/localisation/japanese/generic".format(mod_name)
	if not os.path.exists(mod_name):
		os.makedirs(mod_name)
	if not os.path.exists(ideology_folder):
		os.makedirs(ideology_folder)
	if not os.path.exists(country_leader_folder):
		os.makedirs(country_leader_folder)
	if not os.path.exists(scripted_localisation_folder):
		os.makedirs(scripted_localisation_folder)
	if not os.path.exists(interface_folder):
		os.makedirs(interface_folder)
	if not os.path.exists(localisation_folder):
		os.makedirs(localisation_folder)
	
def generation_value(mod_name, csv_name, key_name):
	list_1 = csv_open(mod_name, csv_name)
	list_2 = [d.get(key_name) for d in list_1]
	return list(set(list_2))
