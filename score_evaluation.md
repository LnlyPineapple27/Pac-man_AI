Pacman or monsters only moves in 4 direction: left, right, bottom, up and cannot move
over or through the wall. The game has four levels:
-Level 1: 
+ Pac man: biết vị trí food
+ Monster: không có
+ Food: chỉ 1

-Level 2:
+ Pacman: biết vị trí food, đụng quái thì chết
+ Monster: Có, đứng yên
+ Food: chỉ 1

-Level 3:
+ Pacman: không thấy food nếu food nằm ngoài tầm nhìn, tầm nhìn = 3 bước gần nhất = các ô kề (8 ô x 3?)	
+ Monster: có nhiều quái, di chuyển 1 bước quanh vị trí ban đầu? lúc mới spawn, Pacman đi 1 bước thì di chyển 1 bước
+ Food: nhiều

-Level 4: map đóng?
+ Pacman: tìm càng nhiều thức ăn càng tốt, đụng quái thì chết
+ Monster: có nhiều quái, tìm và diệt pacman, quái đi qua nhau được, Pacman đi 1 bước thì di chyển 1 bước
+ Food: nhiều

==================================================================================================================
Point caculation:
+ Đi 1 bước: - 1 
+ Ăn 1 food: +20

==================================================================================================================
Score:
- Finish level 1 successfully. 							15%
- Finish level 2 successfully. 							15%
- Finish level 3 successfully. 							10%
- Finish level 4 successfully. 							10%
- Graphical demonstration of each step of the running process. 
- You can demo in console screen or use any other graphical library.		10%
- Generate at least 5 maps with difference in number and structure of
walls, monsters, and food.							10%
7 Report your algorithm, experiment with some reflection or comments. 		30%
Total 100%

==================================================================================================================
NOTE
Beside above requirements, report must also give the following information:
- Your detail information (Student Id, Full Name)
- Assignment Plan
- Environment to compile and run your program.
- Estimating the degree of completion level for each requirement.
- References (if any)
