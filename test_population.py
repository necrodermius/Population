import pytest
from main import sort_by_area, sort_by_population, read_population_data


@pytest.fixture
def population_file(tmp_path):
    d = tmp_path / "data"
    d.mkdir()
    file_path = d / "test_population.txt"
    file_content = """Ukraine,603.7,44.13
Germany,357.4,83.02
Poland,312.7,37.97
invalid line
Brazil,8516,211.05
"""
    file_path.write_text(file_content, encoding='utf-8')
    return file_path


def test_read_population_data(population_file):
    data = read_population_data(population_file)
    assert len(data) == 4

    expected = [
        ("Ukraine", 603.7, 44.13),
        ("Germany", 357.4, 83.02),
        ("Poland", 312.7, 37.97),
        ("Brazil", 8516.0, 211.05)
    ]
    assert data == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [
                ("A", 5.0, 10.0),
                ("B", 6.0, 20.0),
                ("C", 4.0, 30.0),
            ],
            ["B", "A", "C"]
        ),
        (
            [
                ("X", 100.0, 5.0),
                ("Y", 200.0, 3.0),
                ("Z", 150.0, 10.0),
            ],
            ["Y", "Z", "X"]
        ),
    ],
)
def test_sort_by_area(input, expected, capsys):

    sort_by_area(input)
    captured = capsys.readouterr()

    lines = captured.out.strip().split("\n")

    sorted_lines = lines[1:]

    result_countries = []
    for line in sorted_lines:
        parts = line.split(":")
        country = parts[0].strip()
        result_countries.append(country)

    assert result_countries == expected


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            [
                ("A", 5.0, 10.0),
                ("B", 6.0, 20.0),
                ("C", 4.0, 30.0),
            ],
            ["C", "B", "A"]
        ),
        (
            [
                ("X", 1.0, 99.0),
                ("Y", 2.0, 100.0),
            ],
            ["Y", "X"]
        ),
    ],
)
def test_sort_by_population(input, expected, capsys):

    sort_by_population(input)
    captured = capsys.readouterr()
    
    lines = captured.out.strip().split("\n")

    sorted_lines = lines[1:]  
    
    result_countries = []
    for line in sorted_lines:
        parts = line.split(":")
        country = parts[0].strip()
        result_countries.append(country)
    
    assert result_countries == expected
