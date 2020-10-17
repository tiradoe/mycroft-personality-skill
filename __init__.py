from mycroft import MycroftSkill, intent_file_handler


class MycroftPersonality(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('personality.mycroft.intent')
    def handle_personality_mycroft(self, message):
        self.speak_dialog('personality.mycroft')


def create_skill():
    return MycroftPersonality()

