#!/bin/bash

clear 

echo ""

echo -e "\e[5;32m   

                                                            
                                                            
        CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK   SSSSSSSSSSSSSSS 
     CCC::::::::::::CK:::::::K    K:::::K SS:::::::::::::::S
   CC:::::::::::::::CK:::::::K    K:::::KS:::::SSSSSS::::::S
  C:::::CCCCCCCC::::CK:::::::K   K::::::KS:::::S     SSSSSSS
 C:::::C       CCCCCCKK::::::K  K:::::KKKS:::::S            
C:::::C                K:::::K K:::::K   S:::::S            
C:::::C                K::::::K:::::K     S::::SSSS         
C:::::C                K:::::::::::K       SS::::::SSSSS    
C:::::C                K:::::::::::K         SSS::::::::SS  
C:::::C                K::::::K:::::K           SSSSSS::::S 
C:::::C                K:::::K K:::::K               S:::::S
 C:::::C       CCCCCCKK::::::K  K:::::KKK            S:::::S
  C:::::CCCCCCCC::::CK:::::::K   K::::::KSSSSSSS     S:::::S
   CC:::::::::::::::CK:::::::K    K:::::KS::::::SSSSSS:::::S
     CCC::::::::::::CK:::::::K    K:::::KS:::::::::::::::SS 
        CCCCCCCCCCCCCKKKKKKKKK    KKKKKKK SSSSSSSSSSSSSSS   
                                                            
                                                               
                                                            


"

echo -e "\e[1;31m  _______ Code By D1ARK-VA4U3 _______
"

echo "1. Termux  "

echo ""
echo "2. Linux"
echo ""
read -p "Enter Choose ::  " s 

if [[ $s == 1 ]];then 
termux-setup-storage 
mkdir /sdcard/fb-video
pkg install python -y
pip install --upgrade pip 
pip install fb-down 
clear 
echo -e "\e[1;32m  Code By  D1ARK-VA4U3 "

echo ""

read -p "Enter the Video Url Link :: " url 
echo ""
read -p "Enter the you want to give :: " s 
echo "" 
echo -e "\e[1;32m××××××××××× start ×××××××××××"
fbdown $url --output /sdcard/fb-video/$s.mp4 
sleep 2 
clear 
echo -e "\e[1;32m____________ Done ___________"

elif [[ $s == 2 ]];then
sudo pip install fb-down
mkdir fb-video
clear 
echo -e "\e[1;32m  Code By  D1ARK-VA4U3 "

echo ""

read -p "Enter the Video Url Link :: " url 
echo ""
read -p "Enter the you want to give ::  " s 
echo "" 
echo -e "\e[1;32m××××××××××× start ×××××××××××"
fbdown $url --output fb-video/$s.mp4 | grep url
sleep 2 
clear 
echo -e "\e[1;32m____________ Done ____________"
fi
