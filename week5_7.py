# Create lists.
line_items = ["USB Keyboard", "USB microphone", "¼ inch Headphone", "HDMI Cable", "USB Mouse"]

usb_line_items = [item for item in line_items if "USB" in item]

list_prices = [52.00, 125.00, 10.00, 8.00, 12.00]


# List comprehension.
lc_discounted_list_prices = [item_price-(0.1*item_price) for item_price in list_prices if item_price > 20]

# Generator expression.
ge_discounted_list_prices = (item_price-(0.1*item_price) for item_price in list_prices if item_price > 20)

# View the output.
print(lc_discounted_list_prices)
print(ge_discounted_list_prices)
print(next(ge_discounted_list_prices))