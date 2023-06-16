
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

while True:
    try:
        input_number = int(input("Enter a number : "))
        if (0 < input_number <= 1000):
            break
        else:
            print("โปรดใส่ค่าตั้งแต่ {} - {}".format(0,1000))
    except ValueError:
        print("กรุณากรอกตัวเลข.")

# print(input_number)

def number_to_roman(number):
    roman_digits = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_text = ''
    
    for value in roman_digits:
        while number >= value:
            roman_text += roman_digits[value]
            number -= value
        
        
    return roman_text
    

roman_number = number_to_roman(input_number)
print(roman_number)
