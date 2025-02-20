from typing import List

from project.player import Player


class Guild:

    def __init__(self, name: str) -> None:
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str) -> str:
        if player := next((p for p in self.players if p.name == player_name), None):
            self.players.remove(player)
            player.guild = "Unaffiliated"
            return f"Player {player.name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        return f"Guild: {self.name}\n" + '\n'.join(player.player_info() for player in self.players)
