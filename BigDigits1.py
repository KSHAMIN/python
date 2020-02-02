import sys

Zero=["   ***   ",
      "  *   *  ",
      " *     * ",
      " *     * ",
      " *     * ",
      "  *   *  ",
      "   ***   "]
One=["  *  ",
     " **  ",
     "  *  ",
     "  *  ",
     "  *  ",
     "  *  ",
     " *** "]
     
Two=["  ***  ",
     " *   * ",
     " *  *  ",
     "   *   ",
     "  *    ",
     " *     ",
     "*****  "]
     
Three=[" ***** ",
       "     * ",
       "     * ",
       "  **** ",
       "     * ",
       "     * ",
       " ***** "]
       
Four=["     * ",
      "   * * ",
      "  *  * ",
      " *   * ",
      "*******",
      "     * ",
      "     * "]
      
Five=["  ****  ",
      "  *     ",
      "  *     ",
      "  ****  ",
      "     *  ",
      "     *  ",
      "  ****  ",]

Six=[" ****  ",
     " *     ",
     " *     ",
     " ****  ", 
     " *  *  ",
     " *  *  ", 
     " ****  ",]
     
Seven=[" ******* ",
       "      *  ", 
       "     *   ",
       "    *    ",
       "   *     ",
       "  *      ", 
       " *       ",]
             
             
Eight=[" ***** ",
       " *   * ", 
       " *   * ",
       " ***** ",
       " *   * ",
       " *   * ",
       " ***** ",]
       
Nine=[" ***** ",
      " *   * ",
      " *   * ",
      " ***** ",
      "     * ",
      "     * ",
      " ***** ",]       
       
       
Digits=[Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine]

try:
    digits=sys.argv[1]
    height=len(Zero)
    row=0
    while row<7:
	line=" "
	for digit in digits:
		line+=Digits[int(digit)][row].replace('*',digit)
		line+= ' '
	print(line)
	row+=1
except IndexError:
    print("usage:2.py<number>")
except ValueError as err:
    print(err,"in",digits)
