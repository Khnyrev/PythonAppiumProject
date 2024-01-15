class SessionStorage:
    session = None

    def set_session(self, driver):
        self.session = driver

    def get_session(self):
        return self.session

    def reset_session(self):
        self.session.quit()
        self.session = None


session_storage = SessionStorage()
