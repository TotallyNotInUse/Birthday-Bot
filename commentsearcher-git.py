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
import praw, time, re
comments = []
from win10toast import ToastNotifier
toaster = ToastNotifier()

christmas = False
version = "1.8.1"

def main():
	reddit = praw.Reddit("bot1")
	print("Comment Searcher. Version %s" %version)
	print("--------------------------------------------------")
	me = reddit.redditor("BirthdayWishingBot")
	for comment in praw.models.util.stream_generator(reddit.inbox.unread):
		#print(comment)
		processInbox(comment, reddit)

def processInbox(comment, reddit):
	if re.search("Bad bot", comment.body, re.IGNORECASE):
		comment.reply("Sorry human, don't call me bad bot, please. \n \n ^(Beep Boop I'm a bot. Version %s [Feedback](https://www.reddit.com/user/Birthday-Bot_/comments/f4jgsi/feedback/) | [Changelog](https://www.reddit.com/user/Birthday-Bot_/comments/f3kpft/changelog/))" %version)
		print("Bad bot comment found and replied!")
		print("--------------------------------------------------")
		toaster.show_toast("BirthdayBot | Comment Searcher", "Bad Bot comment found", icon_path="python.ico" , duration=15, )
		comments.append(comment)
		reddit.inbox.mark_read(comments)
	if re.search("Good bot", comment.body, re.IGNORECASE):
		comment.reply("Thanks human! \n \n ^(Beep Boop I'm a bot. Version %s [Feedback](https://www.reddit.com/user/Birthday-Bot_/comments/f4jgsi/feedback/) | [Changelog](https://www.reddit.com/user/Birthday-Bot_/comments/f3kpft/changelog/))" %version)
		print("Good bot comment found and replied!")
		print("--------------------------------------------------")
		toaster.show_toast("BirthdayBot | Comment Searcher", "Good Bot comment found", icon_path="python.ico" , duration=15, )
		comments.append(comment)
		reddit.inbox.mark_read(comments)
	if re.search("Thanks birthdaybot", comment.body, re.I) or re.search("Thanks birthday bot", comment.body, re.I):
		comment.reply("You're welcome! \n \n ^(Beep Boop I'm a bot. Version %s [Feedback](https://www.reddit.com/user/Birthday-Bot_/comments/f4jgsi/feedback/) | [Changelog](https://www.reddit.com/user/Birthday-Bot_/comments/f3kpft/changelog/))" %version)
		print("Good bot comment found and replied!")
		print("--------------------------------------------------")
		toaster.show_toast("BirthdayBot | Comment Searcher", "Thanks Bot comment found", icon_path="python.ico" , duration=15, )
		comments.append(comment)
		reddit.inbox.mark_read(comments)

if __name__ == "__main__":
	main()
