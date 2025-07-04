from pathlib import Path
from typing import Annotated, List, TypeVar

from pydantic import StringConstraints, Field
from pydantic.types import PathType

T = TypeVar('T')

Base62Str = Annotated[str, StringConstraints(pattern=r"^[0-9A-Za-z]+$")]
SemanticVersion = Annotated[str, StringConstraints(pattern=r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")]
FilePath = Annotated[Path, PathType('file')]
DirectoryPath = Annotated[Path, PathType('dir')]
NotEmptyList = Annotated[List[T], Field(min_length=1)]
JarFile = Annotated[str, StringConstraints(pattern=r"^.*\.jar$")]
