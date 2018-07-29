import os
import glob



def last_zip():
	list_of_files = glob.glob('*.zip') # * means all if need specific format then *.csv
	latest_file = max(list_of_files, key=os.path.getctime)
	return latest_file


def test(ch):
	command1 = 'unzip -l ' + ch +'| grep .zip | grep -v "Archive"' + " | awk '{print $4}'"
	data = os.popen(command1).readlines()
	inside_zip_name = data[0].strip()
	pwd = inside_zip_name.replace(".zip","")
	os.system("unzip -P "+pwd+" "+ch)
	os.system("rm -rf "+ch)
	return last_zip()



def main():
	lasts = last_zip()
	a = test(lasts)




if __name__ == '__main__':
	main()


