class Runner:
    def read_frame(self, source: str):
        # Read frame from source
        pass

    def preprocess_frame(self, frame):
        # Preprocess frame
        pass

    def send_frame(self, frame):
        # Send frame to inference service
        pass

    def receive_result(self):
        # Receive result from inference service
        pass

    def postprocess_result(self, result):
        # Postprocess result
        pass
