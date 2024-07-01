class Orchestrator:
    def __init__(self):
        self.state_machine = StateMachine()
    
    def read_event(self, command: dict):
        scenario_id = command.get("scenario_id")
        new_state = command.get("state")
        self.control_state(scenario_id, new_state)
    
    def control_state(self, scenario_id: int, new_state: State):
        scenario = scenarios.get(scenario_id)
        if scenario:
            self.state_machine.change_state(scenario, new_state)
    
    def execute_action(self, action: str):
        # Logic to control Runner based on action
        pass
