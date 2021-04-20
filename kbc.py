
print("             WELL-COME TO KBC                 ")
name=input('enter your name:-')
print("well-come",name)
quetion=["1)captal of india?\na)New Delhi       b)jaypur\nc)Mumbai          d)Aagra","2)whice is national food?\na)khova          b)jalebi\nc)rasgulla        d)none","3)Capital of Maharastra?\na)Delhi           b)jaypur\nc)Mumbai          d)chandigad",
"4)Whice place in boys campus?\na)Banglore          b)Pune\nc)Dharmshala          d)Delhi","5)------jay kishan?\na)jay Army           b)Jay kishan\nc)Jay javan           d)none",
"6)National food of Navgurukul?\na)Makcrony           b)Fride-Rice\nc)Halwa          d)Milk Food"]
Answer=["a","b","c","c","c","b"]
fifty=["{c-a}","{a-b}","{c-a}","{b-c}","{c-d}","{a-b}"]
def kbc(player):
		a=0
		Q=0
		Rs=0
		ll=0
		while a<=6:
		    a+=1
		    print(quetion[Q])
		    print("-----------------------------------------------------------")
		    # Q+=1
		    player=input("enter your answear:  ")
		    print()
		    if player==Answer[Q]:
		        Rs+=5000
		        print("you are win",Rs,"Rs")
		        print("-----------------------------------------------------------")
		        Q+=1
		    elif player=="5050":
		        if ll==0:
		            print(fifty[Q])
		            ll+=1
		            print ('you used your all life line ')
		            continue
		        else:
		            print ('you used your all lifeline so fuck off!')
		            break
		    else:
		
		        print("you are lose",Rs,"Rs")
		        break
		print("congratulation!!",name,"you are win",Rs,"₹")

		
olo=input()		
kbc(olo)