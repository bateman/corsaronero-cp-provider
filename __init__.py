from .main import CorsaroNero

def autoload():
    return CorsaroNero()

config = [{
    'name': 'corsaronero',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'CorsaroNero',
            'description': 'See <a href="http://ilcorsaronero.info">ilCorsaroNero</a>',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 20,
                    'description': 'Starting score for each release found via this provider.',
                },
                {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                }
            ],
        },
    ],
}]
