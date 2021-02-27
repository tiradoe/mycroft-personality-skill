from mycroft import MycroftSkill, intent_file_handler
import json


class MycroftPersonality(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('what.is.best.intent')
    def handle_best_in_life_dialog(self, message):
        self.speak_dialog('what.is.best')

    @intent_file_handler('who.shot.first.intent')
    def handle_han_shot_dialog(self, message):
        self.speak_dialog('who.shot.first')

    @intent_file_handler('murder.house.welcome.intent')
    def handle_murder_house_dialog(self, message):
        self.speak_dialog('murder.house.welcome')

    @intent_file_handler('darn.browns.intent')
    def handle_win_lose_browns(self, message):
        utterance = message.data.get('utterance')
        self.speak_dialog('darn.browns')
        if 'won' in utterance:
            self.gui['browns_status'] = 'won'
        elif 'steelers' in utterance:
            self.gui['browns_status'] = 'beat_steelers'
        else:
            self.gui['browns_status'] = 'lost'

        browns_data = {
            "intent": "darn_browns",
            "game_result": self.gui['browns_status']
        }

        # I'm not using the official QT gui so this
        # is a workaround until I find a better way
        self.gui.send_event("browns_data", browns_data)

    @intent_file_handler('here.we.go.brownies.intent')
    def handle_here_we_go_brownies(self, message):
        self.speak_dialog('here.we.go.brownies')

    @intent_file_handler('is.it.serious.intent')
    def handle_is_it_serious(self, message):
        self.speak_dialog('is.it.serious')


def create_skill():
    return MycroftPersonality()
