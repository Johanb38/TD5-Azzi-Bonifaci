#!/usr/bin/env python3

class Order:
	
	id=1
	def __init__(self, quantity, price, buy=True, id):
		self.quantity = quantity
		self.price = price
		self.buy = buy
		self.id+=1


class Book:
	
	Orders=[]

	def __init__(self, name):
		self.name=name

	def insert_buy(quantity,price):
		order=Order(quantity,price)
		Orders.append(order)
		sorted(Orders,key=lambda order: order[1])    #sorted by price
		str="--- Insert BUY " + quantity +"@"+ price +" id="+ id + " on "+ name
		print(str)
		str="Book on "+name
		print(str)
		for k in Orders:
			if k.buy==False:
				str="SELL "+quantity+"@"+price+" id"+id
				print(str)
		for k in Orders:
			if k.buy:
				str="BUY "+quantity+"@"+price+" id="+id
                                print(str)
		print('------------------------')

	def insert_sell(quantity,price):
		order=Order(quantity,price,buy=False)
		Orders.append(order)
		sorted(Orders,key=lambda order: order[1])    #sorted by price
		for k in Orders:
                        if k.buy==False:
                                str="SELL "+quantity+"@"+price+" id"+id
                                print(str)
                for k in Orders:
                        if k.buy:
                                str="BUY "+quantity+"@"+price+" id="+id
                                print(str)
                print('------------------------')
