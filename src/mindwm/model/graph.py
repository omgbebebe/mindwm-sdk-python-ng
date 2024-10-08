from typing import ClassVar, Optional, List
from datetime import date, datetime, time, timedelta
import pandas as pd
from pydantic import Field
from neontology import BaseNode, BaseRelationship, init_neontology, auto_constrain

class MindwmNode(BaseNode):
    atime: int = 0
    #    atime: datetime = Field(
    #    default_factory=datetime.now
    #)

class User(MindwmNode):
    __primarylabel__: ClassVar[str] = "User"
    __primaryproperty__: ClassVar[str] = "username"
    username: str

class Host(MindwmNode):
    __primarylabel__: ClassVar[str] = "Host"
    __primaryproperty__: ClassVar[str] = "hostname"
    hostname: str

class Tmux(MindwmNode):
    __primarylabel__: ClassVar[str] = "Tmux"
    __primaryproperty__: ClassVar[str] = "socket_path"
    socket_path: str
#    host_id: str # for what?

class TmuxSession(MindwmNode):
    __primarylabel__: ClassVar[str] = "TmuxSession"
    __primaryproperty__: ClassVar[str] = "name"
    name: str
#    tmux_id: int #for what?

class TmuxPane(MindwmNode):
    __primarylabel__: ClassVar[str] = "TmuxPane"
    __primaryproperty__: ClassVar[str] = "title"
    title: str

class IoDocument(MindwmNode):
    __primarylabel__: ClassVar[str] = "IoDocument"
    __primaryproperty__: ClassVar[str] = "uuid"
    uuid: str
    input: str
    output: str
    ps1: str

class Clipboard(MindwmNode):
    __primarylabel__: ClassVar[str] = "Clipboard"
    __primaryproperty__: ClassVar[str] = "uuid"
    uuid: str
    time: int
    data: str

class Parameter(MindwmNode):
    __primarylabel__: ClassVar[str] = "Parameter"
    __primaryproperty__: ClassVar[str] = "key"
    key: str
    val: str

# Relations
class UserHasHost(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_HOST"
    source: User
    target: Host

class HostHasTmux(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_TMUX"
    source: Host
    target: Tmux

class TmuxHasTmuxSession(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_TMUX_SESSION"
    source: Tmux
    target: TmuxSession

class TmuxSessionHasTmuxPane(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_TMUX_PANE"
    source: TmuxSession
    target: TmuxPane

class TmuxPaneHasIoDocument(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_IO_DOCUMENT"
    source: TmuxPane
    target: IoDocument

class HostHasClipboard(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_CLIPBOARD"
    source: Host
    target: Clipboard

class UserHasParameter(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_PARAMETER"
    source: User
    target: Parameter

class HostHasParameter(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_PARAMETER"
    source: Host
    target: Parameter

class TmuxHasParameter(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_PARAMETER"
    source: Tmux
    target: Parameter

class TmuxSessionHasParameter(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_PARAMETER"
    source: TmuxSession
    target: Parameter

class TmuxPaneHasParameter(BaseRelationship):
    __relationshiptype__: ClassVar[str] = "HAS_PARAMETER"
    source: TmuxPane
    target: Parameter
