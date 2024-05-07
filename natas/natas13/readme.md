the file "script.sh" is a bash script intended for automating the process of obtaining the pasword of natas13 

it starts by echoing a php script that cats the content of the file containing the password for the next level and redirecting the output of that echo to a file named image.jpeg

then it uses de the command xxd to check the hex of the file just created

then uses the printf command to print the corresponding magi bytes for a jpeg file and pipes it to dd command to replace the first 4bytes of the file 

we use xxd to check the hex version of the file to verify the magic bytes have been modified

consequently we create a POST reques using curl, set the required HEADERS and the Data required, emulating the functioning of the form. It is in this step where we set the variable filename to have the php suffix. The response is redirected to the file "response.html"

we use cat and grep to keep only the url of the uploaded "image", then creating the full url where the image is stored

we used the full url to make a GET request and filtering the response to print only the password for the next level. 

