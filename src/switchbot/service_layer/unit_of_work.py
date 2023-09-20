# pylint: disable=attribute-defined-outside-init
from __future__ import annotations
import abc

from switchbot.adapters import switchbotapi


class AbstractUnitOfWork(abc.ABC):
    devices: switchbotapi.AbstractSwitchBotApiServer

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for dev in self.devices.seen:
            while dev.events:
                yield dev.events.pop(0)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError


class ApiUnitOfWork(AbstractUnitOfWork):
    
    def __enter__(self):
        self.devices = switchbotapi.SwitchBotHttpApiServer()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def _commit(self):
        pass

    def rollback(self):
        pass