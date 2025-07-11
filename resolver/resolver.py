from abc import abstractmethod, ABC
from typing import List

from base_model import MCLBaseModel
from task_builder.models.download_task import DownloadTask


class Resolver(MCLBaseModel, ABC):

    @abstractmethod
    def resolve_dependencies(self, incompatible_mods: List[DownloadTask], old_mods: List[DownloadTask]) -> List[DownloadTask]:
        """
        This method populates DownloadTask.dependency_versions with the versions of the dependencies that are required to resolve the task.
        The versions inside DownloadTask.dependency_versions are always unique inside their respective list of tasks.
        """