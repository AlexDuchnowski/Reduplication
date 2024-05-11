# A slow way of adding context to each line of a subtitles file

head -n-2 $1 | sed '1i\\' | sed '1i\\' > temp_1.txt
head -n-1 $1 | sed '1i\\' > temp_2.txt
tail -n+2 $1 | sed '$a\\' > temp_3.txt
paste $1 temp_1.txt temp_2.txt $1 temp_3.txt
rm temp_*.txt
