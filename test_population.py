import pytest
from main import sort_by_area, sort_by_population

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

