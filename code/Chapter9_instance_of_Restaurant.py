#Chapter_9_instance_import_Restraurant.py
class Restaurant():
    def __init__(self):
        self.special = "Yanzhou fried rice"
        self.open_time = 8
        self.close_time = 22
    def show_info(self):
        print("Our special food is Yangzhou fried rice.\n" + "Our business hours are from " + str(self.open_time) + ":00 to " + str(self.close_time) + ":00. ")
