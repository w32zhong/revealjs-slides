SECONDS=0
while true; do
	let "min=$SECONDS / 60"
	let "sec=$SECONDS % 60"
	echo "$min:$sec"
	sleep 1
done
