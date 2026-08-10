count=0
recharge_amount=[299,399,299,999,299,150]
print("recharge_amount:",recharge_amount)
total=sum(recharge_amount)
print("total:",total)
highest_recharge=max(recharge_amount)
print("highest_recharge",highest_recharge)
for amount in recharge_amount:
    if amount==299:
        count+=1
print("count:",count)
new_amount=int(input("enter recharge amount:"))
print("new amount:",new_amount)
