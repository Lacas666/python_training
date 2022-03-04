# sum_negativ, amely parameterul kap egy listat, es osszegzi a benne szereplo negativ szamokat, azzal ter vissza
def sum_negativ(number_list):
    sum_numbers = 0
    for number in number_list:
        if number < 0:
            sum_numbers += number
    return sum_numbers


# to_minutes fv-t, amely parameterul megkapja az orak szamat es visszadaja a perceket
def to_minutes(hours):
    minutes=hours*60
    return minutes


# input_number fv-t egy parameterrel. A fuggveny beker a felhasznalotol egy szoveget
# a parameterrel megadott szoveget szamma konvertalja és azt adja vissza
def input_number():
    input_text = input("Adj meg egy szamot! ")
    return int(input_text)


# irjatok egy annotate_every_even_number fv-t, amely kap egy szam listat
# a lista elemeit kiirja egymas ala, ugy, hogy minden masodik elemet egy karakterrel bentebb ir
def annotate_every_even_number(numbers_list):
    counter = 1
    for number in numbers_list:
        if counter % 2 == 1:
            print(" "+str(number))
        else:
            print(number)
        counter +=