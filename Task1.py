# Name: - Neeraj Kumar
# ID: - 2047559

class FoodItem:
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0, serving = '0.00'):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.serving = serving
        pass

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def setServing(self, serving):
        self.serving = serving
        pass

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print(f'Number of calories for {reformat(self.serving)} serving(s): {reformat(self.calories_calculator())}')
        pass

    def calories_calculator(self):
        return str(float(self.serving) * ((9*self.fat)+(4*self.carbs)+(4*self.protein)))
        pass

def reformat(val):
    arr = [char for char in val]
    for i in range(len(arr)):
        if arr[i] =='.':
            if (i+2)==len(arr):
                arr.append('0')
            pass
    pass
    val = ''.join(item for item in arr)
    return val

if __name__ == '__main__':
    name = str(input())
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    serving = input()

    foodItem1 = FoodItem()
    foodItem1.setServing(serving)
    foodItem1.print_info()

    print()
    foodItem2 = FoodItem(name, fat, carbs, protein, serving)
    foodItem2.print_info()
    pass
