invoices = open("CupcakeInvoices.csv")
costs = []
chocolate_costs = []
vanilla_costs = []
strawberry_costs = []

# for i in invoices:
#    i = i.rstrip('\n').split(',')
#    cost = float(i[4])
#    number = float(i[3])
#    total = cost * number
#    print("the type of cupcake is", i[2])
#    print("the total  for this order is", total)
#    costs = costs + [total]
#    print(costs)
   
# print(sum(costs))

for j in invoices:
   j = j.rstrip('\n').split(',')

   cost = float(j[4])
   number = float(j[3])
   total = cost * number

   if j[2] == "Chocolate":
      chocolate_costs = chocolate_costs + [total]
   elif j[2] == "Vanilla":
      vanilla_costs = vanilla_costs + [total]
   elif j[2] == "Strawberry":
      strawberry_costs = strawberry_costs + [total]

print("The total for chocolate is:", round(sum(chocolate_costs), 2))
print("The total for vanila is:", round(sum(vanilla_costs), 2))
print("The total for strawberry is:", round(sum(strawberry_costs), 2))



invoices.close()