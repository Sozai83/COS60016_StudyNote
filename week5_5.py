# .__next__() Method

def generator_function():
    yield "first value"
    yield "second value"
    yield "third value"

sentence = generator_function()


print(sentence.__next__())
print(sentence.__next__())
print(sentence.__next__())


sentence = generator_function()

# A while loop
while True:
    try:
        line = sentence.__next__()
        print(line)
    except StopIteration:
        break



# A for loop

sentence = generator_function()
for line in sentence:
    print(line)



# Generator expression

# Create lists.
line_items = ["USB Keyboard", "USB microphone", "¼ inch Headphone", "HDMI Cable", "USB Mouse"]

usb_line_items = [item for item in line_items if "USB" in item]


list_prices = [52.00, 125.00, 10.00, 8.00, 12.00]

discount_list_prices = [(price*0.9) for price in list_prices if price >= 20]
print(discount_list_prices)

generator_discount_list_prices = ((price*0.9) for price in list_prices if price >= 20)
print(discount_list_prices)

print(next(generator_discount_list_prices))
print(next(generator_discount_list_prices))

