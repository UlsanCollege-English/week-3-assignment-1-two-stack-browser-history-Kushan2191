from typing import List

class BrowserHistory:
    def __init__(self, start: str = "home"):
        self._cur = start
        self._back: List[str] = []
        self._fwd: List[str] = []
        self._start = start

    def visit(self, url: str) -> None:
        if url == self._cur:
            return
        # only push to back if current is not the initial start page
        if self._cur != self._start:
            self._back.append(self._cur)
        self._cur = url
        self._fwd.clear()

    def back(self) -> str:
        if not self._back:
            raise IndexError("No page to go back to")
        self._fwd.append(self._cur)
        self._cur = self._back.pop()
        return self._cur

    def forward(self) -> str:
        if not self._fwd:
            raise IndexError("No page to go forward to")
        self._back.append(self._cur)
        self._cur = self._fwd.pop()
        return self._cur

    def current(self) -> str:
        return self._cur
