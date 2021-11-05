from mycroft import MycroftSkill, intent_file_handler
from influxdb import InfluxDBClient

class MycroftInfluxdbSensorLookup(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.influxdb_host = "192.168.0.102"
        self.influxdb_port = 8086
        self.influxdb_user = "sensorlogger"
        self.influxdb_password = "sensorlogger"
        self.influxdb_dbname = "sensor_data"
        self.current_temperature = 0.0

    @intent_file_handler('lookup.sensor.influxdb.mycroft.intent')
    def handle_lookup_sensor_influxdb_mycroft(self, message):
        db_client = InfluxDBClient(self.influxdb_host, self.influxdb_port, self.influxdb_user, self.influxdb_password, self.influxdb_dbname)
        # Look up last temperature value in database
        query = 'SELECT last(temperature) FROM temperature WHERE time > now() - 1h;'
        result = db_client.query(query)
        point = result.get_points(measurement='temperature')
        for p in point:
            self.current_temperature = p['last']
        self.speak_dialog('lookup.sensor.influxdb.mycroft',{"temperature":self.current_temperature})

def create_skill():
    return MycroftInfluxdbSensorLookup()

