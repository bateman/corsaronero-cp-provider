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
            'icon': 'AAABAAEAEBAAAAAAAABoBQAAFgAAACgAAAAQAAAAIAAAAAEACAAAAAAAAAEAAAAAAAAAAAAAAAEAAAAAAAA1JRoA+fn5AMbCvwB6b2kApZ6ZAMfCvwDo5uUAdmtkALmzsADk4uAAmI+KAGhcVQDW09EA+Pf3ANfT0QCGfHYAeG1nALexrgCzrakA1NHPAIB2bwDk4uEAopqVALGrpwCCeHIAYVRMAPDv7gDPy8gAg3hyAMXAvgAyIRcAdWljAC0dEgC9uLQA39zaAG1hWQDRzcsAzMnGAO7t7ABbTkUAMB8VAOHe3QDd2tgA/v7+ADwsIgB/dG4AenBpAC4dEwC9uLUASz00ALm0sABtYVoAioF7ANfU0QCspaEAOiogAJqSjQB5bmcA3drZALeyrgC4sq4A+vr6ANnW1ABnW1MAaFtTADgoHgCmn5oAmJCLAOTj4QDb2NcAaV1WAIuBfADX1NIAtrCsAPT08wBmWVEAqKGdAOvp6QBYSkIA5+XkAFNGPQB1amMAZFdPADUkGgCim5YAgXdwAHNoYQDh390AYlVNAPHw7wDj4eAAsKqmAO/u7QAxIBYA6+roAOHf3gBwZF0AYlVOAI2EfgCvqKQAXlFJAO3s6wDMyMUALx4UAFpNRAB8cWoAKxoPALGqpwCMgnwAraaiAOzq6QB6b2gAm5OOAPv7+wCJgHoAaVxUAHxxawDq6OcAnpWRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKysrAUcNKysrKysFaysrKysrXh8gclkrKytZI28NKysrKytlT21zNBU8Ti4PRSsrKysrKysrFXQLAyIrKysrKysrK00XbGNKKzUQAwwrKysSHEthJXU6KhsaT0hAPxhCMAMHASsdMR43J1QrcXZTCCsMWRMRViw/aUEUW1crSTIrK09YX1wJUS0+PQYzXCsrKysCTCsrKw5iKysrcEQrKysrUQ8rKyskGQErPWRmKysrK2AoBFoTaGpSOEZqQysrKyshampdL2pqampqajYrKysrK1VqampqampqalBZKysrKys9CgBqampqZzkmKysrKysrKytuOzgWbSkrKysrKwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=',
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
                },
		{
                    'name': 'ignore_year',
                    'label': 'Ignore year',
                    'default': 0,
                    'type': 'bool',
                    'description': 'Will ignore the year in the search results',
                }
            ],
        },
    ],
}]
