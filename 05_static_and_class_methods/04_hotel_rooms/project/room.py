from typing import Optional


class Room:

    def __init__(self, number: int, capacity: int) -> None:
        self.number = number
        self.capacity = capacity
        self.guests: int = 0
        self.is_taken: bool = False

    def take_room(self, people: int) -> Optional[str]:
        if self.is_taken or people > self.capacity:
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests = people

    def free_room(self) -> Optional[str]:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0
