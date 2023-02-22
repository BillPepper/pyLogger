red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
clear = "\033[0m"


class Logger:
    def __init__(self, level):
        self.level = level
        self.source = None
        self.color = ""

        if self.level > 3:
            print("Logging is disabled")

    def debug(self, *args):
        if self.level > 0:
            return

        self.color = green
        self.show("DEBUG", *args)

    def info(self, *args):
        if self.level > 1:
            return

        self.show("INFO", *args)

    def warn(self, *args):
        if self.level > 2:
            return

        self.color = yellow
        self.show("WARN", *args)

    def error(self, *args):
        if self.level > 3:
            return

        self.color = red
        self.show("FAIL", *args)

    def show(self, typ, *args):
        print(self.color + f"[{typ}] ", end="")
        if self.source:
            print(f"[{self.source}] ", end="")

        for arg in args:
            print(arg, end=" ")

        self.color = clear
        print("")


log = Logger(0)
log.source = "Some Module"
log.debug("hello", "debug")
log.info("hello", "info")
log.warn("hello", "warn")
log.error("hello", "error")
