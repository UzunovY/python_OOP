from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    sold_artifacts = 0
    valid_artifacts = {"RenaissanceArtifact": RenaissanceArtifact,
                       "ContemporaryArtifact": ContemporaryArtifact}
    valid_collectors = {"Museum": Museum,
                        "PrivateCollector": PrivateCollector}

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.valid_artifacts:
            raise ValueError("Unknown artifact type!")

        for art in self.artifacts:
            if art.name == artifact_name:
                raise ValueError(f"{artifact_name} has been already registered!")

        self.artifacts.append(self.valid_artifacts[artifact_type](artifact_name, artifact_price, artifact_space))

        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.valid_collectors:
            raise ValueError("Unknown collector type!")

        for collector in self.collectors:
            if collector.name == collector_name:
                raise ValueError(f"{collector_name} has been already registered!")

        self.collectors.append(self.valid_collectors[collector_type](collector_name))
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        art = next((art for art in self.artifacts if art.name == artifact_name), None)
        collector = next((coll for coll in self.collectors if coll.name == collector_name), None)

        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")
        if not art:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(art.price, art.space_required):
            return "Purchase is impossible."

        self.sold_artifacts += 1
        self.artifacts.remove(art)
        collector.purchased_artifacts.append(art)
        collector.available_money -= art.price
        collector.available_space -= art.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {art.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        art = next((art for art in self.artifacts if art.name == artifact_name), None)

        if not art:
            return "No such artifact."

        self.artifacts.remove(art)
        return "Removed " + art.artifact_information()

    def fundraising_campaigns(self, max_money: float):
        affected_collectors = 0

        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                affected_collectors += 1

        return f"{affected_collectors} collector/s increased their available money."

    def get_auction_report(self):
        info = {}

        for c in self.collectors:
            info[c.name] = [c, c.purchased_artifacts]

        sorted_info = sorted(info.items(), key=lambda kvp: (-len(kvp[1][1]), kvp[0]))

        result = ["**Auction statistics**",
                  f"Total number of sold artifacts: {self.sold_artifacts}",
                  f"Available artifacts for sale: {len(self.artifacts)}",
                  "***"
                  ]

        for name, collector in sorted_info:
            result.append(str(collector[0]))

        return "\n".join(result).strip()
