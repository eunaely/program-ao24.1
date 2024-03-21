def format_date(date_str):
    """
    Formats a date string in the format "dd/mm/aaaa" to "dd de mês por extenso de aaaa".
    """
    months = {
        1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
        5: "maio", 6: "junho", 7: "julho", 8: "agosto",
        9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"
    }

    try:
        day, month, year = map(int, date_str.split("/"))
        formatted_month = months.get(month, "mês inválido")
        return f"{day} de {formatted_month} de {year}"
    except ValueError:
        return "Data inválida. Use o formato dd/mm/aaaa."

date_input = input("Digite uma data no formato dd/mm/aaaa: ")
formatted_date = format_date(date_input)
print(formatted_date)
