class laptop:
    price = ""
    processor = ""
    ram = ""


hp = laptop()
dell = laptop()
lenovo = laptop()

hp.price = 50000
hp.processor ="i5"
hp.ram="8gb"

dell.price = 60000
dell.processor = "i7"
dell.ram = "8gb"

lenovo.price = 70000
lenovo.processor = "i7"
lenovo.ram = "8gb"

print("hp price :",hp.price)
print("dell processor :",dell.processor)
print("lenovo ram :",lenovo.ram)
