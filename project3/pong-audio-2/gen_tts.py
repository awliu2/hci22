from gtts import gTTS

pause_speech = "Game paused. Say play to resume"
start_speech = "Go!"
easy_speech = "difficulty: easy"
hard_speech = "difficulty: hard"
insane_speech = "difficulty: insane"


pause_tts = gTTS(text=pause_speech, lang='en', slow=False)
start_tts  = gTTS(text=start_speech, lang='en', slow=False)
easy_tts = gTTS(text=easy_speech, lang='en', slow=False)
hard_tts = gTTS(text=hard_speech, lang='en', slow=False)
insane_tts = gTTS(text=insane_speech, lang='en', slow=False)

pause_tts.save("pause.mp3")

start_tts.save("start.mp3")

easy_tts.save("easy.mp3")

hard_tts.save("hard.mp3")

insane_tts.save("insane.mp3")
