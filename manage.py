import os

from flask_script import Manager, Shell, Server
from flask_script.commands import ShowUrls, Clean

from app.app import create_app
from app.settings import DevConfig, ProdConfig

app = create_app(DevConfig)

HERE = os.path.abspath(os.path.dirname(__file__))
TEST_PATH = os.path.join(HERE, 'tests')

manager = Manager(app)

@manager.command
def test():
    """ Run the tests """
    import pytest
    exit_code = pytest.main([TEST_PATH, '--verbose'])
    return exit_code

manager.add_command('runserver', Server())
manager.add_command('show-urls', ShowUrls())
manager.add_command('clean', Clean())

if __name__ == '__main__':
    manager.run()