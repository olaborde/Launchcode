def ground_shipping(weight):
      if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + (price_per_pound * weight )  

print(ground_shipping(8.4))

#drone function
def drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return price_per_pound * weight  

print(drone_shipping(1.5))

premium_ground_shipping = 125.00

def cheapest_shipping_method(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_ground_shipping
  
  if ground < drone and ground < premium:
    cost = ground
    method = "Standard ground"
  elif premium < drone and premium < ground:
    cost = premium
    method = "Premium" 
  
  return "The cheapest option available is $%.2f with the %s shipping" %(cost, method)

print(cheapest_shipping_method(4.8))
print(cheapest_shipping_method(41.5))
