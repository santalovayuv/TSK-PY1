OUTPUT_FILE = "output. csv"

def to_csv_file(filename: str, headers: list[str], rows: list[list[str]], delimiter: str = ",", new_line: str = '\n'):
    headers = f'{delimiter}'. join(headers) + new_line
    with open(filename, 'w') as file:
        file.write(headers)
        for lines in rows:
            if lines is rows[-1]:
                lines = [x.rstrip() for x in lines]
                lines = f'{delimiter} '.join(lines)
                file.write(lines)
            else:
                lines = f'{delimiter} '.join(lines) + new_line
                file.write(lines)

headers_list = ['longitude', 'latitude', 'housing _median _age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']

data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '1661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

to_csv_file(filename=OUTPUT_FILE, headers=headers_list, rows=data)
with open(OUTPUT_FILE, 'r') as f:
    print(f.read())
