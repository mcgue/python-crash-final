# Final Project for Python Crash Course

# Obtain time of log-on or log-off
def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

class Event:
    def __inti(self, event_date, event_type, machine_name, user):
        self.event_date = event_date
        self.event_type = event_type
        self.machine_name = machine_name
        self.user = user

if __name__ == '__main__':
    get_event_date('PyCharm')


