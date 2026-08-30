"""Goes at tests/test_smoke.py.

Two tests worth having before you write any real code.

The first proves the package is actually installed and importable — which
catches the missing-``__init__.py`` problem, and catches a ``src/`` layout that
was never ``uv sync``'d.

The second proves the fixture zips are committed. That is a real failure mode:
``*.zip`` and ``data/`` are common .gitignore entries, and if either one
swallows ``tests/fixtures/`` then every parser test you write from Stage 2
onwards will pass locally and fail in CI with a confusing error. Better to fail
here, with an obvious message.
"""

from pathlib import Path

import energy_market_dashboard

FIXTURES = Path(__file__).parent / "fixtures"


def test_package_imports() -> None:
    assert energy_market_dashboard.__name__ == "energy_market_dashboard"


def test_fixture_zips_are_committed() -> None:
    names = sorted(p.name for p in FIXTURES.glob("*.zip"))
    assert any(n.startswith("PUBLIC_DISPATCHIS_") for n in names), names
    assert any(n.startswith("PUBLIC_P5MIN_") for n in names), names
