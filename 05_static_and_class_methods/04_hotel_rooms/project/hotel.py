from project.room import Room


class Hotel:

    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: list[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int) -> "Hotel":
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        room = next((r for r in self.rooms if room_number == r.number), None)
        if room and not room.is_taken:
            room.take_room(people)
            self.guests += room.guests

    def free_room(self, room_number) -> None:
        room = next((r for r in self.rooms if room_number == r.number), None)
        if room:
            room.free_room()
            self.guests = sum(r.guests for r in self.rooms)

    def status(self) -> str:
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n" \
               f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}"
