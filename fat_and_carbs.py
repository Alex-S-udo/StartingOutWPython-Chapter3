# Programming Exercise 3.7 Calories from Fat and Carbohydrates
# May 3rd, 2010
# CS110
# Amanda L. Moen
# 7. Calories from Fat and Carbohydrates
# A nutritionist who works for a fitness club helps members by
# evaluating their diets.  As part of her evaluation, she asks
# members for the number of fat grams and carbohydrate grams
# that they consumed in a day.  Then, she calculates the number
# of calories that result from the fat, using the following
# formula:
#   calories from fat = fat grams X 9
# Next, she calculates the number of calories that result from
# the carbohydrates, using the following formula:
#   calories from carbs = carb grams X 4
# The nutritionist asks you to write a program that will make
# these calculations.

def main():

    # Ask for the number of fat grams.
    # Make sure to use "int" to save the input as an integer, float can also be used if needed, just format it to 2 decimal places using the format key word
    fat_grams = int(input('Enter the number of fat grams consumed: '))
    fat_calories(fat_grams)

    # Ask for the number of carb grams.
    # Make sure to use "int" to save the input as an integer, float can also be used if needed, just format it to 2 decimal places using the format key word
    carb_grams = int(input('Enter the number of carbohydrate grams consumed: '))
    carb_calories(carb_grams)

def fat_calories(fat_grams):
    # Calculate the calories from fat.
    # calories_from_fat = fat_grams*9
    #avoid any magic number by using CONSTANTS
    FAT_CONVERSION = 9
    calories_from_fat = fat_grams * FAT_CONVERSION
    print 'The calories from fat are', calories_from_fat

def carb_calories(carb_grams):
    # Calculate the calories from carbs.
    # calories_from_carbs = carb_grams * 4
    #avoid any magic number by using CONSTANTS
    CARBS_CONVERSION = 4
    calories_from_carbs = carb_grams * CARBS_CONVERSION
    print 'The calories from carbohydrates are', calories_from_carbs

# Call the main function.
main()
