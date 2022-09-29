import json
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType,VkBotMessageEvent
main_token = 'Your group token'
groupId = 'Your group id'
vs = vk_api.VkApi(token = main_token)
lp = VkBotLongPoll(vs,groupId)
toJson = {'main':dict(), 'forward':dict(), 'reply':dict()}


def getInfo(msg, att, whoSent):
	for i in range(len(msg)):
		if msg[i]=='@' and msg[i+1]=='a':
			msg = msg[:i] + msg[i+5:]
			break
	toJson[whoSent]['text'] = msg
	if att!=[]:
		toJson[whoSent]['url'] = list()
		for i in range(len(att)):
			if att[0]['type']=='photo':
				photoSizes = att[i]['photo']['sizes']
				photoSizes.sort(key=lambda x: x['height'])
				bestQuality = photoSizes[-1]['url']
			else:
				bestQuality = att[i]['url']
			toJson[whoSent]['url'].append(bestQuality)
	else:
		toJson[whoSent]['url'] = ''


for ev in lp.listen():
	if ev.type==VkBotEventType.MESSAGE_NEW:
		if ev.from_chat:
			mainObj=ev.object.message
			mainText=mainObj['text']
			mainAtt=mainObj['attachments']
			frwObj=ev.object.message['fwd_messages']
			try:
				repObj=ev.object.message['reply_message']
			except:
				pass
			if '@all' in mainText:
				getInfo(mainText,mainAtt,'main')
				if len(frwObj) != 0:	
					frwText=frwObj[0]['text']
					frwAtt=frwObj[0]['attachments']
					getInfo(frwText, frwAtt,'forward')
				else:
					toJson['forward']={}
				try:
					if len(repObj) != 0:	
						repText=repObj['text']
						repAtt=repObj['attachments']
						getInfo(repText, repAtt,'reply')
					else:
						toJson['reply']={}
				except:
					pass


				with open('toJson.json', 'w') as f:
					json.dump(toJson, f, indent=4, ensure_ascii=False)
				with open('toJson.json') as f:
					print(f.read())
