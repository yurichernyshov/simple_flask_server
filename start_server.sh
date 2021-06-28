#!/bin/bash


ports=(55555 55556 55557)


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


			for var in ${ports[*]}
			do
			  python3 app.py $var &
			done
			;;

		"2" )

			ps -aux | grep "python3 app"
			;;

		"3" )


			for var in ${ports[*]}
                        do
                          echo $var 
                        done
			;;
		"x" )
			exit 0
			;;
	esac
done

			
