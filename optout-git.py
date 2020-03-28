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
import praw, time, re, os
comments = []
from win10toast import ToastNotifier
toaster = ToastNotifier()
optoutErs = "optouters.txt"

christmas = False
version = "1.8.1"

def main():
	reddit = praw.Reddit("bot1")
	if not os.path.isfile(optoutErs):
		msgbox.showerror("Error", "File not found.")
	print("Opt Out. Version %s" %version)
	print("--------------------------------------------------")
	me = reddit.redditor("BirthdayWishingBot")
	for comment in praw.models.util.stream_generator(reddit.inbox.unread):
		#print(comment)
		processInbox(comment, reddit)

def processInbox(comment, reddit):
	print(comment.author)
	if re.search("!optout", comment.body):
		with open(optoutErs, "a") as f:
			f.write(str(comment.author)+"\n")
			reddit.redditor(str(comment.author)).message('You have been opted out from Birthday-Bot_', 'Hello there, \n \n due to your comment saying you wanted to be opted out, you will no longer receive comments or messages from this bot. \n \n Have a nice day.')
			toaster.show_toast("BirthdayBot | OptOut", "An user has been opted out.", icon_path="python.ico" , duration=15, )
	comments.append(comment)
	reddit.inbox.mark_read(comments)

if __name__ == "__main__":
	main()

