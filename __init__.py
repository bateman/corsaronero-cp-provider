from .main import CorsaroNero

def start():
    return CorsaroNero()

config = [{
    'name': 'corsaronero',
    'groups': [
        {
            'tab': 'searcher',
            'subtab': 'providers',
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
            ],
        },
    ],
}]
