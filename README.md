# LongPollVkParser
Parser of important messages in VK dialogs using vkLongPoll.
Message with "@all" tag will be received and written in json format.


Instructions:
1) Creat vk group
2) Add this group to desired dialog.
3) Get a group token and group id.
4) Fill 4 and 5 lines in main.py with these data.
5) run main.py and get needed data.

Output json file:
Json file has 3 arrays: main, forwarded and replyed messages.
Each of these arrays has a field with text and an "url" array that contains links to all photos and files in the message.
