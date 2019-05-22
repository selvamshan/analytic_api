# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname('__file__'), '..')))

from flask_script import Manager, Server
from application import create_app
app = create_app()
manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP', '127.0.0.1'),
    port = int(os.getenv('PORT', 5000)))
)

if __name__ == "__main__":
    manager.run()