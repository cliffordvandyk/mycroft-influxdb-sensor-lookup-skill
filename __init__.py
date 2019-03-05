from mycroft import MycroftSkill, intent_file_handler


class MycroftInfluxdbSensorLookup(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lookup.sensor.influxdb.mycroft.intent')
    def handle_lookup_sensor_influxdb_mycroft(self, message):
        self.speak_dialog('lookup.sensor.influxdb.mycroft')


def create_skill():
    return MycroftInfluxdbSensorLookup()

