
class ModelBasedReflexAgent:
    def __init__(self, target_temp):
        self.target_temp = target_temp
        self.current_temp = None
        self.heater_status = "off"  # Track the current state of the heater
    
    def sensor(self, temp):
        self.current_temp = temp
    
    def performance(self):
        if self.current_temp < self.target_temp and self.heater_status == "off":
            action = "Turn on the heater"
            self.heater_status = "on"
        elif self.current_temp >= self.target_temp and self.heater_status == "on":
            action = "Turn off the heater"
            self.heater_status = "off"
        else:
            action = "Do nothing (maintain current state)"
        return action
    
    def actuator(self):
        action = self.performance()
        print(f"{self.current_temp}°C (Heater: {self.heater_status}) => Action: {action}")

# Test the agent with different room temperatures
rooms = {
    "Living Room": 20,
    "Drawing Room": 22,
    "Kitchen": 24,
}

print("Model-Based Reflex Agent (Target Temperature: 22°C)")


for room, temp in rooms.items():
    print(f"{room}:")
    agent = ModelBasedReflexAgent(22)
    agent.sensor(temp)
    agent.actuator()
    print()









