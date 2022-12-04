import shutil
from pathlib import Path

from click.testing import CliRunner

from py2of.__main__ import dump


def test_dump_cli(tmp_path: Path) -> None:
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=tmp_path) as temp_dir:
        shutil.copy(
            f"{Path(__file__).parent / 'case.py'}", Path(temp_dir)
        )  # copies case.py to test directory

        result = runner.invoke(dump, [str(Path(temp_dir) / "case.py")])
        assert result.exit_code == 0
        assert (
            Path(temp_dir) / "of_case" / "constant" / "turbulenceProperties"
        ).exists()
        assert (Path(temp_dir) / "of_case" / "system" / "controlDict").exists()
