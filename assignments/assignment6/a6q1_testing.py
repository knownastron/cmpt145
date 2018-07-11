import LList as llist
import node as node


chain = llist.create()
twochain = llist.create()
emptychain = llist.create()

llist.add_to_front(chain, 5)

llist.add_to_back(chain, 7)
llist.add_to_back(chain, 12)
llist.add_to_back(chain, 3)
llist.add_to_back(chain, 6)
llist.add_to_back(chain, 2)
llist.add_to_back(chain, 11)

print(node.to_string(chain['head']))
llist.sorted(chain)
# llist.ya(cain)
print(node.to_string(chain['head']))
slice_list = llist.slice(chain, 2,6)
print(node.to_string(slice_list['head']))


# print(node.to_string(threechain['head']))
# yachain = threechain
# print(node.to_string(twochain['head']))
# llist.extend(threechain, twochain)
# print(node.to_string(threechain['head']))


# print(node.to_string(threechain['head']))
#

#
# # print(node.to_string(chain['head']))
# # print(node.to_string(chain['head']))
# # print(node.to_string(twochain['head']))
# # print(node.to_string(threechain['head']))
# print(node.to_string(threechain['head']))
# print(threechain['tail'])
