import random
class BoggleBoard:
  
  def __init__(self):
    self.create_16die()
    # print(self.totaldice)
    print("_ _ _ _\n_ _ _ _\n_ _ _ _\n_ _ _ _\n")
    

  def create_16die(self):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary={}
    for count, x in enumerate(alphabet):
      dictionary[count]=x
    dictionary[16]="Qu"
    # print(dictionary)
    list_of_dice=[]
    for y in range(0, 16):
      die={}
      for x in range(0, 6):
        a=random.randint(1,25)
        die[x]=dictionary[a]
      list_of_dice.append(die)
    self.totaldice= list_of_dice
    # returns 0-5 6 sided die, 16 of them (which is 0-15)

  def shake(self):
    grid_total=[]
    grid1=[]
    grid2=[]
    grid3=[]
    grid4=[]
    for count, dice in enumerate(self.totaldice):
      zero_to_five=random.randint(0,5)
      if count >=0 and count<4:
        grid1.append(dice[zero_to_five])
      elif count >=4 and count<8:
        grid2.append(dice[zero_to_five])
      elif count >=8 and count<12:
        grid3.append(dice[zero_to_five])
      elif count >=12 and count<16:
        grid4.append(dice[zero_to_five])
      grid_total.append(dice[zero_to_five])
    self.grid_of_grids=[grid1]+[grid2]+[grid3]+[grid4]
    self.grid_total=grid_total
    temp_grid=[]
    for count, current_letter in enumerate(grid_total):
      temp_grid.append(current_letter)
      if count==3 or count==7 or count==11 or count==15: 
        string="  ".join(temp_grid)
        string=string.replace("Qu ", "Qu")
        print(string)
        temp_grid=[]

  #returns first letter locations in array
  def get_first_letter(self, word_to_check):
    list_of_first_letter=[]
    letter_to_check=word_to_check[0]
    for current_row, x in enumerate(self.grid_of_grids):
      for current_index, current_letter in enumerate(self.grid_of_grids[current_row]):
        # print(current_letter)
        if letter_to_check==current_letter:
          list_of_first_letter.append([current_row, current_index])
    # print(list_of_first_letter)
    return list_of_first_letter
    #gets the row+index of first letter
    # define letter to check before calling function
    #takes letter locations and gives location of next letterS in array
  def return_next_letter_locations(self, letter_to_check, location_of_letter):
      self.new_locations=[]
      while(len(location_of_letter)>0):
        row=location_of_letter[0][0]
        index=location_of_letter[0][1]
        # print(row, index)
        row1=row-1
        row2=row
        row3=row+1
        index1=index-1
        index2=index
        index3=index+1
        self.check_row_and_index(row1, index1, letter_to_check)
        self.check_row_and_index(row1, index2, letter_to_check)
        self.check_row_and_index(row1, index3, letter_to_check)
        
        self.check_row_and_index(row2, index1, letter_to_check)
        self.check_row_and_index(row2, index3, letter_to_check)

        self.check_row_and_index(row3, index1, letter_to_check)
        self.check_row_and_index(row3, index2, letter_to_check)
        self.check_row_and_index(row3, index3, letter_to_check)
        location_of_letter= location_of_letter[1:]
      return self.new_locations
    #returns true or false based on valid row+index
  def check_if_valid_location(self, row, index):
    if row<0:
      return False
    elif row>=4:
      return False
    elif index<0:
      return False
    elif index>=4:
      return False
    else:
      return True
    #returns row and index if inputed values match letters
  def check_row_and_index(self, row, index, letter_to_check):
    if self.check_if_valid_location(row, index):
      if letter_to_check==self.grid_of_grids[row][index]:
          self.new_locations.append([row, index])
  #takes word, gets first letter from def get first letter
  #calls return next letter location, which checks if its a valid spot to check
  #using check if valid location, then checks if the row and index are equal to the 
  #current letter, then returns true if there is a location for the last letter
  #indicating the letter was completed
  def include_word(self, word_to_check):
    first_letter_location=self.get_first_letter(word_to_check)
    for letter in word_to_check:
      if letter==word_to_check[0]:
        continue
      first_letter_location= self.return_next_letter_locations(letter, first_letter_location)
      # print(first_letter_location, letter)
    if first_letter_location==[]:
      return False
    return True







print()


instance=BoggleBoard()
instance.shake()
# instance.grid_of_grids=list=[['R', 'O', 'O', 'D'], ['D', 'T', 'W', 'O'], ['F', 'I', 'W', 'U'], ['X', 'J', 'Z', 'Y']]
# print(instance.grid_of_grids)
# print(instance.check_if_valid_location(1, 4))
print(instance.include_word("WORD"))
