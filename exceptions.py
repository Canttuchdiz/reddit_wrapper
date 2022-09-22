
class CredentialsError(Exception):
    def __init__(self):
        self.message = "Credentials are invalid"

    def __str__(self):
        return self.message