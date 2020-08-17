### Steps to run files
`import code.addition`  
`code.addition.add(2, 4)`  
Expected output = 6  

`code.increment.inc(41)`  
Expected output = 42  

### Class 
`import code.increment as increment`  
`increment.inc(10)`  
Expected output = 11  

### 
`from code.addition import add`  
`add(20, 40)`  

### Steps to run the test files  
`python -m unittest test.test_increment`  
Expected output =  Success  

`python -m unittest test.test_addition`  
Expected output = Success  

`python -m unittest test.test_increment_neg`  
Expected output =  Failure  

`python -m unittest test.test_addition_neg`  
Expected output = Failure  
