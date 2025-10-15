import sys

from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from config import SettingsServiceEnum, settings


def main() -> None:
    if settings.service == SettingsServiceEnum.API_V1:
        from presentation.api.v1.main import main as api_v1_main

        api_v1_main()
    elif settings.service == SettingsServiceEnum.CLI:
        from presentation.cli.main import main as cli_main

        cli_main()

    else:
        raise ValueError(f"Unknown service: {settings.service}")


if __name__ == "__main__":
    main()
