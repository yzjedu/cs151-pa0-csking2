#This program converts Net Income and Cost of Investment into the ROI (Return on Investment)

#Prompt the user to enter the Net Income

Net_Income_str = input('Enter the Net Income:')
Net_Income_int = int(Net_Income_str)

#Prompt the user to enter the Cost of Investment

Cost_of_Investment_str = input('Enter the Cost of Investment:')
Cost_of_Investment_int = int(Cost_of_Investment_str)

#Divide the Net Income by the Cost of Investment then multiply the result by 100 to find the ROI

ROI = (Net_Income_int / Cost_of_Investment_int) * 100

#Display the ROI

print('You\'re ROI is:', ROI)

