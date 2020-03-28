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
import praw, time, os
retry_atps = 0
from termcolor import colored
os.system("color")
from win10toast import ToastNotifier
toaster = ToastNotifier()

christmas = True
version = "1.8.1"

def main(retry_atps):
	reddit = praw.Reddit("bot1")
	print("BirthdayBot Auto delete program. Version %s" %(version))
	print("--------------------------------------------------")
	me = reddit.redditor("BirthdayWishingBot")
	try:
		while True:
			for comment in me.comments.new(limit=20):
				processComment(comment, reddit)
				time.sleep(60)
	except Exception:
		retry_atps = retry_atps + 1
		print(colored("Connection Error. Retrying... %s", "red") %retry_atps)
		toaster.show_toast("BirthdayBot | Auto Delete", "Connection Error. Retrying... %i" %(retry_atps), icon_path="alert.ico" , duration=15)
		time.sleep(30)
		if retry_atps ==+ 5:
			msgbox.showerror("Connection error", "Max retry attempts reached.")

		else:
			main(retry_atps)
def processComment(comment, reddit):
	if comment.score < 0:
		comment.delete()
		print("Bot deleted comment: '%s'" % comment.body)
		print("-----------------------------------------------------------")

if __name__ == "__main__":
	main(retry_atps)
