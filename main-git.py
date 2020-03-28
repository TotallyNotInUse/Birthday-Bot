'''
	Birthday Bot V3
    Copyright (C) 2020 TotallyNotInUse

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
   '''
import praw, re, os, time, preprocessing
posts_replied_to = "posts_replied.txt"
bad_file = "optouters.txt"
from tkinter import messagebox as msgbox
import tkinter as Tk
retry_atps = 0
from termcolor import colored
os.system("color")
from win10toast import ToastNotifier
toaster = ToastNotifier()
root = Tk.Tk()
root.withdraw()


christmas = False
version = "1.8.1"

def main(retry_atps):
	reddit = praw.Reddit("bot1")
	subreddit = reddit.subreddit("teenagers")
	if not os.path.isfile(posts_replied_to) or not os.path.isfile(bad_file):
		msgbox.showerror("Error", "File not found.")
	else:
		with open(posts_replied_to, "r") as f:
			posts_replied = f.read()
			posts_replied = posts_replied.split("\n")
			print("Posts I replied: "+str(len(posts_replied)))
			print("--------------------------------------------------")
			print("BirthdayBot Main. Version %s" % version)
			print("--------------------------------------------------")
			with open(bad_file, "r") as fa:
				bad_guys = fa.read()
	try:
		for submission in subreddit.stream.submissions():
			#print(submission)
			if str(submission.author) not in bad_guys:
				process_submission(submission, reddit, posts_replied)
	except Exception as e:
		print(e)
		retry_atps = retry_atps + 1
		print(colored("Connection Error. Retrying... %i", "red") %retry_atps)
		toaster.show_toast("BirthdayBot", "Connection Error. Retrying... %i" %(retry_atps), icon_path="alert.ico" , duration=15, )
		time.sleep(30)
		if retry_atps ==+ 5:
			msgbox.showerror("Connection error", "Max retry attempts reached.")
		else:
			main(retry_atps)

def process_submission(submission, reddit, posts_replied):
	try:
		if re.search("its my birthday", submission.title, re.IGNORECASE) or re.search("it's my birthday", submission.title, re.IGNORECASE) or re.search("my birthday", submission.title, re.IGNORECASE) or re.search("my bday", submission.title, re.IGNORECASE) or re.search("my b-day", submission.title, re.IGNORECASE):
			#print(submission.title, submission.author)
			if submission not in posts_replied:
				if christmas == True:
					submission.reply("Happy birthday!, %s \n \n ^(Beep Boop I'm a bot. Downvote me to remove.) ^(%s 🎄Merry Christmas!🎄 [Feedback](https://www.reddit.com/user/Birthday-Bot_/comments/f4jgsi/feedback/) | [Changelog](https://www.reddit.com/user/BirthdayBot_/comments/dgm89a/birthday_bot_changelog_111019/))" % (submission.author, version))
				else:
					submission.reply("🎂 Happy birthday!, %s \n \n ^(Beep Boop I'm a bot. Downvote me to remove.) ^(%s [Feedback](https://www.reddit.com/user/Birthday-Bot_/comments/f4jgsi/feedback/) | [Changelog](https://www.reddit.com/user/Birthday-Bot_/comments/f3kpft/changelog/)) To opt-out comment !optout.)" % (submission.author, version))
					#reddit.redditor(str(submission.author)).message('Happy Birthday!', "Happy birthday!, %s \n \n This message was sent to you due to [your post](%s) in r/teenagers. Since I'm banned from the subreddit, I have sent you a PM. To opt-out of these messages click [here](placeholder) \n \n Version %s [Feedback](https://www.reddit.com/user/HBirthdayBot/comments/emufzp/feedback/) | [Changelog](https://www.reddit.com/user/HBirthdayBot/comments/eienw2/changelog/)" % (submission.author, submission.url, version))
				print("replying to: %s, ID: %s" % (submission.title, submission.id))
				print("--------------------------------------------------")
				toaster.show_toast("BirthdayBot", "Bot replied to: '%s'." %(submission.title), icon_path="python.ico" , duration=15, )
				with open(posts_replied_to, "a") as f:
					f.write(submission.id+"\n")
	except Exception as e:
		print(e)
		retry_atps = retry_atps + 1
		print(colored("Connection Error. Retrying... %i", "red") %retry_atps)
		toaster.show_toast("BirthdayBot", "Connection Error. Retrying... %i" %(retry_atps), icon_path="alert.ico" , duration=15, )
		time.sleep(30)
		if retry_atps ==+ 5:
			msgbox.showerror("Connection error", "Max retry attempts reached.")
		else:
			main(retry_atps)

if __name__ == "__main__":
	main(retry_atps)
