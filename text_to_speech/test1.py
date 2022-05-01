import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volune', 4)
engine.setProperty('rate', 100)
engine.setProperty ('voice','french')

engine.say("bonjour christian je suis le PY TT S X 3")
engine.runAndWait()
for voice in engine.getProperty('voices'):
	if (voice.id == 'french'):
    		print ("id : %s " %voice.id )
    		print ("name : %s " %voice.name )
    		print ("langue : %s " %voice.languages )
    		print ("genre : %s " %voice.gender )
    
    
