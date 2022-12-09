# nab-bq-transfer

There is csv export function in the [NAB internet banking](https://www.nab.com.au/personal/online-banking/nab-internet-banking) to extract all the transaction histories.
This is a Python code to read the exported csv and shape the data a little bit to transfer it to Bigquery for further usage.
The entire system is built with 

CSV -> Cloud Storage -> Cloud Function -> Bigquery -> External BI tools (Data Studio)

![nab drawio](https://user-images.githubusercontent.com/59970261/206704044-8c91d42e-0e59-4b4a-9996-2af3a350d432.png)


## Dashboard


![Screen Shot 2022-12-09 at 22 38 46](https://user-images.githubusercontent.com/59970261/206704424-70f6eb80-cfc4-4dc6-9f22-57f1c98383e5.png)



