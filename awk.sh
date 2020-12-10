for i in $(cat list);do
	for j in {01..12};do grep 'chr'$j'' snpfile/$i > ch$j/$i-ch$j;done
done 
