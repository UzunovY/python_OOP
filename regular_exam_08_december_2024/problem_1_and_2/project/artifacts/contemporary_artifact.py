from project.artifacts.base_artifact import BaseArtifact


class ContemporaryArtifact(BaseArtifact):

    def artifact_information(self):
        return f"Contemporary Artifact: {self.name}; " \
               f"Price: {self.price:.2f}; " \
               f"Required space: {self.space_required}"
