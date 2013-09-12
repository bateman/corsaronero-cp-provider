from .main import CorsaroNero

def start():
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
                }
            ],
        },
    ],
}]
