class StateMachine:
    def change_state(self, scenario: Scenario, new_state: State):
        if new_state == State.init_startup:
            self.init_startup(scenario)
        elif new_state == State.in_startup_processing:
            self.in_startup_processing(scenario)
        elif new_state == State.init_shutdown:
            self.init_shutdown(scenario)
        elif new_state == State.in_shutdown_processing:
            self.in_shutdown_processing(scenario)
        elif new_state == State.active:
            self.active(scenario)
        elif new_state == State.inactive:
            self.inactive(scenario)

    def init_startup(self, scenario: Scenario):
        # Initialize startup
        pass

    def in_startup_processing(self, scenario: Scenario):
        # Process startup
        pass

    def init_shutdown(self, scenario: Scenario):
        # Initialize shutdown
        pass

    def in_shutdown_processing(self, scenario: Scenario):
        # Process shutdown
        pass

    def active(self, scenario: Scenario):
        # Set to active
        pass

    def inactive(self, scenario: Scenario):
        # Set to inactive
        pass
