L = ["*      "  for x in range (1,7)]
L.append("*******")
A = ["      *      ", "     * *     ", "    *   *    ", "   *******   ", "  *       *  ", " *         * ", "*           *"]
R = [" ***** ", "*     *", "*     *", "****** ", "*  *   ", "*   *  ", "*    * "] 
word = [L + "  " + A + "  " + R for L,A,R in zip(L,A,R)]
print(*word, sep="\n" )