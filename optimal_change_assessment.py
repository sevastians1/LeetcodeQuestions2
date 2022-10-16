# x=50.12-50
# y=1.5+2.61
# z=.01-.01
# print(x, y, round(z, 99))
def optimal_change(item_cost, amount_paid):
    ##base cases for not enough money and exact change
    if amount_paid<item_cost:
        return "Please enter more money"
    elif amount_paid==item_cost:
        return "You have no change"
    cost=amount_paid-item_cost
    # print(cost) calculating cost
    #using premade object to create smallest amt of change
    possible_change={
    100:"$100 bill",
    50:"$50 bill",
    20:"$20 bill",
    10:"$10 bill",
    5:"$5 bill",
    1:"$1 bill",
    .25:"quarter",
    .1:"dime",
    .05:"nickel",
    .01:"penny"
    }

    instances_of_change={}
    for x in possible_change:
        # print(x, "number")
        while cost>=x:
            name_of_coin=possible_change[x]
            cost=round(cost-x,2)
            if instances_of_change.get(name_of_coin):
                instances_of_change[name_of_coin]+=1
            else:
                 instances_of_change[name_of_coin]=1
            print(cost, "subtracted", instances_of_change)
    #previous loop minuses the amt of change based on the largest valid number and records the instances in dictionary
    final_text_push=[]
    for count, x in enumerate(instances_of_change):
        print(x)
        if count==len(instances_of_change)-1:
            final_text_push.append("and")
        if x=='penny' and instances_of_change[x]>1:
            final_text_push.append(f"{instances_of_change[x]} pennies")
        elif instances_of_change[x]>1:
            final_text_push.append(f"{instances_of_change[x]} {x}s")
        else:
            final_text_push.append(f"{instances_of_change[x]} {x}" )
        print(final_text_push)
    #previous loop accounts for edge cases and delivers instances of bills into the last element of the output
    text=f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is "
    return text+" ".join(final_text_push)
    
##item_cost, amount_paid
print(optimal_change(.73, 13))