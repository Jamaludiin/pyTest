class MessageUtil:
    
    def __init__(self, message: str):
        self.message = message
    
    def print_message(self) -> str:
        return self.message
    
    def salutation_message(self) -> str:
        return f"Hi!{self.message}"