
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

while True:
    try:
        input_number = int(input("Enter a number : "))
        if (0 <= input_number < 10000000):
            break
        else:
            print("โปรดใส่ค่าตั้งแต่ {} - {}".format(0,10000000))
    except ValueError:
        print("กรุณากรอกตัวเลข.")

# print(input_number)

def number_to_thai_text(number):
    thai_digits = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
    thai_mains = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

    if(number == 0):
        return thai_digits[0]
    
    digits = []
    # หน่วย --> ล้าน
    while (number>0):
        digits.append(number % 10)
        number = number // 10
    
    len_digits = len(digits)
    text_digits = []
    # หน่วย --> ล้าน
    for index,element in enumerate(digits):
        if(element != 0):
            if(len_digits > 1 and index == 0 and digits[0] == 1 and digits[1] != 0):
                text_digits.append('เอ็ด')
            elif(len_digits > 1 and index == 1 and digits[1] == 1):
                text_digits.append(thai_mains[index])
            elif(len_digits > 1 and index == 1 and digits[1] == 2):
                text_digits.append('ยี่' + thai_mains[index])
            else:
                text_digits.append(thai_digits[element] + thai_mains[index])
        else:
            text_digits.append('')

    # ล้าน --> หน่วย
    text_digits.reverse()

    return ''.join(text_digits)


thai_text = number_to_thai_text(input_number)
print(thai_text)