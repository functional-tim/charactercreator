import gevent
import signal
import zerorpc
from .pyApi import PyApi


def echo(phrase: str) -> None:
    """A dummy wrapper around print."""
    print(phrase)


def main() -> int:
    port = "1234"
    addr = 'tcp://127.0.0.1:' + port
    s = zerorpc.Server(PyApi())
    s.bind(addr)

    gevent.signal(signal.SIGTERM, s.stop)
    gevent.signal(signal.SIGINT, s.stop)

    s.run()
    return 0


if __name__ == '__main__':
    exit(main())
