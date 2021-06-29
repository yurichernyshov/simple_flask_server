#!/bin/bash


START_PORT=55555
NUMBER_OF_PORTS=1

while [ 1 ]
do

	echo "---------------------------------------------------"
	echo "|                                                 |"
	echo "| simple_flask_server application is started      |"
	echo "| options:                                        |"
	echo "| 1): start API servers                           |"
	echo "| 2)  check status                                |"
	echo "| 3): stop API servers                            |"
	echo "| x): exit                                        |"
	echo "|                                                 |"
	echo "---------------------------------------------------"

	read status


	case $status in


		"1" )


			for ((var=0; var<$NUMBER_OF_PORTS; var++))
			do
 	 		  python3 app.py $(($START_PORT+$var)) &
			done
			;;

		"2" )

			ps -aux | grep "python3 app" | head -n -1
			;;

		"3" )


			for P in $(ps -aux | grep 'app.py' | head -n -1 | awk '{print $2}')
			do 
			  kill -9 $P 
		        done
			;;
		"x" )
			exit 0
			;;
	esac
done

			
