from mycroft import MycroftSkill, intent_file_handler


class OpaCalm(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calm.opa.intent')
    def handle_calm_opa(self, message):
        self.speak_dialog('calm.opa')


def create_skill():
    return OpaCalm()

