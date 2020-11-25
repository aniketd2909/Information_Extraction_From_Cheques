# Information_Extraction_From_Cheques


This project is used to extract important information from bank cheques such as 
- Payee Name
- Amount in words and in figures (It also cross verifies both the amounts i.e in words and in figures before updating the csv file)
- Address of Bank
- IFSC Code of the bank 
- Cheque Number (Validates cheque number using dic.py)
- Date 
- Bank Name

After extracting information and validation of amount and cheque-no, it converts the information into a .csv file 


Prerequisites
- Install all the packages which are required. Go through all the files and install packages which are required if you don't have them.



Steps-
1) Run the IFS.py file(input is given at line 'im = Image.open('3.png')', you can change the file if you want to, they are named as 1.png,2.png,3.png).
2) IFS file will check the IFSC code of the cheque image and accordingly import SBI.py or Axis.py or DMK.py
3) seg.py is used to extract cheque number from the image which uses reference.png file (Check whether reference.png is present in the directory).
4) dic.py is used to verify cheque number using a already stored dictionary.
5) After successfully running the IFS.py file without getting any error, file.csv will be generated which will contain all the extracted information.
6) Change the image file in IFS.py file and re-run the code, new data will be generated which will be appended to the same .csv file.
7) The file.csv in the directory already contains information of all the 3 cheques, delete it before running your code for the first time.
