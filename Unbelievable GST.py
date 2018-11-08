""" Unbelievable GST """
def main():
    """ input price and price prab """
    price = int(input())
    price_p = int(input())
    total = price + price_p
    print("Total: %.2f THB"%(total))
    print("Service: %.2f THB"%(total * 0.09))
    print("VAT: %.2f THB"%(((total * 0.09) + total) * (0.075)))
    print("Final Price: %.2f THB"%(total + (total * 0.09) + ((total * 0.09) + total) * (0.075)))
main()
