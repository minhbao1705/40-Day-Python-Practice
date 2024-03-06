def calculate_can_chi_calendar(year):
    can = ""
    chi = ""

    if year%10==0:
        can="Canh"
    elif year%10==1:
        can="Tân"
    elif year%10==2:
        can="Nhâm"
    elif year%10==3:
        can="Quý"
    elif year%10==4:
        can="Giáp"
    elif year%10==5:
        can="Ất"
    elif year%10==6:
        can="Bính"
    elif year%10==7:
        can="Đinh"
    elif year%10==8:
        can="Mậu"
    elif year%10==9:
        can="Kỳ"

    if year%12==0:
        chi="Thân"
    elif year%12==1:
        chi="Dậu"
    elif year%12==2:
        chi="Tuất"
    elif year%12==3:
        chi="Hợi"
    elif year%12==4:
        chi="Tý"
    elif year%12==5:
        chi="Sửu"
    elif year%12==6:
        chi="Dần"
    elif year%12==7:
        chi="Mẹo"
    elif year%12==8:
        chi="Thìn"
    elif year%12==9:
        chi="Tỵ"
    elif year%12==10:
        chi="Ngọ"
    elif year%12==11:
        chi="Mùi"

    result = can + ' ' + chi

    return result

print(calculate_can_chi_calendar(2002))

# Cách 2
can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'ẤT', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mẹo', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']

year = int(input("Nhập vào năm: "))
can_i = year%10
chi_i = year%12
print(can[can_i] + ' ' + chi[chi_i])