def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    years = [int(input("Digite um ano: ")) for _ in range(4)]
    result = [{"ano": year, "bisexto": is_leap_year(year)} for year in years]
    print(result)

if __name__ == "__main__":
    main()
