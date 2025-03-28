def read_population_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                country, area, population = parts[0], parts[1], parts[2]
                try:
                    area = float(area)
                    population = float(population)
                    data.append((country, area, population))
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")
    return data


def sort_by_area(data):
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    print("\nСортування за площею:")
    for country, area, population in sorted_data:
        print(f"{country}: {area} км², {population} осіб")


def sort_by_population(data):
    sorted_data = sorted(data, key=lambda x: x[2], reverse=True)
    print("\nСортування за населенням:")
    for country, area, population in sorted_data:
        print(f"{country}: {area} км², {population} млн осіб")


if __name__ == "__main__":
    filename = "population.txt"
    data = read_population_data(filename)
    if data:
        sort_by_area(data)
        sort_by_population(data)
