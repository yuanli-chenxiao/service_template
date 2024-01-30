import os
import sys

from mainapp import create_app

conf_file = os.path.abspath("config/default_config.py")
app = create_app(conf_file)


def parse_cmd_line(args):
    """
    parse cmd line
    :param args:
    :return:
    """
    host = "127.0.0.1"
    port = 5000
    
    i = 0
    while i < len(args):
        item = args[i]
        if item == "--host" and i + 1 < len(args):
            i = i + 1
            host = args[i]
        elif item == "--port" and i + 1 < len(args):
            i = i + 1
            port = int(args[i])

        i = i + 1

    return host, port


if __name__ == "__main__":
    start_host, start_port = parse_cmd_line(sys.argv)
    app.run(host=start_host, port=start_port)
