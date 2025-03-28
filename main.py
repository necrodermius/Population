def read_population_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                country, area, population = parts[0], parts[1], parts[2]
                try:
                    area = float(area)
                    population = int(population)
                    data.append((country, area, population))
                except ValueError:
                    print(f"Помилка у рядку: {line.strip()}")
    return data


def sort_by_area(data):
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)
    print("\nСортування за площею:")
    for country, area, population in sorted_data:
        print(f"{country}: {area} км², {population} осіб")