# pylint: disable=too-few-public-methods
from typing import List
from dataclasses import dataclass


class Event:
    pass


@dataclass
class UserRegistered(Event):
    """代表系統已經把新增一筆訂閱用戶資訊"""
    user_id: str


@dataclass
class UserDevFetched(Event):
    """代表系統已經訂閱用戶的設備清單更新"""
    user_id: str


@dataclass
class DevStateUpdated(Event):
    """表示新訂閱用戶的設備狀態是第一次更新，不需要 pub ReportSubscriberDevState"""
    dev_id: str
    state: dict


@dataclass
class DevStateChanged(Event):
    """表示新訂閱用戶的設備狀態更新之後又有狀態變化，需要 pub ReportSubscriberDevState"""
    dev_id: str
    state: dict


@dataclass
class UserDevSynced(Event):
    """表示訂閱用戶設備已經全部更新狀態，需要 pub RequestSubscriberToSync"""
    user_id: str
