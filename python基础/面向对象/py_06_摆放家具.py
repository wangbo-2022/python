class HouseItem:

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "【%s】占用的面积是【%.2f】平米" % (self.name, self.area)

class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return "户型:【%s】\n面积:【%.2f】平米\n剩余:【%.2f】平米\n家具:【%s】\n" % \
                (self.house_type, self.area, self.free_area, self.item_list)

    def add_item(self,item):
        if item.area > self.free_area:
            print("%s太大了，无法添加" % item.name)
            return

        print("要添加%s" % item)
        self.item_list.append(item.name)
        self.free_area -= item.area




bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.50)

print(bed)
print(chest)
print(table)

house = House("四室一厅", 140)
house.add_item(bed)
house.add_item(chest)
house.add_item(table)
print(house)

# a= [1,2,3]
# print(a)
# a.append([4, 5])
# print(a)
# a= [1,2,3]
# a.extend([4, 5])
# print(a)
