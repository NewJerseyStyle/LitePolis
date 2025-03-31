import configparser
import ray

DEFAULT_CONFIG_PATH = '~/.litepolis/config.conf'
SHARED_CONFIG_KEEPER_NAME = '_LITEPOLIS_CONFIG_GLOBAL'

def get_config(sector: str, key: str = None) -> str:
    util = ray.get_actor(SHARED_CONFIG_KEEPER_NAME)
    return ray.get(util.get_config.remote(sector, key))

def keep(config):
    util = ray.get_actor(SHARED_CONFIG_KEEPER_NAME)
    ray.get(util.keep.remote(config))

@ray.remote
class Utils:
    def keep(self, config):
        self.config = config

    def get_config(self, sector, key=None):
        if key is None:
            return dict(self.config.items('Section'))
        return self.config.get(sector, key)

    def set_config(self, sector, key, value):
        self.config.set(sector, key, value)

Utils.options(
    name=SHARED_CONFIG_KEEPER_NAME,
    get_if_exists=True,
    lifetime="detached"
).remote()